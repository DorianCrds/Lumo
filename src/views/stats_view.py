# src/views/stats_view.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox, QHBoxLayout
from PySide6.QtCore import Signal

class StatsView(QWidget):
    period_changed = Signal(str)  # Signal émis quand l'utilisateur change la période

    def __init__(self):
        super().__init__()

        main_v_layout = QVBoxLayout()

        self.title_label = QLabel("Statistiques")
        main_v_layout.addWidget(self.title_label)

        self.period_selector = QComboBox()
        self.period_selector.addItems(["Toutes", "Semaine", "Mois"])
        self.period_selector.currentTextChanged.connect(self.on_period_changed)
        main_v_layout.addWidget(self.period_selector)

        content_h_layout = QHBoxLayout()

        self.days_worked_label = QLabel()
        self.total_time_label = QLabel()
        self.avg_per_day_label = QLabel()


        content_h_layout.addWidget(self.days_worked_label)
        content_h_layout.addWidget(self.total_time_label)
        content_h_layout.addWidget(self.avg_per_day_label)

        main_v_layout.addLayout(content_h_layout)
        main_v_layout.addStretch()

        self.setLayout(main_v_layout)

    def update_stats(self, stats: dict):
        self.days_worked_label.setText(f"Jours travaillés : {stats['days_worked']}")
        self.total_time_label.setText(f"Temps total travaillé : {stats['total_worked_time_str']}")
        self.avg_per_day_label.setText(f"Moyenne par jour : {stats['average_per_day_str']}")

    def on_period_changed(self, value: str):
        self.period_changed.emit(value.lower())  # envoie le filtre à MainController
