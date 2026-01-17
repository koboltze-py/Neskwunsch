"""
Migrations-Skript: Füge first_submission_at Spalte zur users Tabelle hinzu
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Datenbank-Konfiguration (wie in app.py)
database_url = os.environ.get('DATABASE_URL')
if database_url:
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/dienstwunsch.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def migrate():
    with app.app_context():
        # SQL-Befehle für verschiedene Datenbanken
        try:
            # Prüfe ob die Spalte bereits existiert
            result = db.session.execute(db.text("SELECT first_submission_at FROM users LIMIT 1"))
            print(" Spalte first_submission_at existiert bereits")
        except Exception as e:
            # Spalte existiert nicht, füge sie hinzu
            print("Füge Spalte first_submission_at hinzu...")
            
            # Für PostgreSQL und SQLite
            try:
                db.session.execute(db.text("ALTER TABLE users ADD COLUMN first_submission_at TIMESTAMP"))
                db.session.commit()
                print(" Spalte first_submission_at erfolgreich hinzugefügt")
            except Exception as alter_error:
                print(f" Fehler beim Hinzufügen der Spalte: {alter_error}")
                db.session.rollback()

if __name__ == '__main__':
    migrate()
