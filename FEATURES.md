# Feature-Liste: DRK Dienstwünsche-App

**Schichtplanungs-System für das Deutsche Rote Kreuz Köln - Erste-Hilfe-Station Flughafen**

---

## 🔐 Authentifizierung & Benutzerverwaltung

- **Benutzer-Registrierung** - Neue Mitarbeiter können sich selbst registrieren
- **Login-System** - Sichere Anmeldung mit Session-Management
- **Passwort-Hashing** - SHA-256 Verschlüsselung aller Passwörter
- **Passwort-Reset** - Admins können temporäre Passwörter vergeben
- **Passwort-Änderung** - Benutzer müssen nach Reset neue Passwörter setzen
- **Rollen-System** - Unterscheidung zwischen normalen Benutzern und Administratoren
- **Session-Verwaltung** - Automatisches Session-Handling

---

## 📅 Dienstwunsch-Verwaltung

### Für Mitarbeiter:
- **Schichtwünsche erstellen** - Auswahl zwischen Früh-, Spät- und Nachtschicht
- **Mehrere Wünsche gleichzeitig** - Batch-Erstellung von Dienstwünschen
- **Bemerkungen hinzufügen** - Notizfeld für zusätzliche Informationen
- **Wünsche bearbeiten** - Nachträgliche Änderung eigener Dienstwünsche
- **Wünsche löschen** - Entfernen nicht mehr gewünschter Schichten
- **Wünsche ansehen** - Übersicht aller eigenen Dienstwünsche
- **Status-Tracking** - Anzeige ob Wünsche bestätigt wurden (PENDING/CONFIRMED)
- **Snapshot-System** - Erste Eingabe wird gespeichert und kann eingesehen werden

### Schichttypen:
- **Frühschicht**
- **Spätschicht**
- **Nachtschicht**

---

## 👨‍💼 Admin-Dashboard

### Benutzerverwaltung:
- **Benutzer-Übersicht** - Liste aller registrierten Mitarbeiter
- **Admin-Rechte vergeben** - Benutzer zu Admins ernennen oder zurückstufen
- **Passwort zurücksetzen** - Temporäre Passwörter für Benutzer erstellen
- **Benutzer-Details** - Anzeige von E-Mail, Registrierungsdatum, etc.

### Dienstwunsch-Verwaltung:
- **Zentrale Übersicht** - Alle Dienstwünsche aller Mitarbeiter
- **Kalenderansicht** - Darstellung nach Datum gruppiert
- **Einzelbestätigung** - Bestätigung einzelner Dienstwünsche
- **Massenbestätigung** - Alle Wünsche eines Mitarbeiters auf einmal bestätigen
- **Originalwünsche einsehen** - Snapshots der ersten Eingaben anzeigen
- **Änderungsverfolgung** - Erkennung von nachträglichen Änderungen
- **Zeitstempel** - Anzeige von Erstellungs- und Änderungsdatum

---

## 📝 Notiz-System

- **Schicht-Notizen** - Notizen zu einzelnen Dienstwünschen hinzufügen
- **Mehrere Notizen** - Beliebig viele Notizen pro Schicht
- **Autor-Kennzeichnung** - Anzeige wer die Notiz erstellt hat
- **Zeitstempel** - Wann wurde die Notiz erstellt
- **Notizen anzeigen** - Alle Notizen zu einem Dienstwunsch einsehen

---

## 💬 Nachrichten-System

- **Nachrichten senden** - Mitarbeiter können Nachrichten an Admins senden
- **Nachrichten empfangen** - Admins sehen alle eingegangenen Nachrichten
- **Gelesen-Status** - Markierung welche Nachrichten bereits gelesen wurden
- **Nachrichten-Historie** - Alle Nachrichten mit Zeitstempel
- **Multi-Admin-Support** - Gelesen-Status pro Admin

---

## 📊 Export-Funktionen

### Excel-Export:
- **Formatierte Tabellen** - Professionell gestaltete Dienstpläne
- **Farbcodierung** - Unterschiedliche Farben für Schichttypen
- **Gruppierung** - Nach Datum organisiert
- **Zusatzinfos** - Bemerkungen und Notizen inklusive
- **Download** - Direkter Excel-Download (.xlsx)

### PDF-Export:
- **Druckoptimiert** - Landscape-Format für bessere Lesbarkeit
- **Tabellen-Layout** - Übersichtliche Darstellung
- **Vollständige Daten** - Alle Dienstwünsche mit Details
- **Download** - Direkter PDF-Download

---

## 🎨 Benutzeroberfläche

### Frontend:
- **React-Interface** - Moderne Single-Page-Application
- **TypeScript** - Typsichere Entwicklung
- **Responsive Design** - Funktioniert auf Desktop, Tablet und Smartphone
- **HTML-Templates** - Alternative klassische Ansichten
- **Tailwind CSS** - Modernes, anpassbares Design

### Ansichten:
- **Login-Seite** - Anmeldeformular
- **Dienstwunsch-Formular** - Eingabemaske für Schichtwünsche
- **Admin-Dashboard** - Verwaltungsoberfläche (3 Versionen)

---

## 🗄️ Datenbank-Features

- **PostgreSQL** - Production-Datenbank (Render/Cloud Run)
- **SQLite** - Lokale Entwicklung
- **Auto-Migration** - Automatische Schema-Updates
- **Datenintegrität** - Foreign Keys und Constraints
- **Cascade-Delete** - Automatische Bereinigung bei Löschungen
- **Timestamps** - Automatische Zeitstempel für alle Einträge

### Datenbank-Tabellen:
- `users` - Benutzerdaten
- `shift_requests` - Dienstwünsche
- `shift_notes` - Notizen zu Schichten
- `shift_request_snapshots` - Originalwünsche
- `messages` - Nachrichten
- `message_reads` - Gelesen-Status

---

## 🔧 Technische Features

### Backend:
- **Flask Framework** - Python Web-Framework
- **RESTful API** - Strukturierte API-Endpunkte
- **CORS-Support** - Cross-Origin Resource Sharing für React
- **Session-Management** - Sichere Sitzungsverwaltung
- **Error-Handling** - Umfassende Fehlerbehandlung
- **IPv6→IPv4 Fix** - Automatische Netzwerk-Kompatibilität

### Sicherheit:
- **Password-Hashing** - SHA-256 Verschlüsselung
- **Session-Secrets** - Kryptographisch sichere Session-Keys
- **Login-Required** - Geschützte Routen
- **Admin-Checks** - Autorisierungsprüfungen

### Deployment:
- **Docker-Support** - Container-basierte Bereitstellung
- **Cloud Run** - Google Cloud Deployment
- **Render.com** - Alternative Hosting-Plattform
- **docker-compose** - Lokale Entwicklungsumgebung

---

## 📈 Datenanalyse & Reporting

- **Schicht-Statistiken** - Übersicht über Wunschverteilung
- **Benutzer-Aktivität** - Wer hat wann Wünsche eingereicht
- **Änderungsprotokoll** - Nachverfolgung von Modifikationen
- **Export-Optionen** - Daten für externe Verarbeitung

---

## 🌐 API-Endpunkte

### Öffentlich:
- `POST /login` - Benutzer-Anmeldung
- `POST /register` - Benutzer-Registrierung
- `GET /logout` - Benutzer-Abmeldung

### Authentifiziert:
- `GET /api/shift-requests` - Eigene Dienstwünsche abrufen
- `POST /api/shift-requests` - Neuen Dienstwunsch erstellen
- `POST /api/shift-requests/batch` - Mehrere Wünsche erstellen
- `DELETE /api/shift-requests/<id>` - Dienstwunsch löschen
- `GET /api/shift-notes/<id>` - Notizen zu Schicht abrufen
- `POST /api/shift-notes` - Neue Notiz erstellen
- `GET /api/messages` - Nachrichten abrufen
- `POST /api/messages` - Neue Nachricht senden

### Admin-Only:
- `GET /admin` - Admin-Dashboard
- `GET /api/admin/users` - Alle Benutzer
- `POST /api/admin/users/<id>/toggle-admin` - Admin-Status ändern
- `POST /api/admin/users/<id>/reset-password` - Passwort zurücksetzen
- `POST /api/admin/shift-requests/<id>/confirm` - Wunsch bestätigen
- `POST /api/admin/users/<id>/confirm-all-shifts` - Alle Wünsche bestätigen
- `GET /api/admin/users/<id>/snapshots` - Original-Wünsche anzeigen
- `POST /api/messages/<id>/read` - Nachricht als gelesen markieren
- `GET /api/admin/export` - JSON-Export
- `GET /api/admin/export/excel` - Excel-Export
- `GET /api/admin/export/pdf` - PDF-Export

---

## 📱 Plattform-Kompatibilität

- **Windows** - Vollständig unterstützt
- **macOS** - Vollständig unterstützt
- **Linux** - Vollständig unterstützt
- **Web-Browser** - Chrome, Firefox, Safari, Edge
- **Mobile Browser** - Responsive Design für Smartphones/Tablets

---

## 🔄 Workflow-Features

1. **Mitarbeiter registriert sich** → Account wird erstellt
2. **Mitarbeiter loggt sich ein** → Session wird gestartet
3. **Mitarbeiter gibt Dienstwünsche ein** → Snapshot wird erstellt
4. **Admin sieht alle Wünsche** → Kann bestätigen/exportieren
5. **Mitarbeiter ändert Wünsche** → Admin sieht Original + Änderung
6. **Admin bestätigt Wünsche** → Status wechselt zu CONFIRMED
7. **Admin exportiert Plan** → Excel/PDF wird generiert

---

**Version:** 1.0.0  
**Status:** ✅ Produktionsbereit  
**Letzte Aktualisierung:** 17. Januar 2026
