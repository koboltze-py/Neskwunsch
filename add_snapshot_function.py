# -*- coding: utf-8 -*-
"""Fügt die showUserSnapshots Funktion hinzu"""

with open('templates/admin_dashboard_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Finde </script> Tag und füge Funktion davor ein
snapshot_function = """
        async function showUserSnapshots(userId) {
            try {
                const response = await fetch(`/api/admin/users/${userId}/snapshots`);
                const data = await response.json();
                
                if (data.success) {
                    const snapshots = data.snapshots || [];
                    const current = data.current || [];
                    const userName = data.user_name;
                    
                    // Erstelle Vergleichstabelle
                    const allDates = new Set([...snapshots.map(s => s.date), ...current.map(c => c.date)]);
                    const sortedDates = [...allDates].sort();
                    
                    let html = `<div style="max-width: 800px;">`;
                    html += `<h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem;">`;
                    html += `Änderungen von ${userName}</h3>`;
                    html += `<table style="width: 100%; border-collapse: collapse; border: 1px solid #ddd;">`;
                    html += `<thead><tr style="background: #f3f4f6;">`;
                    html += `<th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Datum</th>`;
                    html += `<th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Original</th>`;
                    html += `<th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Aktuell</th>`;
                    html += `<th style="border: 1px solid #ddd; padding: 8px; text-center;">Status</th>`;
                    html += `</tr></thead><tbody>`;
                    
                    sortedDates.forEach(date => {
                        const original = snapshots.find(s => s.date === date);
                        const changed = current.find(c => c.date === date);
                        const hasChange = original && changed && original.shift_type !== changed.shift_type;
                        
                        html += `<tr style="background: ${hasChange ? '#fef3c7' : 'white'};">`;
                        html += `<td style="border: 1px solid #ddd; padding: 8px;">${new Date(date + 'T12:00:00').toLocaleDateString('de-DE')}</td>`;
                        html += `<td style="border: 1px solid #ddd; padding: 8px; font-weight: ${hasChange ? 'bold' : 'normal'};">${original ? original.shift_type : '-'}</td>`;
                        html += `<td style="border: 1px solid #ddd; padding: 8px; font-weight: ${hasChange ? 'bold' : 'normal'};">${changed ? changed.shift_type : '-'}</td>`;
                        html += `<td style="border: 1px solid #ddd; padding: 8px; text-align: center;">${hasChange ? '⚠️ GEÄNDERT' : '✓'}</td>`;
                        html += `</tr>`;
                    });
                    
                    html += `</tbody></table></div>`;
                    
                    // Erstelle Modal
                    const modal = document.createElement('div');
                    modal.style.cssText = 'position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center; z-index: 1000;';
                    modal.innerHTML = `
                        <div style="background: white; padding: 2rem; border-radius: 0.5rem; max-height: 90vh; overflow-y: auto;">
                            ${html}
                            <button onclick="this.closest('div').parentElement.remove()" style="margin-top: 1rem; padding: 0.5rem 1rem; background: #3b82f6; color: white; border: none; border-radius: 0.25rem; cursor: pointer;">
                                Schließen
                            </button>
                        </div>
                    `;
                    document.body.appendChild(modal);
                } else {
                    alert('Fehler beim Laden der Änderungen: ' + (data.error || 'Unbekannter Fehler'));
                }
            } catch (error) {
                alert('Fehler beim Laden der Änderungen: ' + error.message);
            }
        }
"""

# Finde </script> und füge davor ein
script_close_pos = content.rfind('</script>')
if script_close_pos > 0:
    content = content[:script_close_pos] + snapshot_function + "\n    " + content[script_close_pos:]
    print("✓ showUserSnapshots Funktion hinzugefügt")
else:
    print("✗ </script> nicht gefunden")

with open('templates/admin_dashboard_v3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Datei gespeichert")
