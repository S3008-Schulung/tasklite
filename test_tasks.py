import unittest

import tasks


class TaskTests(unittest.TestCase):
    def setUp(self):
        tasks.reset()

    def test_add_task(self):
        t = tasks.add_task("Kaffee kochen")
        self.assertEqual(t["title"], "Kaffee kochen")
        self.assertFalse(t["done"])

    def test_empty_title_raises(self):
        with self.assertRaises(ValueError):
            tasks.add_task("")

    def test_complete_task(self):
        t = tasks.add_task("Review schreiben")
        tasks.complete_task(t["id"])
        self.assertEqual(tasks.open_tasks(), [])

    def test_open_tasks(self):
        tasks.add_task("A")
        b = tasks.add_task("B")
        tasks.complete_task(b["id"])
        self.assertEqual(len(tasks.open_tasks()), 1)


if __name__ == "__main__":
    unittest.main()


class CountTests(unittest.TestCase):
    def setUp(self):
        tasks.reset()

    def test_count_all(self):
        tasks.add_task("A")
        tasks.add_task("B")
        self.assertEqual(tasks.count_all(), 2)
