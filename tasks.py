"""TaskLite - winzige Aufgabenverwaltung (Seminar-Beispielprojekt S3008)."""

_tasks = []


def add_task(title):
    """Legt eine neue Aufgabe an und gibt sie zurueck."""
    if not title:
        raise ValueError("Titel darf nicht leer sein")
    task = {"id": len(_tasks) + 1, "title": title, "done": False}
    _tasks.append(task)
    return task


def complete_task(task_id):
    """Markiert eine Aufgabe als erledigt."""
    for task in _tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise KeyError(f"Keine Aufgabe mit id={task_id}")


def open_tasks():
    """Alle offenen Aufgaben."""
    return [t for t in _tasks if not t["done"]]


def count_all():
    """Anzahl aller Aufgaben (offen + erledigt)."""
    return len(_tasks)


def reset():
    """Nur fuer Tests: Zustand zuruecksetzen."""
    _tasks.clear()
