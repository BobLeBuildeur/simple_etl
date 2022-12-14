from src.engine import Chain, Step

class TransformMatching(Step):
	def __init__(self, source_a: str, source_b: str, label: str):
		super().__init__()
		self.source_a = source_a
		self.source_b = source_b
		self.label = label
	
	def process(self, chain: Chain):
		df_a = chain.get_data_frame(self.source_a)
		df_b = chain.get_data_frame(self.source_b)
		chain.set_data_frame(self.source_a, df_a.merge(df_b, on=self.label))

