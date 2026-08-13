"""
Custom exceptions for the Student Management System.
Using custom exceptions gives clearer error messages and makes
error handling in main.py and student_manager.py more precise.
"""


class StudentNotFoundError(Exception):
    """Raised when a student ID/name is not found in records."""
    def __init__(self, identifier):
        self.identifier = identifier
        super().__init__(f"Student not found: '{identifier}'")


class DuplicateStudentError(Exception):
    """Raised when trying to add a student with an ID that already exists."""
    def __init__(self, student_id):
        self.student_id = student_id
        super().__init__(f"Student with ID '{student_id}' already exists")


class InvalidInputError(Exception):
    """Raised when user input fails validation (e.g. empty name, bad marks)."""
    def __init__(self, message="Invalid input provided"):
        super().__init__(message)
