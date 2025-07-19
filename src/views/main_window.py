# views/main_window.py

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QStackedWidget
)
from src.views.sessions_view import SessionsView
from src.views.stats_view import StatsView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lumo")
        self.setMinimumSize(800, 650)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Menu vertical (à gauche)
        self.menu_layout = QVBoxLayout()
        self.button_sessions = QPushButton("Sessions")
        self.button_stats = QPushButton("Statistiques")

        self.menu_layout.addWidget(self.button_sessions)
        self.menu_layout.addWidget(self.button_stats)
        self.menu_layout.addStretch()  # pousse les boutons en haut

        # Zone de contenu (QStackedWidget)
        self.stack = QStackedWidget()
        self.sessions_view = SessionsView()
        self.stats_view = StatsView()

        self.stack.addWidget(self.sessions_view)  # index 0
        self.stack.addWidget(self.stats_view)     # index 1

        # Ajout au layout principal
        menu_widget = QWidget()
        menu_widget.setLayout(self.menu_layout)
        main_layout.addWidget(menu_widget)
        main_layout.addWidget(self.stack, stretch=1)

        # Connexion des boutons
        self.button_sessions.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.button_stats.clicked.connect(lambda: self.stack.setCurrentIndex(1))
