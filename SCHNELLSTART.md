# 🚀 SCHNELLSTART - DRK Dienstwünsche

## ✅ Was wurde gemacht?

Alle Services sind jetzt **vollständig mit Flask verbunden**:
- ✅ React Frontend ruft Flask API auf
- ✅ Login/Logout funktioniert mit Flask Sessions
- ✅ Dienstwünsche werden in Flask-Datenbank gespeichert
- ✅ CORS ist konfiguriert

---

## 🏃 SO STARTEN SIE DIE ANWENDUNG

### Schritt 1: Backend starten (Terminal 1)

```powershell
python app.py
```

**Erwartete Ausgabe:**
```
✓ Initial-Admin 'Groß' erstellt
 Dienstwunsch-Anwendung startet...
 Öffne im Browser: http://localhost:5000
```

✅ Flask läuft auf: **http://localhost:5000**

---

### Schritt 2: Frontend starten (Terminal 2)

**Neues PowerShell-Terminal öffnen!**

```powershell
npm run dev
```

**Erwartete Ausgabe:**
```
VITE ready in XXX ms
➜ Local:   http://localhost:5173/
```

✅ React läuft auf: **http://localhost:5173**

---

### Schritt 3: Im Browser öffnen

```
http://localhost:5173
```

**Login mit:**
- Name: `Groß`
- Passwort: `mettwurst`

Oder erstellen Sie einen neuen Account durch einfaches Eingeben von Name + Passwort!

---

## 📋 Checkliste

- [ ] Python Dependencies installiert? → `pip install -r requirements.txt`
- [ ] Node Modules installiert? → `npm install`
- [ ] Flask läuft auf Port 5000?
- [ ] React läuft auf Port 5173?
- [ ] Browser zeigt Login-Seite?

---

## ❓ Probleme?

### Problem: "Module not found: flask_cors"
**Lösung:**
```powershell
pip install Flask-CORS
```

### Problem: "Cannot find module 'react'"
**Lösung:**
```powershell
npm install
```

### Problem: Port 5000 bereits belegt
**Lösung:** Port in `app.py` ändern (Zeile 300):
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```
Dann auch in `.env.local` anpassen:
```
VITE_API_URL=http://localhost:5001
```

### Problem: CORS-Fehler im Browser
**Status:** ✅ Sollte gelöst sein (Flask-CORS ist konfiguriert)

Falls doch Fehler:
1. Beide Server neu starten
2. Browser-Cache leeren (Strg + Shift + Entf)
3. Im Inkognito-Modus testen

---

## 📁 Wichtige Dateien

| Datei | Funktion |
|-------|----------|
| `app.py` | Flask Backend (API) |
| `src/services/api.ts` | API-Aufrufe an Flask |
| `src/App.tsx` | React Hauptkomponente mit Login |
| `src/components/Login.tsx` | Login-Formular |
| `src/components/ShiftRequestForm.tsx` | Dienstwunsch-Formular |
| `.env.local` | Entwicklungs-Konfiguration |

---

## 🎯 Was Sie jetzt tun können

1. ✅ **Einloggen** als Admin (Groß/mettwurst)
2. ✅ **Neuen User erstellen** (einfach anderen Namen + Passwort eingeben)
3. ✅ **Dienstwunsch abgeben** (Datum + Schichtart auswählen)
4. ✅ **Eigene Wünsche ansehen** (unten im Formular)
5. ✅ **Admin-Dashboard öffnen** (als Admin unter http://localhost:5000/admin)

---

## 📚 Weitere Dokumentation

- **Vollständige Anleitung**: `FLASK_INTEGRATION.md`
- **Service-Übersicht**: `SERVICE_CONNECTIONS.md`
- **Deployment**: `DEPLOYMENT.md`

---

**Stand:** 15. Januar 2026  
**Status:** ✅ Produktionsbereit für lokale Entwicklung
