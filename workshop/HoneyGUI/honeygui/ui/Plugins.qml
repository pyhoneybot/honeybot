import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Window 2.14

Item {
  id: _root

  property Window window
  property alias drawer: _drawer


  Drawer {
    id: _drawer
    width: _root.window.width * 0.66
    height: _root.window.height
    edge: Qt.RightEdge
    modal: false
    interactive: _root.window.visibility !== Window.Windowed || position > 0
  }

  Component {
    id: _listdelg
    Rectangle {
      readonly property ListView __lv: ListView.view
      id: _rect
      width: parent.width; height: 32
      color: __lv.currentIndex == index ? Qt.darker("#414141"): "#424242"
      Text {
        anchors {
          left: parent.left; leftMargin: 8; verticalCenter: parent.verticalCenter
        }

        text: model.name
        color: __lv.currentIndex == index ? "#efefef": "#efefef"
        font.pixelSize: 12
      }
      Rectangle {
        id: _sep
        width: parent.width
        height: .5
        color: "#414141"
        anchors {
          bottom: parent.bottom; horizontalCenter: parent.horizontalCenter
        }
      }
      MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.LeftButton | Qt.RightButton
        onClicked: (mouse) => {
        if(mouse.button == Qt.RightButton)
        {
        __lv.currentIndex = index;
        // Open contextmenu for selected index
      }else if (mouse.button == Qt.LeftButton){
      __lv.currentIndex = index;
    }
  }

}
}

}

Rectangle {
  id: container_
  anchors.fill: parent
  color: "#212121"

  ListView {
    id: _lv
    width: 256; height: parent.height
    anchors.margins: 2
    anchors.left: parent.left
    model: __pModel
    delegate: _listdelg
    clip: true
    keyNavigationWraps: true

  }

  Rectangle {
    id: _cfgContainer
    height: parent.height
    anchors {
      right: parent.right; left: _lv.right; leftMargin: 2
    }
    color: "#212121"

    PluginConfig {
      id: _pConfig
      anchors.fill: parent
    }
  }

}

}