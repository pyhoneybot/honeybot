import os
import sys
from pathlib import Path

from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


ROOT_DIR = Path(__file__).resolve().parent.parent


def main():

    QCoreApplication.setOrganizationName('')
    QCoreApplication.setOrganizationDomain('')
    QCoreApplication.setApplicationName('HoneyGUI')


    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.fspath( ROOT_DIR  / 'ui/HoneyGui.qml'))


    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
