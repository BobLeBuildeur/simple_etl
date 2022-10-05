from abc import abstractmethod
from enum import Enum
import pandas
from pandas import DataFrame
from src import util


class Comparison(Enum):
	GT 	= ">"
	LT 	= "<"
	GTE 	= ">="
	LTE 	= "<="
	EQ 	= "="
	NEQ	= "<>"


class Chain:
	def __init__(self):
		self.dataFrames = {}
		self.steps = []
		
	def getDataFrame(self, key: str): 
		return self.dataFrames[key]
		
	def setDataFrame(self, key: str, data: DataFrame):
		self.dataFrames[key] = data

	def addStep(self, step):
		self.steps.append(step)
	
	def process(self):
		for step in self.steps: 	
			step.process(self)


class Step:
	@abstractmethod
	def process(self, chain: Chain):
		pass


class Extract(Step):
	def __init__(self, uri, name=False):
		super().__init__()
		self.uri = uri
		self.name = name or uri
	
	def process(self, chain: Chain):
		data = self.extract(self.uri)
		chain.setDataFrame(self.uri, data)

	@staticmethod
	@abstractmethod
	def extract(uri) -> DataFrame:
		pass	


class Load:
	def __init__(self, source, uri):
		super().__init__()
		self.source = source
		self.uri = uri
	
	@abstractmethod
	def process(self, chain: Chain):
		pass





