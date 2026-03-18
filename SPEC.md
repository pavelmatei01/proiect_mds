
# Specificație: Aplicație TODO list (CLI REPL)

O aplicație de tip linie de comandă (CLI) care rulează într-o buclă interactivă (REPL).

**Sarcina trebuie să conțină:**
- id, titlu, descriere, deadline, interval_orar, status.

**Comenzi suportate:**
1. `add` - Creează o sarcină nouă.
2. `done <id>` - Marchează ca rezolvată.
3. `delete <id>` - Șterge sarcina.
4. `list` - Afișează toate sarcinile.
5. `list <data_inceput> <data_sfarsit>` - Afișează sarcinile din interval.
6. `exit` sau `quit` - Închide aplicația.

Datele trebuie salvate local într-un fișier `tasks.json`. Cod în Python.

