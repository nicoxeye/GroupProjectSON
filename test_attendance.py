     
import unittest
import os
from main import import_from_file, export_attendance, add_student

class TestAttendanceSystem(unittest.TestCase):

    def setUp(self):
        """Tworzy pliki testowe i ustawia środowisko przed każdym testem."""
        self.test_import_file = "test_import.csv"
        with open(self.test_import_file, 'w') as file:
            file.write("John,Doe,yes\nJane,Smith,no\n")

        self.test_export_file = "test_export.csv"
        self.students = [
            {"first_name": "Alice", "last_name": "Wonderland", "present": True},
            {"first_name": "Bob", "last_name": "Builder", "present": False}
        ]

    def tearDown(self):
        """Czyści pliki testowe po każdym teście."""
        if os.path.exists(self.test_import_file):
            os.remove(self.test_import_file)
        if os.path.exists(self.test_export_file):
            os.remove(self.test_export_file)

    def test_import_from_file(self):
        """Testuje importowanie uczniów z pliku."""
        students = import_from_file(self.test_import_file)
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0]['first_name'], "John")
        self.assertTrue(students[0]['present'])
        self.assertFalse(students[1]['present'])

    def test_export_attendance(self):
        """Testuje eksportowanie listy obecności do pliku."""
        export_attendance(self.students, self.test_export_file)
        self.assertTrue(os.path.isfile(self.test_export_file))

        with open(self.test_export_file, 'r') as file:
            lines = file.readlines()
            self.assertEqual(lines[0].strip(), "Alice,Wonderland,yes")
            self.assertEqual(lines[1].strip(), "Bob,Builder,no")

    def test_add_student(self):
        """Testuje dodawanie nowego ucznia do pliku."""
        test_add_file = "test_add.csv"
        if os.path.isfile(test_add_file):
            os.remove(test_add_file)

        add_student("Test", "User", test_add_file)
        self.assertTrue(os.path.isfile(test_add_file))

        with open(test_add_file, 'r') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 2)  # Nagłówki + jeden student
            self.assertIn("Test,User,False", lines[1])

        os.remove(test_add_file)


if __name__ == "__main__":
    unittest.main()