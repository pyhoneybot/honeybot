import QtQuick 2.14
import QtQuick.Window 2.14
import Qt.labs.settings 1.0


Window {
  id: mainwindow
  width: 640
  height: 420
  visible: true
  color: "#212121"

  Rectangle{
    id: _header
    width: parent.width
    height: 30
    color: "#212121"
    Text {
      text: "Plugins"
      color: "#efefef"
      font.pixelSize: 18
      font.weight: Font.DemiBold
      anchors {
        verticalCenter: parent.verticalCenter; left: parent.left; leftMargin: 8
      }
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
  }

  Plugins{
    id: _plugins
    anchors {
      top: _header.bottom; bottom: parent.bottom; left: parent.left; right: parent.right
    }
    window: mainwindow
  }







  Settings {
    id: mainSettings
    property alias x: mainwindow.x
    property alias y: mainwindow.y
    property alias width: mainwindow.width
    property alias height: mainwindow.height }




  }