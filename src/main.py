# main.py

import sys
import argparse
from PySide6.QtWidgets import QApplication

from src.controllers.main_controller import MainController
from src.db.schema import initialize_database
from src.db.seed import seed_sessions
from src.db.database import SessionLocal
from src.db.entities.session import Session as WorkSession

def reset_database():
    db = SessionLocal()
    db.query(WorkSession).delete()
    db.commit()
    db.close()
    print("Base de données réinitialisée.")

def main():
    parser = argparse.ArgumentParser(description="Lumo - Tracker de concentration")
    parser.add_argument("--seed", action="store_true", help="Insérer des données de test dans la base")
    parser.add_argument("--reset", action="store_true", help="Supprimer toutes les données de la base")
    args = parser.parse_args()

    initialize_database()

    if args.reset:
        reset_database()

    if args.seed:
        seed_sessions(n_days=14)

    app = QApplication(sys.argv)
    controller = MainController()
    controller.main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
