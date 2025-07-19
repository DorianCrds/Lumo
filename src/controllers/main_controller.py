# controllers/main_controller.py
from PySide6.QtWidgets import QListWidgetItem, QMessageBox
from src.views.main_window import MainWindow
from src.db.schema import initialize_database
from src.models.session_model import SessionModel
from src.views.widgets.new_session_dialog import NewSessionDialog

class MainController:
    def __init__(self):
        initialize_database()
        self.session_model = SessionModel()
        self.main_window = MainWindow()
        self.main_window.sessions_view.new_session_button.clicked.connect(self.show_new_session_dialog)
        self.main_window.sessions_view.delete_session_button.clicked.connect(self.delete_selected_session)
        self.main_window.stats_view.period_changed.connect(self.refresh_stats)
        self.refresh()

    def refresh(self):
        # Rafraîchir la liste des sessions
        self.main_window.sessions_view.session_list_widget.list_widget.clear()
        sessions = self.session_model.get_all_sessions()
        for session in sessions:
            item_text = (
                f"{session['start_time'].strftime('%Y-%m-%d %H:%M')} → "
                f"{session['end_time'].strftime('%H:%M')}  |  "
                f"Durée : {session['duration_str']}"
            )
            item = QListWidgetItem(item_text)
            item.setData(0x0100, session["id"])  # Qt.UserRole
            self.main_window.sessions_view.session_list_widget.list_widget.addItem(item)

        self.refresh_stats("toutes")

    def show_new_session_dialog(self):
        dialog = NewSessionDialog()
        if dialog.exec():
            data = dialog.get_data()
            self.session_model.add_session(
                start_time=data["start_time"],
                end_time=data["end_time"],
                break_minutes=data["break_minutes"]
            )
            self.refresh()

    def delete_selected_session(self):
        list_widget = self.main_window.sessions_view.session_list_widget.list_widget
        selected_items = list_widget.selectedItems()

        if not selected_items:
            QMessageBox.information(self.main_window, "Aucune sélection",
                                    "Veuillez sélectionner une session à supprimer.")
            return

        item = selected_items[0]
        session_id = item.data(0x0100)

        confirm = QMessageBox.question(
            self.main_window,
            "Confirmation",
            "Supprimer cette session ?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            self.session_model.delete_session(session_id)
            self.refresh()

    def refresh_stats(self, period: str = "toutes"):
        stats = self.session_model.get_stats(period=period)
        self.main_window.stats_view.update_stats(stats)
