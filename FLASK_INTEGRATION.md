# DRK Dienstwünsche - Anleitung

## ✅ Systemarchitektur

Diese Anwendung nutzt:
- **Backend**: Flask (Python) mit SQLAlchemy
- **Frontend**: React (TypeScript) mit Vite
- **Datenbank**: PostgreSQL (Produktion) / SQLite (Entwicklung)

## 🚀 Schnellstart (Entwicklung)

### 1. Backend (Flask) starten

```powershell
# Python-Umgebung aktivieren (falls vorhanden)
# .\venv\Scripts\Activate.ps1

# Abhängigkeiten installieren
pip install -r requirements.txt

# Flask-Server starten
python app.py
```

Der Flask-Server läuft auf: **http://localhost:5000**

### 2. Frontend (React) starten

**Neues Terminal öffnen:**

```powershell
# Node-Module installieren (einmalig)
npm install

# Entwicklungsserver starten
npm run dev
```

Das React-Frontend läuft auf: **http://localhost:5173**

## 📋 Standardbenutzer

Nach dem ersten Start wird automatisch ein Admin-Benutzer erstellt:
- **Name**: Groß
- **Passwort**: mettwurst

## 🔗 Service-Verbindungen

### API-Endpunkte (Flask Backend)

| Endpunkt | Methode | Beschreibung |
|----------|---------|--------------|
| `/login` | POST | Login/Registrierung |
| `/logout` | GET | Abmelden |
| `/api/shift-requests` | GET | Eigene Dienstwünsche abrufen |
| `/api/shift-requests` | POST | Neuen Dienstwunsch erstellen |
| `/api/shift-requests/<id>` | DELETE | Dienstwunsch löschen |
| `/admin` | GET | Admin-Dashboard |

### React → Flask Kommunikation

Das React-Frontend kommuniziert mit dem Flask-Backend über:
- **Datei**: `src/services/api.ts`
- **Methode**: `fetch()` mit `credentials: 'include'` für Session-Cookies
- **Base-URL**: `http://localhost:5000` (Entwicklung)

#### Beispiel API-Call:

```typescript
// Dienstwunsch erstellen
import * as api from './services/api';

const result = await api.createShiftRequest({
  date: new Date('2026-01-20'),
  shiftType: 'Früh',
  remarks: 'Bitte berücksichtigen'
});

if (result.success) {
  console.log('Erfolgreich!', result.data);
}
```

## 🏗️ Projektstruktur

```
├── app.py                      # Flask Backend
├── requirements.txt            # Python Dependencies
├── src/
│   ├── App.tsx                # React Hauptkomponente mit Auth
│   ├── services/
│   │   └── api.ts            # ✅ Flask API Service Layer
│   ├── components/
│   │   ├── Login.tsx         # ✅ Login mit Flask Auth
│   │   └── ShiftRequestForm.tsx  # ✅ Nutzt Flask API
│   └── types/
│       └── shift.ts          # TypeScript Typen
├── templates/                  # Flask HTML Templates (für Admin)
│   ├── login.html
│   ├── admin_dashboard.html
│   └── shift_request_form.html
└── instance/                   # SQLite Datenbank (lokal)
```

## 🔧 Konfiguration

### Backend (.env für Flask)

```bash
DATABASE_URL=postgresql://user:password@host:port/database
SECRET_KEY=ihr-geheimer-schluessel
```

### Frontend (.env.local für Vite)

```bash
VITE_API_URL=http://localhost:5000
```

## 🌐 Deployment (Render)

### Backend (Flask)

1. Render.com → New Web Service
2. Repository verbinden
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app:app`
5. Environment Variables:
   - `DATABASE_URL` (wird automatisch gesetzt)
   - `PYTHON_VERSION=3.11`

### Frontend (React)

Zwei Optionen:

#### Option A: Statische Seite auf Render

1. Render.com → New Static Site
2. Build Command: `npm install && npm run build`
3. Publish Directory: `dist`
4. Environment Variable:
   - `VITE_API_URL=https://ihr-backend.onrender.com`

#### Option B: Flask serviert React (empfohlen)

```python
# In app.py hinzufügen:
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path and os.path.exists(os.path.join('dist', path)):
        return send_from_directory('dist', path)
    return send_from_directory('dist', 'index.html')
```

Build React: `npm run build`  
→ Kopiert `dist/` Ordner zum Flask-Projekt

## 🧪 Testen der Verbindung

### Test 1: Backend läuft

```powershell
# In PowerShell:
Invoke-RestMethod -Uri http://localhost:5000/login -Method GET
```

### Test 2: API-Call

```powershell
# Login
$body = @{
    name = "TestUser"
    password = "test123"
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:5000/login -Method POST -Body $body -ContentType "application/json" -SessionVariable session

# Dienstwünsche abrufen
Invoke-RestMethod -Uri http://localhost:5000/api/shift-requests -WebSession $session
```

## ❓ Troubleshooting

### Problem: CORS-Fehler

**Lösung**: Flask CORS aktivieren

```python
# In app.py
from flask_cors import CORS
CORS(app, supports_credentials=True, origins=['http://localhost:5173'])
```

```bash
pip install flask-cors
```

### Problem: Session funktioniert nicht

**Ursache**: Cookies zwischen localhost:5173 und localhost:5000

**Lösung**: Proxy in `vite.config.ts`:

```typescript
export default {
  server: {
    proxy: {
      '/api': 'http://localhost:5000',
      '/login': 'http://localhost:5000',
      '/logout': 'http://localhost:5000',
    }
  }
}
```

Dann API-Base-URL ändern zu: `''` (leer = gleiche Origin)

## 📝 Weitere Befehle

```powershell
# Backend-Datenbank zurücksetzen
Remove-Item .\instance\dienstwuensche.db
python app.py

# Frontend neu bauen
npm run build

# TypeScript prüfen
npm run lint

# Dependencies aktualisieren
pip install --upgrade -r requirements.txt
npm update
```

## 🎯 Nächste Schritte

- [ ] CORS richtig konfigurieren
- [ ] Vite Proxy einrichten (optional)
- [ ] Admin-Dashboard in React erstellen
- [ ] Tests schreiben
- [ ] Deployment durchführen

---

**Erstellt für**: DRK Köln e.V. - Erste-Hilfe-Station Flughafen  
**Datum**: Januar 2026
