import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts

ApplicationWindow {
	visible: true
	width: 600
	height: 500
	title: "ETL"


	header: ToolBar {
		Material.theme: Material.Dark
		
		RowLayout {
			anchors.fill: parent
			ToolButton {
				text: "Run"
				onClicked: {
					AppController.process(dslModel.text)
					statusModel.text = AppController.status()
				}
			}
			Label {
				id: statusModel
				text: AppController.status()
			}
		}
	}

	TextArea {
		id: dslModel
		anchors.fill: parent
	}

}

