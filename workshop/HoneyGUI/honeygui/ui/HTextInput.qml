import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Window 2.14


Item {
  id: _root
  width: 200; height: 30
  property color backgroundColor: "#414141"

  Rectangle {
    id: _container
    anchors.fill: parent
    color: _root.backgroundColor
    radius: 2
    border.color: "#414141"
    border.width: 1
    clip:true


    TextInput {
      id: input
      anchors {
        left: parent.left; leftMargin: 3; right: parent.right; rightMargin: 3;
        bottom: parent.bottom; bottomMargin: 8
      }
      color: "#efefef"
    }
  }
}