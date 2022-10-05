import sys
import os
from pathlib import Path
from PyQt6.QtCore import QObject
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from src.parser import process


class AppController(QObject):

	def __init__(self):
		super().__init__()
		self.status = "Idle"

	@pyqtSlot(str)
	def process(self, dsl_code):
		self.status = "Processing..."
		try:
			process(dsl_code)
			self.status="Done"
		except BaseException as err:
			self.status = str(err)[0:30] + "..."
			print(str(err))
	
	@pyqtSlot(result=str)
	def status(self):
		return self.status


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

app_controller = AppController()

engine.rootContext().setContextProperty("AppController", app_controller)

engine.quit.connect(app.quit)

engine.load(f"{Path(__file__).parent}/UI/main.qml")

sys.exit(app.exec())
