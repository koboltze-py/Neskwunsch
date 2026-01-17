"""
Startup-Skript für Render: Löscht alte DB und erstellt neue mit allen Spalten
"""
import os
import shutil

# Pfad zur SQLite DB
db_path = 'instance/dienstwunsch.db'

# Nur löschen wenn SQLite verwendet wird (nicht PostgreSQL)
database_url = os.environ.get('DATABASE_URL')
if not database_url or database_url.startswith('sqlite'):
    if os.path.exists(db_path):
        print(f"  Lösche alte Datenbank: {db_path}")
        os.remove(db_path)
        print(" Alte Datenbank gelöscht")
    
    if os.path.exists('instance'):
        print(" instance/ Verzeichnis existiert")
    else:
        os.makedirs('instance')
        print(" instance/ Verzeichnis erstellt")

# Starte die App
from app import app, init_db

print(" Initialisiere Datenbank...")
init_db()
print(" Datenbank initialisiert")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
