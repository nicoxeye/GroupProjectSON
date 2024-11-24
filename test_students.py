import os
import pytest
from main import (
    import_from_file,
    export_attendance,
    add_student,
    edit_student
)

TEST_FILE = "test_students.csv"

# testy z zapisywaniem do pliku i wczytywaniem z pliku
def test_import_from_file():
    with open(TEST_FILE, "w") as f:
        f.write("John,Doe,yes\nJane,Smith,no\n")
    
    students = import_from_file(TEST_FILE)
    assert len(students) == 2
    assert students[0] == {"first_name": "John", "last_name": "Doe", "present": True}
    assert students[1] == {"first_name": "Jane", "last_name": "Smith", "present": False}

    os.remove(TEST_FILE)

def test_export_attendance():
    students = [
        {"first_name": "Alice", "last_name": "Brown", "present": True},
        {"first_name": "Bob", "last_name": "Green", "present": False},
    ]
    
    export_attendance(students, TEST_FILE)
    with open(TEST_FILE, "r") as f:
        lines = f.readlines()
    assert lines == ["Alice,Brown,yes\n", "Bob,Green,no\n"]
    
    os.remove(TEST_FILE)

# testy z operacjami na studentach i obecności
def test_add_student():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    
    add_student("Charlie", "Johnson", TEST_FILE)
    
    with open(TEST_FILE, "r") as f:
        lines = f.readlines()
    assert lines[1].strip() == "Charlie,Johnson,False"
    os.remove(TEST_FILE)

def test_edit_student():
    with open(TEST_FILE, "w") as f:
        f.write("first_name,last_name,present\nJohn,Doe,False\nJane,Smith,False\n")
    edit_student("John", "Doe", "Jonathan", "Doe", TEST_FILE)

    students = import_from_file(TEST_FILE)
    assert any(s["first_name"] == "Jonathan" and s["last_name"] == "Doe" for s in students)
    assert not any(s["first_name"] == "John" and s["last_name"] == "Doe" for s in students)

    os.remove(TEST_FILE)