import QtQuick 2.14
import QtQuick.Window 2.14
import Qt.labs.settings 1.0


Window {
  id: mainwindow
  width: 640
  height: 420
  visible: true
  color: "#212121"









  Settings {
    id: mainSettings
    property alias x: mainwindow.x
    property alias y: mainwindow.y
    property alias width: mainwindow.width
    property alias height: mainwindow.height }




}