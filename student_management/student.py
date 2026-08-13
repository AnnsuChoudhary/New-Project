"""
Student class: represents a single student record.
Demonstrates OOP concepts: encapsulation, constructors, dunder methods.
"""

from exceptions import InvalidInputError


class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = self._validate_id(student_id)
        self.name = self._validate_name(name)
        self.age = self._validate_age(age)
        self.course = self._validate_course(course)
        self.marks = self._validate_marks(marks)

    # ---------- Validation helpers ----------
    @staticmethod
    def _validate_id(student_id):
        if not str(student_id).strip():
            raise InvalidInputError("Student ID cannot be empty")
        return str(student_id).strip()

    @staticmethod
    def _validate_name(name):
        if not name or not name.strip():
            raise InvalidInputError("Name cannot be empty")
        if not all(part.isalpha() for part in name.split()):
            raise InvalidInputError("Name must contain only letters and spaces")
        return name.strip().title()

    @staticmethod
    def _validate_age(age):
        try:
            age = int(age)
        except (ValueError, TypeError):
            raise InvalidInputError("Age must be a number")
        if not (3 <= age <= 100):
            raise InvalidInputError("Age must be between 3 and 100")
        return age

    @staticmethod
    def _validate_course(course):
        if not course or not course.strip():
            raise InvalidInputError("Course cannot be empty")
        return course.strip().upper()

    @staticmethod
    def _validate_marks(marks):
        try:
            marks = float(marks)
        except (ValueError, TypeError):
            raise InvalidInputError("Marks must be a number")
        if not (0 <= marks <= 100):
            raise InvalidInputError("Marks must be between 0 and 100")
        return marks

    # ---------- Serialization ----------
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            course=data["course"],
            marks=data["marks"],
        )

    # ---------- Display ----------
    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        return "F"

    def __str__(self):
        return (f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | "
                f"Course: {self.course} | Marks: {self.marks} | Grade: {self.grade()}")

    def __repr__(self):
        return f"Student({self.student_id!r}, {self.name!r})"
