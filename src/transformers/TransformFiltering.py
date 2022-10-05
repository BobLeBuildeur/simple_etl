from src.engine import Chain, Step, Comparison
from src.util import normalize
from pandas import DataFrame

class TransformFiltering(Step):
	def __init__(self, source: str, label: str, comparison: str | Comparison, value: any):
		super().__init__()
		self.source = source
		self.label = label
		self.comparison = comparison
		self.value = value
	
	def process(self, chain: Chain):
		data_frame = chain.getDataFrame(self.source)
		chain.setDataFrame(self.source, TransformFiltering._filter(data_frame, self.label, self.comparison, self.value))
		
	@staticmethod
	def _filter(data_frame: DataFrame, label: str, comparison: str | Comparison, value) -> DataFrame:
		if type(comparison) == str: comparison = Comparison(comparison)
		
		value = normalize(value)
		
		if comparison == Comparison.EQ:
			return data_frame.loc[data_frame[label] == value]
		elif comparison == Comparison.NEQ:
			return data_frame.loc[data_frame[label] != value]
		elif comparison == Comparison.GT:
			return data_frame.loc[data_frame[label] > value]
		elif comparison == Comparison.LT:
			return data_frame.loc[data_frame[label] < value]
		elif comparison == Comparison.GTE:
			return data_frame.loc[data_frame[label] >= value]
		elif comparison == Comparison.LTE:
			return data_frame.loc[data_frame[label] <= value]
		else:
			raise ValueError(f"Comparison {comparison} not found")



