# -*- coding: utf-8 -*-
"""Fügt den Änderungen-Button zum Admin-Dashboard hinzu"""

with open('templates/admin_dashboard_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Suche die Stelle nach "Alle bestätigen" Button
old_section = """                                ` : ''}
                            </div>
                        </div>
                        <div class="divide-y divide-gray-200">"""

new_section = """                                ` : ''}
                            ${hasModifications ? `
                                <button type="button" onclick="showUserSnapshots(${userId})" class="ml-2 px-4 py-2 bg-orange-600 text-white rounded-lg hover:bg-orange-700 text-sm font-semibold">
                                    ⚠️ Änderungen anzeigen
                                </button>
                            ` : ''}
                            </div>
                        </div>
                        <div class="divide-y divide-gray-200">"""

if old_section in content:
    content = content.replace(old_section, new_section)
    print("✓ Button erfolgreich eingefügt")
else:
    print("✗ Ziel-Abschnitt nicht gefunden")
    print("Versuche alternative Suche...")
    
with open('templates/admin_dashboard_v3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Datei gespeichert")
