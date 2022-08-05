from PySide6.QtCore import QObject, Signal, Property
from typing import List

class Plugin(QObject):

    nameChanged = Signal(str, name='nameChanged')
    portChanged = Signal(int, name='portChanged')
    serverUrlChanged = Signal(str, name='serverUrlChanged')
    channelsChanged = Signal(List[str], name='channelsChanged')
    emailChanged = Signal(str, name='emailChanged')
    passwordChanged = Signal(str, name='passwordChanged')

    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)

        self.name_ : str = ""
        self.port_ : int = 0
        self.serverUrl_ = ""
        self.channels_ : List[str]
        self.email_: str = ""
        self.password_: str = ""
        self.smtpSever: str = ""
        self.smtpPort_: int = 0


    def getName(self):
        return self.name_

    def setName(self, name):
        self.name_ = name
        self.nameChanged.emit(self.name_)

    def getPort(self):
        return self.port_
    
    def setPort(self, port):
        self.port_ = port
        self.portChanged.emit(self.port_)
    

    name = Property(str, getName, setName, notify=nameChanged)
    port = Property(int, getPort, setPort, notify=portChanged)
    serverUrl = Property(str, getServerUrl, setServerUrl, notify=serverUrlChanged)
    email = Property(str, getEmail, setEmail, notify=emailChanged)
    password = Property(str, getPassword, setPassword, notify=passwordChanged)
    channels = Property(List[str], getChannels, setChannels, notify=channelsChanged)
