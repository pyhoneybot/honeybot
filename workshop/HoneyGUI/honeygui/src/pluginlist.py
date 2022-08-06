from PySide6.QtCore import (
    QObject,
    Signal,
    Property,
    QAbstractListModel,
    Qt,
    QModelIndex,
    QByteArray,
)

from .plugin import Plugin
from typing import List



class PluginListModel(QAbstractListModel):

    NameRole = Qt.UserRole + 1

    def __init__(self, parent: QAbstractListModel = None) -> None:
        super().__init__(parent)

        self._data: List[Plugin] = []

    def rowCount(self, parent: QModelIndex) -> int:
        return len(self._data)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> str:
        if not index.isValid():
            return None
        elif index.row() >= len(self._data):
            return None
        elif role == PluginListModel.NameRole:
            return self._data[index.row()]
        else:
            return None

    def roleNames(self):
        roles = {
            PluginListModel.NameRole: QByteArray(b"name"),
        }
        return roles

