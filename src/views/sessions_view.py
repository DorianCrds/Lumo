# views/sessions_view.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

from src.views.widgets.session_list_widget import SessionListWidget


class SessionsView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Vue des sessions"))

        self.new_session_button = QPushButton("+ Nouvelle session")
        layout.addWidget(self.new_session_button)

        self.delete_session_button = QPushButton("- Supprimer la session")
        layout.addWidget(self.delete_session_button)

        self.session_list_widget = SessionListWidget()
        layout.addWidget(self.session_list_widget)
        self.setLayout(layout)
