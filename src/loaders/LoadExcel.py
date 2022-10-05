from src.engine import Load, Chain


class LoadExcel(Load):
	def __init__(self, *, source: str, uri: str):
		super().__init__(source, uri)
	
	def process(self, chain: Chain):
		chain.getDataFrame(self.source).to_excel(self.uri, index=False)
