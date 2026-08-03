# TaskLite

Winzige Aufgabenverwaltung als Seminar-Beispielprojekt (GFU S3008).

## Starten

    python3 app.py        # Server auf Port 8000, GET /tasks

## Tests

    python3 -m unittest -q

## Architektur

TaskLite besteht aus zwei Dateien: `tasks.py` (Fachlogik) und `app.py`
(HTTP-Schicht). Die Aufgaben liegen im Arbeitspeicher, es gibt keine
Datenbank — bewusst minimal gehalten.
