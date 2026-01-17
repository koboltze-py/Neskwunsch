import re
import shutil

# Backup erstellen
shutil.copy('app.py', 'app.py.before_update')

# Lese beide Dateien
with open('app.py', 'r', encoding='utf-8') as f:
    current_app = f.read()

with open('C:/Users/DRKairport/wunsch/app.py', 'r', encoding='utf-8') as f:
    wunsch_app = f.read()

print("=== Feature-Integration gestartet ===\n")

# 1. Füge ShiftRequestSnapshot Modell hinzu
snapshot_model = """
class ShiftRequestSnapshot(db.Model):
    \"\"\"Speichert ursprüngliche Dienstwünsche beim ersten Speichern\"\"\"
    __tablename__ = 'shift_request_snapshots'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    shift_type = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    user = db.relationship('User')
"""

# Finde Position (nach ShiftNote, vor Message)
insert_pattern = r'(class ShiftNote\(db\.Model\):.*?user = db\.relationship.*?\n)(\nclass Message)'
current_app = re.sub(insert_pattern, r'\1' + snapshot_model + r'\2', current_app, flags=re.DOTALL)
print(" ShiftRequestSnapshot Modell hinzugefügt")

# 2. Extrahiere und füge Batch-Route hinzu
batch_route_match = re.search(
    r"@app\.route\('/api/shift-requests/batch'.*?(?=\n@app\.route|\nif __name__)",
    wunsch_app,
    re.DOTALL
)
if batch_route_match:
    batch_route = batch_route_match.group(0)
    # Füge vor dem letzten @app.route ein
    last_route_pattern = r"(@app\.route\('/api/shift-requests/<request_id>', methods=\['DELETE'\]\).*?return jsonify.*?\n)"
    current_app = re.sub(last_route_pattern, r'\1\n' + batch_route + '\n', current_app, flags=re.DOTALL)
    print(" Batch-Route hinzugefügt")

# 3. Extrahiere und füge Snapshot-Ansicht Route hinzu
snapshot_route_match = re.search(
    r"@app\.route\('/api/admin/users/<int:user_id>/snapshots'.*?(?=\n@app\.route)",
    wunsch_app,
    re.DOTALL
)
if snapshot_route_match:
    snapshot_route = snapshot_route_match.group(0)
    # Füge nach confirm-all-shifts Route ein
    confirm_all_pattern = r"(@app\.route\('/api/admin/users/<int:user_id>/confirm-all-shifts'.*?return jsonify.*?\n)"
    current_app = re.sub(confirm_all_pattern, r'\1\n' + snapshot_route + '\n', current_app, flags=re.DOTALL)
    print(" Snapshot-Ansicht Route hinzugefügt")

# Speichere aktualisierte Datei
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(current_app)

print("\n=== Integration abgeschlossen ===")
print("Backup gespeichert als: app.py.before_update")
