from src.engine import Extract
import pandas
from pandas import DataFrame

class ExtractCsv(Extract):
	def __init__(self, *, uri):
		super().__init__(uri)

	@staticmethod
	def extract(uri) -> DataFrame:
		return pandas.read_csv(uri)


