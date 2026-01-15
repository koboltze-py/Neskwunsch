# 🚀 GitHub Upload Anleitung

## Option 1: Git installieren und Command Line nutzen (empfohlen)

### Schritt 1: Git installieren

1. Downloaden Sie Git von: https://git-scm.com/download/win
2. Installieren Sie Git mit Standard-Einstellungen
3. PowerShell neu starten

### Schritt 2: Repository initialisieren

```powershell
# In Ihrem Projekt-Ordner:
git init
git add .
git commit -m "Initial commit: Flask + React Dienstwünsche App"
```

### Schritt 3: GitHub Repository erstellen

1. Gehen Sie zu: https://github.com/new
2. Repository Name: z.B. `drk-dienstplanung`
3. Private oder Public wählen
4. **NICHT** "Initialize with README" aktivieren
5. "Create repository" klicken

### Schritt 4: Zu GitHub pushen

GitHub zeigt Ihnen Befehle an. Nutzen Sie diese:

```powershell
git remote add origin https://github.com/IHR-USERNAME/drk-dienstplanung.git
git branch -M main
git push -u origin main
```

---

## Option 2: GitHub Desktop (einfacher, grafisch)

### Schritt 1: GitHub Desktop installieren

Download: https://desktop.github.com/

### Schritt 2: Mit GitHub Desktop arbeiten

1. GitHub Desktop öffnen
2. "File" → "Add local repository"
3. Ihr Projekt-Ordner auswählen
4. Falls noch kein Git-Repo: "Create a repository" klicken
5. Commit Message eingeben: "Initial commit"
6. "Commit to main" klicken
7. "Publish repository" klicken
8. GitHub-Account verbinden
9. Repository-Name eingeben
10. "Private" oder "Public" wählen
11. "Publish Repository" klicken

✅ Fertig! Ihr Code ist auf GitHub.

---

## Option 3: Visual Studio Code mit GitHub Extension

### Voraussetzung: VS Code installiert

1. VS Code öffnen
2. Projekt-Ordner öffnen (File → Open Folder)
3. Source Control Icon klicken (links, 3. Symbol)
4. "Initialize Repository" klicken
5. Alle Dateien stagen (+ Symbol)
6. Commit Message eingeben: "Initial commit"
7. Commit (✓ Symbol)
8. "Publish to GitHub" klicken
9. GitHub Account verbinden
10. Repository-Name und Privacy wählen
11. Bestätigen

---

## Option 4: Manueller Upload (ohne Git)

### Wenn Sie Git nicht installieren möchten:

1. Gehen Sie zu: https://github.com/new
2. Repository erstellen mit "Initialize with README"
3. Im Repository: "Add file" → "Upload files"
4. Alle Dateien Ihres Projekts in den Browser ziehen
5. Commit Message eingeben
6. "Commit changes" klicken

**⚠️ Achtung:** Dies ist keine richtige Git-Versionierung!

---

## 📋 Was wird hochgeladen?

Alle Dateien **außer** denen in `.gitignore`:
- ✅ Python-Code (`app.py`)
- ✅ React-Code (`src/`)
- ✅ Konfigurationsdateien (`package.json`, `requirements.txt`)
- ✅ Dokumentation (`.md` Dateien)
- ❌ `node_modules/` (zu groß)
- ❌ `instance/` (Datenbank - sensibel)
- ❌ `.env` Dateien (Secrets)
- ❌ `__pycache__/` (temporär)

---

## 🔒 Sicherheit

**Wichtig:** Folgende Dateien NIE hochladen:
- Passwörter
- API-Keys
- Datenbank-Dateien mit echten Daten
- `.env` Dateien

✅ `.gitignore` ist bereits konfiguriert und schützt diese Dateien.

---

## 🎯 Empfohlene Methode

**Für Einsteiger:** Option 2 (GitHub Desktop)  
**Für Fortgeschrittene:** Option 1 (Command Line)  
**Schnellste Lösung:** Option 3 (VS Code)

---

## 📞 Nächste Schritte nach Upload

1. Repository-Link teilen: `https://github.com/IHR-USERNAME/REPO-NAME`
2. Collaborators hinzufügen (Settings → Collaborators)
3. Issues für ToDos erstellen
4. GitHub Actions für CI/CD einrichten (optional)

---

**Erstellt:** 15. Januar 2026  
**Bereit für Upload:** ✅ Ja
