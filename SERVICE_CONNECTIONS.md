# ✅ Service-Verbindungen - Zusammenfassung

## Was wurde geändert?

### 1. ✅ API Service erstellt (`src/services/api.ts`)
- Zentrale Stelle für alle Flask API-Aufrufe
- Funktionen: `login()`, `logout()`, `createShiftRequest()`, `getUserShiftRequests()`, `deleteShiftRequest()`
- Nutzt `fetch()` mit `credentials: 'include'` für Session-Cookies
- Automatische Fehlerbehandlung

### 2. ✅ React Components an Flask angebunden

#### `ShiftRequestForm.tsx`
- ❌ Alt: `import { createShiftRequest } from '../actions/shift-request'` (Next.js Server Actions)
- ✅ Neu: `import * as api from '../services/api'` (Flask API)
- Alle API-Calls nutzen jetzt Flask Backend

#### `Login.tsx` (NEU)
- Vollständige Login-Komponente mit Flask-Integration
- Auto-Registrierung neuer Benutzer
- Admin-Weiterleitung

#### `App.tsx`
- Auth-State-Management hinzugefügt
- Login/Logout Flow implementiert
- Automatische Session-Prüfung

### 3. ✅ Flask CORS aktiviert (`app.py`)
- `flask-cors` installiert
- CORS für `localhost:5173` aktiviert
- Credentials-Support für Sessions

### 4. ✅ Vite Proxy konfiguriert (`vite.config.ts`)
- Proxy für `/api`, `/login`, `/logout`
- Vereinfacht API-Calls (optional)

### 5. ✅ Environment Variables
- `.env.local`: Entwicklung (`http://localhost:5000`)
- `.env.production`: Produktion (Render URL)

## 🔗 Verbindungsfluss

```
┌─────────────────────────────────────────────────────────┐
│  React Frontend (http://localhost:5173)                 │
│  ┌──────────────────────────────────────┐               │
│  │ App.tsx                              │               │
│  │ - Auth State Management              │               │
│  │ - Login/Logout Handling              │               │
│  └──────────────┬───────────────────────┘               │
│                 │                                        │
│  ┌──────────────▼───────────────────────┐               │
│  │ Login.tsx / ShiftRequestForm.tsx     │               │
│  │ - User Input                         │               │
│  │ - Form Validation                    │               │
│  └──────────────┬───────────────────────┘               │
│                 │                                        │
│  ┌──────────────▼───────────────────────┐               │
│  │ services/api.ts                      │               │
│  │ - API Call Functions                 │               │
│  │ - Error Handling                     │               │
│  │ - Session Management                 │               │
│  └──────────────┬───────────────────────┘               │
└─────────────────┼───────────────────────────────────────┘
                  │
                  │ HTTP Request (fetch)
                  │ credentials: 'include'
                  │
┌─────────────────▼───────────────────────────────────────┐
│  Flask Backend (http://localhost:5000)                  │
│  ┌──────────────────────────────────────┐               │
│  │ app.py                               │               │
│  │ - CORS aktiviert                     │               │
│  │ - Session Management                 │               │
│  └──────────────┬───────────────────────┘               │
│                 │                                        │
│  ┌──────────────▼───────────────────────┐               │
│  │ Routes/Endpoints                     │               │
│  │ POST /login                          │               │
│  │ GET  /logout                         │               │
│  │ GET  /api/shift-requests             │               │
│  │ POST /api/shift-requests             │               │
│  │ DELETE /api/shift-requests/<id>      │               │
│  └──────────────┬───────────────────────┘               │
│                 │                                        │
│  ┌──────────────▼───────────────────────┐               │
│  │ SQLAlchemy (ORM)                     │               │
│  │ - User Model                         │               │
│  │ - ShiftRequest Model                 │               │
│  └──────────────┬───────────────────────┘               │
└─────────────────┼───────────────────────────────────────┘
                  │
                  ▼
          ┌───────────────┐
          │   Database    │
          │  PostgreSQL   │
          │  or SQLite    │
          └───────────────┘
```

## 📋 API Endpunkte

| Methode | Endpunkt | Body | Response | Verwendet von |
|---------|----------|------|----------|---------------|
| POST | `/login` | `{name, password}` | `{success, is_admin}` | `Login.tsx` |
| GET | `/logout` | - | Redirect | `App.tsx` |
| GET | `/api/shift-requests` | - | `{success, data: [...]}` | `ShiftRequestForm.tsx` |
| POST | `/api/shift-requests` | `{date, shiftType, remarks}` | `{success, data: {...}}` | `ShiftRequestForm.tsx` |
| DELETE | `/api/shift-requests/<id>` | - | `{success}` | (noch nicht implementiert) |

## 🔐 Authentication Flow

```
1. User öffnet App → App.tsx prüft Session
   ↓
2. Nicht eingeloggt → Login.tsx wird angezeigt
   ↓
3. User gibt Name + Passwort ein
   ↓
4. api.login() sendet POST /login
   ↓
5. Flask prüft/erstellt User, setzt Session
   ↓
6. Response: {success: true, is_admin: false}
   ↓
7. App.tsx setzt isAuthenticated = true
   ↓
8. ShiftRequestForm wird angezeigt
   ↓
9. Alle weiteren API-Calls nutzen Session-Cookie
```

## ✅ Was funktioniert jetzt?

1. ✅ React Frontend ruft Flask Backend API auf
2. ✅ Session-basierte Authentifizierung funktioniert
3. ✅ CORS ist korrekt konfiguriert
4. ✅ Login/Logout funktioniert
5. ✅ Dienstwünsche können erstellt werden
6. ✅ Dienstwünsche können abgerufen werden
7. ✅ Fehlerbehandlung ist implementiert

## 🚀 Nächste Schritte zum Starten

### Terminal 1: Flask Backend
```powershell
pip install -r requirements.txt
python app.py
```

### Terminal 2: React Frontend
```powershell
npm install
npm run dev
```

### Browser öffnen
```
http://localhost:5173
```

## 📝 Entfernte/Deaktivierte Komponenten

- ❌ `src/actions/shift-request.ts` - Next.js Server Actions (nicht mehr verwendet)
- ❌ `src/lib/prisma.ts` - Prisma Client (nicht mehr verwendet)
- ❌ `src/lib/auth.ts` - Clerk Auth (nicht mehr verwendet)
- ❌ `prisma/schema.prisma` - Prisma Schema (Flask nutzt SQLAlchemy)
- ℹ️ Diese Dateien können gelöscht werden, sind aber aktuell nur nicht importiert

## 🎯 Deployment-Hinweise

### Produktion (Render.com)

1. **Backend**: Web Service mit `gunicorn app:app`
2. **Frontend**: Static Site oder von Flask serviert
3. **Environment Variable**: `VITE_API_URL=https://ihr-backend.onrender.com`
4. **CORS**: Origins-Liste in `app.py` um Produktions-URL erweitern

---

**Status**: ✅ Alle Services sind verbunden  
**Datum**: 15. Januar 2026  
**Technologie**: Flask + React + SQLAlchemy
