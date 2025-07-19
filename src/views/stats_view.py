# src/views/stats_view.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox
from PySide6.QtCore import Signal

class StatsView(QWidget):
    period_changed = Signal(str)  # Signal émis quand l'utilisateur change la période

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title_label = QLabel("Statistiques")
        self.period_selector = QComboBox()
        self.period_selector.addItems(["Toutes", "Semaine", "Mois"])
        self.period_selector.currentTextChanged.connect(self.on_period_changed)

        self.days_worked_label = QLabel()
        self.total_time_label = QLabel()
        self.avg_per_day_label = QLabel()

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.period_selector)
        self.layout.addWidget(self.days_worked_label)
        self.layout.addWidget(self.total_time_label)
        self.layout.addWidget(self.avg_per_day_label)

    def update_stats(self, stats: dict):
        self.days_worked_label.setText(f"Jours travaillés : {stats['days_worked']}")
        self.total_time_label.setText(f"Temps total travaillé : {stats['total_worked_time_str']}")
        self.avg_per_day_label.setText(f"Moyenne par jour : {stats['average_per_day_str']}")

    def on_period_changed(self, value: str):
        self.period_changed.emit(value.lower())  # envoie le filtre à MainController
