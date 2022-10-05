from src.engine import Chain, Step

def checkboxFormatter(element: str | int | float) -> bool:
	true = ['true', 't', 'yes', 'y', 'x']
	value = str(element).strip().lower()
	return value in true


def lowerStringFormatter(element: any) -> any:
	if type(element) != str: return element
	return element.lower()


def upperStringFormatter(element: any) -> any:
	if type(element) != str: return element
	return element.upper()
	

def trimStringFormatter(element: any, left=0, right=0) -> any:
	if type(element) != str: return element
	return element[int(left):len(element) - int(right)]


def sliceStringFormatter(element: any, start=0, end=0) -> any:
	if type(element) != str: return element
	return element[int(start):int(end)]


formatters = {
	"checkbox": checkboxFormatter,
	"trim": trimStringFormatter,
	"slice": sliceStringFormatter,
	"upper": upperStringFormatter,
	"lower": lowerStringFormatter
}


class TransformFormatting(Step):
	def __init__(self, source: str, label: str, formatter, *args):
		super().__init__()
		self.source = source
		self.label = label
		self.formatter = formatters[formatter]
		self.args = args
	
	def process(self, chain: Chain):
		data_frame = chain.getDataFrame(self.source)
		data_frame[self.label] = data_frame[self.label].apply(lambda v: self.formatter(v, *self.args))
		


