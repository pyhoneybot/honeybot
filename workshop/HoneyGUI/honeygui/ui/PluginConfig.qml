import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Window 2.14
import QtQuick.Layouts 1.14



Item {
  id: _root



  Rectangle {
    id: _top
    color: "#212121"
    width: parent.width; height: 50
    anchors {
      top: parent.top; left: parent.left; right: parent.right
    }

    Text {
      id: _title
      text: qsTr("Configuration")
      color: "#efefef"
      font.pixelSize: 28
      anchors {
        left: parent.left; leftMargin: 8; bottom: parent.bottom; bottomMargin: 8
      }
    }

  }

  // TODO: Make container scrollable
  Rectangle {
    id: _container
    width: 600; height: parent.height
    clip: true
    anchors {
      left: parent.left; top: _top.bottom
    }
    color: "#212121"

    RowLayout {
      id: _row0
      anchors {
        left: parent.left; leftMargin: 8; top: _container.top; topMargin: 4
      }
      Text {
        id: _botNameLbl
        text: "Bot Name"
        color: "#efefef"
      }

      HTextInput {
        id: _botName
      }
    }


    GridLayout {
      id: _grid0
      rows: 2; columns: 2
      anchors {
        top: _row0.bottom; topMargin: 12; left: parent.left; leftMargin: 8
      }
      columnSpacing: 14

      Text {
        id: _serverUrlLbl
        text: qsTr("Server Url")
        color: "#efefef"
      }

      Text {
        id: _portLbl
        text: qsTr("Port")
        color: "#efefef"
      }

      HTextInput {
        id: _serverUrl
      }

      HTextInput {
        id: _port
        width: 100
      }

    }


    GridLayout {
      id: _row2
      rows: 3; columns: 2
      columnSpacing: 10
      rowSpacing: 8
      anchors {
        top: _grid0.bottom; topMargin: 12; left: parent.left; leftMargin: 8
      }

      Text {
        id: _channelsLbl
        text: qsTr("Channels")
        color: "#efefef"
        Layout.topMargin: 5
      }

      HTextInput {
        id: _channels
        width: 450
        Layout.alignment: Qt.AlignRight
      }

      Text {
        id: _emailLbl
        text: qsTr("Email")
        color: "#efefef"
        Layout.topMargin: 5
      }

      HTextInput {
        id: _email
        width: 230
        Layout.alignment: Qt.AlignLeft
      }

      Text {
        id: _emailPswdLbl
        text: qsTr("Password")
        color: "#efefef"
        Layout.topMargin: 5
      }

      HTextInput {
        id: _emailPassword
        Layout.alignment: Qt.AlignLeft
      }
    }


    Rectangle {
      id: _row3
      width: 500; height: 50
      color: "transparent"
      anchors {
        left: parent.left; leftMargin: 8; top: _row2.bottom; topMargin: 30
      }
      Text {
        id: _smtpServerLbl
        text: qsTr("SMTP Server")
        color: "#efefef"
        anchors.left: parent.left
        y: 5
      }
      HTextInput {
        id: _smtpServer
        anchors.left: _smtpServerLbl.right
        anchors.leftMargin: 10
      }

      Text {
        id: _smtpPortLbl
        y: 5
        text: qsTr("SMTP Port")
        color: "#efefef"
        anchors.left: _smtpServer.right
        anchors.leftMargin: 10
      }

      HTextInput {
        id: _smtpPort
        width: 100
        anchors.left: _smtpPortLbl.right
        anchors.leftMargin: 10
      }
    }

    Rectangle {
      id: _button
      width: 120; height: 30
      color: "#414141"
      radius: 4
      anchors {
        left: parent.left; leftMargin: 16; top: _row3.bottom; topMargin: 100
      }

      Text {
        text: qsTr("Save")
        color: "#efefef"
        anchors.centerIn: parent
      }

      MouseArea {
        id: _mouseArea
        anchors.fill: parent
      }
    }
  }
}