"""
StudentManager: business logic layer for CRUD + search operations.
Talks to FileHandler for persistence and works with Student objects.
"""

from student import Student
from file_handler import FileHandler
from exceptions import StudentNotFoundError, DuplicateStudentError, InvalidInputError


class StudentManager:
    def __init__(self, filepath="data/students.json"):
        self.file_handler = FileHandler(filepath)
        self.students = self._load_students()

    def _load_students(self):
        raw_data = self.file_handler.load_data()
        return [Student.from_dict(item) for item in raw_data]

    def _save(self):
        self.file_handler.save_data([s.to_dict() for s in self.students])

    # ---------- CREATE ----------
    def add_student(self, student_id, name, age, course, marks):
        if any(s.student_id == str(student_id).strip() for s in self.students):
            raise DuplicateStudentError(student_id)
        student = Student(student_id, name, age, course, marks)
        self.students.append(student)
        self._save()
        return student

    # ---------- READ ----------
    def list_all(self):
        return self.students

    def find_by_id(self, student_id):
        for s in self.students:
            if s.student_id == str(student_id).strip():
                return s
        raise StudentNotFoundError(student_id)

    # ---------- UPDATE ----------
    def update_student(self, student_id, **kwargs):
        student = self.find_by_id(student_id)
        updated_data = student.to_dict()
        for key, value in kwargs.items():
            if value is not None and value != "":
                updated_data[key] = value
        updated_student = Student.from_dict(updated_data)

        index = self.students.index(student)
        self.students[index] = updated_student
        self._save()
        return updated_student

    # ---------- DELETE ----------
    def delete_student(self, student_id):
        student = self.find_by_id(student_id)
        self.students.remove(student)
        self._save()
        return student

    # ---------- SEARCH & FILTER ----------
    def search_by_name(self, keyword):
        keyword = keyword.strip().lower()
        results = [s for s in self.students if keyword in s.name.lower()]
        if not results:
            raise StudentNotFoundError(keyword)
        return results

    def filter_by_course(self, course):
        course = course.strip().upper()
        return [s for s in self.students if s.course == course]

    def filter_by_grade(self, grade):
        grade = grade.strip().upper()
        return [s for s in self.students if s.grade() == grade]

    def sort_by_marks(self, descending=True):
        return sorted(self.students, key=lambda s: s.marks, reverse=descending)
