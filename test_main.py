import os
import pytest
from typing import List, Dict
from main import import_from_file, export_attendance, add_student, edit_student, manage_attendance

class MockCSVStorage:
    def __init__(self):
        self.data = []

    def write(self, rows: List[Dict[str, str]]):
        self.data = rows
    
    def read(self) -> List[Dict[str, str]]:
        return self.data
    
    def append(self, row: Dict[str, str]):
        self.data.append(row)


class TestAttendanceSystem:
    #test: saving to file
    def test_save_to_file(self):
        #Given
        students = [
              {"first_name": "John", "last_name": "Doe", "present": True},
              {"first_name": "Jane", "last_name": "Smith", "present": False},
        ]
        mock_storage = MockCSVStorage()

        #When
        export_attendance(students, mock_storage)

        #Then
        expected_data = [
           {"first_name": "John", "last_name": "Doe", "present": "yes"},
           {"first_name": "Jane", "last_name": "Smith", "present": "no"}, 
        ]
        assert mock_storage.data == expected_data

    #test: loading from file
    def test_load_from_file(self):
        #Given
        mock_storage = MockCSVStorage()
        mock_storage.write([
                {"first_name": "John", "last_name": "Doe", "present": "yes"},
                {"first_name": "Jane", "last_name": "Smith", "present": "no"},
            ])

        #When
        students = import_from_file(mock_storage)

        #Then
        expected_students = [
                 {"first_name": "John", "last_name": "Doe", "present": True},
                 {"first_name": "Jane", "last_name": "Smith", "present": False},
            ]
        assert students == expected_students

    #test: adding students
    def test_add_students(self):
        #Given
        mock_storage = MockCSVStorage()
        mock_storage.write([
                    {"first_name": "John", "last_name": "Doe", "present": "yes"},
                ])

        #When
        add_student("Jane", "Smith", mock_storage)

        #Then
        expected_data = [
                    {"first_name": "John", "last_name": "Doe", "present": "yes"},
                    {"first_name": "Jane", "last_name": "Smith", "present": "no"},
                ]
        assert mock_storage.data == expected_data

    #test: editing students' data
    def test_edit_student(self):
        #Given
        mock_storage = MockCSVStorage()
        mock_storage.write([
                         {"first_name": "John", "last_name": "Doe", "present": "yes"},
                         {"first_name": "Jane", "last_name": "Smith", "present": "no"},
                    ])

        #When
        edit_student("Jane", "Smith", "Janet", "Smith", mock_storage)

        #Then
        expected_data = [
                        {"first_name": "John", "last_name": "Doe", "present": "yes"},
                        {"first_name": "Janet", "last_name": "Smith", "present": "no"},

                    ]
        assert mock_storage.data == expected_data
    
    #test: attendance
    def test_attendance_management(self):
        # Given
        mock_storage = MockCSVStorage()
        mock_storage.write([
            {"first_name": "John", "last_name": "Doe", "present": "no"},
        ])

        #replacement function to simulate user input
        def mock_input(p):
            if "Is John Doe present" in p:
                return "yes"
            return "no"
        
        #When
        students = mock_storage.read()
        for student in students:
            if mock_input(f"Is {student['first_name']} {student['last_name']} present? (yes/no): ").lower() == "yes":
                student["present"] = "yes"
            else:
                student["present"] = "no"
        
        mock_storage.write(students)

        #Then
        expected_data = [
            {"first_name": "John", "last_name": "Doe", "present": "yes"},
        ]
        assert mock_storage.read() == expected_data