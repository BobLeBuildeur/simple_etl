from src.engine import Chain, Step


class TransformFiltering(Step):
	def __init__(self, source: str, *labels):
		super().__init__()
		self.source = source
		self.labels = labels
	
	def process(self, chain: Chain):
		data_frame = chain.get_data_frame(self.source)
		chain.set_data_frame(self.source, data_frame.drop(labels=self.labels, axis=1))
		


