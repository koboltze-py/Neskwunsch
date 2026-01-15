# Git Upload Skript für DRK Dienstwünsche
# Führen Sie dieses Skript in einem NEUEN PowerShell-Terminal aus!

Write-Host "🚀 GitHub Upload wird vorbereitet..." -ForegroundColor Green
Write-Host ""

# Git-Konfiguration (einmalig)
Write-Host "⚙️ Git wird konfiguriert..." -ForegroundColor Yellow
git config --global user.name "test"
git config --global user.email "drk@example.com"

# Repository initialisieren
Write-Host "📦 Repository wird initialisiert..." -ForegroundColor Yellow
git init

# Alle Dateien hinzufügen
Write-Host "➕ Dateien werden hinzugefügt..." -ForegroundColor Yellow
git add .

# Commit erstellen
Write-Host "💾 Commit wird erstellt..." -ForegroundColor Yellow
git commit -m "Initial commit: DRK Dienstwünsche App mit Flask und React

- Flask Backend mit SQLAlchemy
- React Frontend mit TypeScript
- Login/Auth System
- Dienstwunsch-Verwaltung
- Admin Dashboard
- Responsive Design mit TailwindCSS"

Write-Host ""
Write-Host "✅ Lokales Repository ist bereit!" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Nächste Schritte:" -ForegroundColor Cyan
Write-Host "1. Gehen Sie zu: https://github.com/new" -ForegroundColor White
Write-Host "2. Repository-Name: drk-dienstplanung" -ForegroundColor White
Write-Host "3. Private auswählen" -ForegroundColor White
Write-Host "4. NICHT 'Initialize with README' aktivieren" -ForegroundColor White
Write-Host "5. 'Create repository' klicken" -ForegroundColor White
Write-Host ""
Write-Host "6. Dann diese Befehle ausführen:" -ForegroundColor Cyan
Write-Host ""
Write-Host "   git remote add origin https://github.com/test/drk-dienstplanung.git" -ForegroundColor Yellow
Write-Host "   git branch -M main" -ForegroundColor Yellow
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""
Write-Host "📋 Diese Befehle wurden in die Zwischenablage kopiert!" -ForegroundColor Green

# Befehle in Zwischenablage
$commands = @"
git remote add origin https://github.com/test/drk-dienstplanung.git
git branch -M main
git push -u origin main
"@

Set-Clipboard -Value $commands
Write-Host "✨ Einfach mit STRG+V einfügen nach Repository-Erstellung!" -ForegroundColor Green
