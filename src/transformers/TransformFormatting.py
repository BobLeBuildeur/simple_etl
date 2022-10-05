from src.engine import Chain, Step

def checkbox_formatter(element: str | int | float) -> bool:
	true = ['true', 't', 'yes', 'y', 'x']
	value = str(element).strip().lower()
	return value in true


def lower_string_formatter(element: any) -> any:
	if type(element) != str: return element
	return element.lower()


def upper_string_formatter(element: any) -> any:
	if type(element) != str: return element
	return element.upper()
	

def trim_string_formatter(element: any, left=0, right=0) -> any:
	if type(element) != str: return element
	return element[int(left):len(element) - int(right)]


def slice_string_formatter(element: any, start=0, end=0) -> any:
	if type(element) != str: return element
	return element[int(start):int(end)]


formatters = {
	"checkbox": checkbox_formatter,
	"trim": trim_string_formatter,
	"slice": slice_string_formatter,
	"upper": upper_string_formatter,
	"lower": lower_string_formatter
}


class TransformFormatting(Step):
	def __init__(self, source: str, label: str, formatter, *args):
		super().__init__()
		self.source = source
		self.label = label
		self.formatter = formatters[formatter]
		self.args = args
	
	def process(self, chain: Chain):
		data_frame = chain.get_data_frame(self.source)
		data_frame[self.label] = data_frame[self.label].apply(lambda v: self.formatter(v, *self.args))
		


