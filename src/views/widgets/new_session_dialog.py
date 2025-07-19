# src/views/widgets/new_session_dialog.py

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QDateTimeEdit,
    QSpinBox, QPushButton, QHBoxLayout
)
from PySide6.QtCore import QDateTime
from datetime import datetime

class NewSessionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nouvelle session")

        layout = QVBoxLayout()

        self.start_time_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.start_time_edit.setCalendarPopup(True)
        layout.addWidget(QLabel("Début :"))
        layout.addWidget(self.start_time_edit)

        self.end_time_edit = QDateTimeEdit(QDateTime.currentDateTime().addSecs(3600))
        self.end_time_edit.setCalendarPopup(True)
        layout.addWidget(QLabel("Fin :"))
        layout.addWidget(self.end_time_edit)

        self.break_spin = QSpinBox()
        self.break_spin.setSuffix(" min")
        self.break_spin.setRange(0, 120)
        layout.addWidget(QLabel("Pause :"))
        layout.addWidget(self.break_spin)

        buttons = QHBoxLayout()
        self.btn_ok = QPushButton("Ajouter")
        self.btn_cancel = QPushButton("Annuler")
        buttons.addWidget(self.btn_ok)
        buttons.addWidget(self.btn_cancel)
        layout.addLayout(buttons)

        self.setLayout(layout)

        self.btn_ok.clicked.connect(self.accept)
        self.btn_cancel.clicked.connect(self.reject)

    def get_data(self):
        return {
            "start_time": self.start_time_edit.dateTime().toPython(),
            "end_time": self.end_time_edit.dateTime().toPython(),
            "break_minutes": self.break_spin.value()
        }
