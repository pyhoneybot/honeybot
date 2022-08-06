import os
import sys
from pathlib import Path

from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType

from workshop.HoneyGUI.honeygui.src.plugin import Plugin
from workshop.HoneyGUI.honeygui.src.pluginlist import PluginListModel

ROOT_DIR = Path(__file__).resolve().parent.parent


def main():

    QCoreApplication.setOrganizationName('pyhoneybot')
    QCoreApplication.setOrganizationDomain('org.honeybot.pyhoneybot')
    QCoreApplication.setApplicationName('HoneyGUI')

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    _pModel = PluginListModel()
    _plugin = Plugin()

    qmlRegisterType(Plugin, "org.honeybot.phoneybot", 1,0, "Plugin")
    
    engine.rootContext().setContextProperty('__pModel', _pModel)
    engine.rootContext().setContextProperty('__plugin', _plugin)



    engine.load(os.fspath( ROOT_DIR  / 'ui/HoneyGui.qml'))


    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
