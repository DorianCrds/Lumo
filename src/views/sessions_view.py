# views/sessions_view.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout

from src.views.widgets.session_list_widget import SessionListWidget


class SessionsView(QWidget):
    def __init__(self):
        super().__init__()
        main_v_layout = QVBoxLayout()
        main_v_layout.addWidget(QLabel("Historique des sessions"))

        self.session_list_widget = SessionListWidget()

        self.new_session_button = QPushButton("+ Nouvelle session")

        self.delete_session_button = QPushButton("- Supprimer la session")

        buttons_v_layout = QVBoxLayout()
        buttons_v_layout.addWidget(self.new_session_button)
        buttons_v_layout.addWidget(self.delete_session_button)
        buttons_v_layout.addStretch()

        content_h_layout = QHBoxLayout()
        content_h_layout.addWidget(self.session_list_widget)
        content_h_layout.addLayout(buttons_v_layout)

        main_v_layout.addLayout(content_h_layout)

        self.setLayout(main_v_layout)
