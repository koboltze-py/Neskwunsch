# 🚀 GitHub Upload - Schritt für Schritt

## ✅ Git wurde installiert!

**WICHTIG:** Bitte öffnen Sie ein **NEUES PowerShell-Fenster**, damit Git funktioniert!

---

## 📝 Befehle für Ihren GitHub-Upload

### Schritt 1: Neues PowerShell-Terminal öffnen

1. Aktuelles Terminal **schließen**
2. **Neues** PowerShell öffnen
3. Zum Projekt-Ordner navigieren:

```powershell
cd "c:\Users\DRKairport\OneDrive - Deutsches Rotes Kreuz - Kreisverband Köln e.V\Dateien von Erste-Hilfe-Station-Flughafen - DRK Köln e.V_ - !Gemeinsam.26\Nesk\Dienstwünsche"
```

### Schritt 2: Git-Repository initialisieren

```powershell
git init
```

### Schritt 3: Alle Dateien hinzufügen

```powershell
git add .
```

### Schritt 4: Ersten Commit erstellen

```powershell
git commit -m "Initial commit: DRK Dienstwünsche App mit Flask und React"
```

### Schritt 5: GitHub Repository erstellen

1. Öffnen Sie: https://github.com/new
2. Repository Name: `drk-dienstplanung` (oder beliebig)
3. Beschreibung: "Dienstwunsch-Verwaltung für DRK Köln"
4. **Private** oder **Public** wählen
5. **NICHT** "Initialize with README" aktivieren!
6. "Create repository" klicken

### Schritt 6: Mit GitHub verbinden und pushen

**GitHub zeigt Ihnen nach der Erstellung Befehle an. Nutzen Sie diese:**

```powershell
git remote add origin https://github.com/test/drk-dienstplanung.git
git branch -M main
git push -u origin main
```

**Falls Login erforderlich:**
- GitHub wird nach Username und Token fragen
- Token erstellen unter: https://github.com/settings/tokens
- Token kopieren und als Passwort verwenden

---

## 🔐 Git-Konfiguration (einmalig)

Falls Git nach Name/Email fragt:

```powershell
git config --global user.name "test"
git config --global user.email "ihre-email@example.com"
```

---

## ✅ Erfolgreich? Prüfen Sie:

1. Öffnen Sie: `https://github.com/test/drk-dienstplanung`
2. Sie sollten alle Ihre Dateien sehen
3. README.md wird automatisch angezeigt

---

## 📋 Was wird hochgeladen?

✅ **Hochgeladen werden:**
- `app.py` (Flask Backend)
- `src/` (React Frontend)
- `package.json`, `requirements.txt`
- Alle Dokumentations-Dateien
- `.gitignore`

❌ **NICHT hochgeladen werden:**
- `node_modules/` (wird von .gitignore ausgeschlossen)
- `instance/` (lokale Datenbank)
- `.env.local` (Secrets)
- `__pycache__/` (Python-Cache)

---

## 🐛 Probleme?

### "Permission denied"
```powershell
# Personal Access Token erstellen:
# https://github.com/settings/tokens
# Dann als Passwort beim Push verwenden
```

### "Nothing to commit"
```powershell
# Status prüfen:
git status

# Falls Dateien fehlen:
git add -A
git commit -m "Alle Dateien hinzugefügt"
```

### Git nicht gefunden
```powershell
# PowerShell NEU starten!
# Dann git --version testen
```

---

## 🎯 Zusammenfassung

**IN NEUEM POWERSHELL-TERMINAL:**

```powershell
# 1. Zum Ordner navigieren
cd "c:\Users\DRKairport\OneDrive - Deutsches Rotes Kreuz - Kreisverband Köln e.V\Dateien von Erste-Hilfe-Station-Flughafen - DRK Köln e.V_ - !Gemeinsam.26\Nesk\Dienstwünsche"

# 2. Git initialisieren
git init
git add .
git commit -m "Initial commit: DRK Dienstwünsche App"

# 3. Zu GitHub pushen (nach Repository-Erstellung auf GitHub)
git remote add origin https://github.com/test/drk-dienstplanung.git
git branch -M main
git push -u origin main
```

---

**Ihr GitHub:** https://github.com/test  
**Repository:** https://github.com/test/drk-dienstplanung (nach Upload)

✅ Viel Erfolg!
