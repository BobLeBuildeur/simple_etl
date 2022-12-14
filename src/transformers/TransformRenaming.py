from src.engine import Chain, Step

class TransformRenaming(Step):
	def __init__(self, source: str, old_label: str, new_label: str):
		self.source = source
		self.old_label = old_label
		self.new_label = new_label
	
	def process(self, chain: Chain):
		data_frame = chain.get_data_frame(self.source)
		columns = {self.old_label: self.new_label}
		chain.set_data_frame(self.source, data_frame.rename(columns=columns))
