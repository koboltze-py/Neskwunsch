"""
Migrations-Skript: Konvertiere alte Schichttypen zu neuen
Früh → T (Tagdienst)
Spät → T10 (Tagdienst 10h)
Nacht → N10 (Nachtdienst 10h)
"""
from app import app, db, ShiftRequest

def migrate_shift_types():
    with app.app_context():
        # Mapping
        mapping = {
            'Früh': 'T',
            'Spät': 'T10',
            'Nacht': 'N10'
        }
        
        # Hole alle Shift Requests
        all_shifts = ShiftRequest.query.all()
        
        updated_count = 0
        for shift in all_shifts:
            if shift.shift_type in mapping:
                old_type = shift.shift_type
                new_type = mapping[old_type]
                shift.shift_type = new_type
                print(f"  {shift.user.name}: {old_type} → {new_type} ({shift.date})")
                updated_count += 1
        
        db.session.commit()
        print(f"\n✅ {updated_count} Einträge aktualisiert!")
        print(f"   Gesamt: {len(all_shifts)} Dienstwünsche in der Datenbank")

if __name__ == '__main__':
    print("🔄 Starte Migration der Schichttypen...\n")
    migrate_shift_types()
    print("\n✅ Migration abgeschlossen!")
