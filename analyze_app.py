import re

# Lese beide Dateien
with open('C:/Users/DRKairport/dienstwunsch2/app.py', 'r', encoding='utf-8') as f:
    current_app = f.read()

with open('C:/Users/DRKairport/wunsch/app.py', 'r', encoding='utf-8') as f:
    wunsch_app = f.read()

# 1. Extrahiere ShiftRequestSnapshot Modell
snapshot_model_match = re.search(r'class ShiftRequestSnapshot\(db\.Model\):.*?(?=\nclass |\n@app\.route)', wunsch_app, re.DOTALL)
if snapshot_model_match:
    snapshot_model = snapshot_model_match.group(0).strip()
    print("Snapshot Model gefunden:")
    print(snapshot_model[:200])
else:
    print("Snapshot Model NICHT gefunden")

# 2. Finde Position zum Einfügen (nach ShiftNote und vor Message)
insert_pos_match = re.search(r'(class ShiftNote\(db\.Model\):.*?user = db\.relationship.*?\n)\n(class Message)', current_app, re.DOTALL)
if insert_pos_match:
    print(f"\nEinfügeposition gefunden bei: {insert_pos_match.start(2)}")
else:
    print("Einfügeposition NICHT gefunden")

# 3. Prüfe ob User.first_submission_at existiert
if 'first_submission_at' in current_app:
    print("\nUser.first_submission_at existiert bereits")
else:
    print("\nUser.first_submission_at muss hinzugefügt werden")

