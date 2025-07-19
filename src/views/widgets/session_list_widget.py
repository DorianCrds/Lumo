# src/views/session_list_widget.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from PySide6.QtCore import Qt

class SessionListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title = QLabel("Sessions récentes")
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)