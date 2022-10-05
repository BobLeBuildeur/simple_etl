from src.engine import Load, Chain


class LoadCsv(Load):
	def __init__(self, *, source: str, uri: str):
		super().__init__(source, uri)
	
	def process(self, chain: Chain):
		chain.getDataFrame(self.source).to_csv(self.uri, index=False)

