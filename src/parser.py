import yaml
from pathlib import Path
from lark import Lark
from src import engine, util

steps = yaml.load(util.read(f"{Path(__file__).parent}/steps.yaml"), Loader=yaml.FullLoader)

def loadStep(module_name, class_key):
	name = steps[module_name][class_key].split('.')[-1]
	module = __import__(f"src.{steps[module_name][class_key]}");
	return getattr(getattr(getattr(module, module_name), name), name)


def handleExtract(data):
	adapter = data[0].value
	uri = data[1].value.replace('"', '')
	
	try:
		return loadStep("extractors", adapter)(uri=uri)
	except:
		raise ValueError(f"Extract adapater \"{adapter}\" not found")


def handleTransform(data):
	source = data[0].value.replace('"', '')
	transformer = data[1].value
	args = list(map(lambda token: token.value.replace('"', ''), data[2::]))

	try:
		return loadStep("transformers", transformer)(source, *args)
	except BaseException as err:
		print(err)
		raise ValueError(f"Transformer \"{transformer}\" not found")


def handleLoad(data):
	source = data[0].value.replace('"', '')
	adapter = data[1].value
	uri = data[2].value.replace('"', '')
	
	try:
		return loadStep('loaders', adapter)(source=source, uri=uri)
	except:
		raise ValueError(f"Load adapter \"{adapter}\" not found")


def translate(chain, t):
	if t.data == "extract":
		chain.addStep(handleExtract(t.children))
	elif t.data == "transform":
		chain.addStep(handleTransform(t.children))
	elif t.data == "load":
		chain.addStep(handleLoad(t.children))
	else:
		raise ValueError(f"Command \"{t.data}\" not valid")


def process(dsl_code: str):
	lark = Lark(util.read(f"{Path(__file__).parent}/grammar/etl.lark"))
	
	chain = engine.Chain()

	for instruction in lark.parse(dsl_code).children:
		translate(chain, instruction)

	chain.process()
	


if __name__ == "__main__":
	import sys
	from util import read
	
	if len(sys.argv) < 2:
		raise ValueError('No filename')
		
	process(read(sys.argv[1]))

