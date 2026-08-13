"""
Student Management System - CLI entry point.
Run with: python main.py
"""

from student_manager import StudentManager
from exceptions import StudentNotFoundError, DuplicateStudentError, InvalidInputError


MENU = """
========================================
      STUDENT MANAGEMENT SYSTEM
========================================
1. Add Student
2. View All Students
3. Update Student
4. Delete Student
5. Search Student by Name
6. Filter by Course
7. Filter by Grade
8. Sort by Marks
9. Exit
========================================
"""


def print_students(students):
    if not students:
        print("No records found.")
        return
    print("-" * 90)
    for s in students:
        print(s)
    print("-" * 90)
    print(f"Total: {len(students)} student(s)")


def add_student(manager):
    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")
        student = manager.add_student(student_id, name, age, course, marks)
        print(f"\n✅ Student added successfully:\n{student}")
    except (InvalidInputError, DuplicateStudentError) as e:
        print(f"\n❌ Error: {e}")


def view_all(manager):
    print("\n--- All Students ---")
    print_students(manager.list_all())


def update_student(manager):
    try:
        student_id = input("Enter Student ID to update: ")
        manager.find_by_id(student_id)  # confirm exists first
        print("Leave field blank to keep current value.")
        name = input("New Name: ")
        age = input("New Age: ")
        course = input("New Course: ")
        marks = input("New Marks: ")

        updates = {}
        if name: updates["name"] = name
        if age: updates["age"] = age
        if course: updates["course"] = course
        if marks: updates["marks"] = marks

        student = manager.update_student(student_id, **updates)
        print(f"\n✅ Student updated:\n{student}")
    except (StudentNotFoundError, InvalidInputError) as e:
        print(f"\n❌ Error: {e}")


def delete_student(manager):
    try:
        student_id = input("Enter Student ID to delete: ")
        student = manager.delete_student(student_id)
        print(f"\n✅ Deleted: {student}")
    except StudentNotFoundError as e:
        print(f"\n❌ Error: {e}")


def search_student(manager):
    try:
        keyword = input("Enter name (or part of it) to search: ")
        results = manager.search_by_name(keyword)
        print("\n--- Search Results ---")
        print_students(results)
    except StudentNotFoundError as e:
        print(f"\n❌ Error: {e}")


def filter_by_course(manager):
    course = input("Enter course to filter by: ")
    results = manager.filter_by_course(course)
    print(f"\n--- Students in {course.upper()} ---")
    print_students(results)


def filter_by_grade(manager):
    grade = input("Enter grade to filter by (A+, A, B, C, F): ")
    results = manager.filter_by_grade(grade)
    print(f"\n--- Students with Grade {grade.upper()} ---")
    print_students(results)


def sort_by_marks(manager):
    order = input("Sort order - (H)igh to low or (L)ow to high? [H/L]: ").strip().lower()
    descending = order != "l"
    results = manager.sort_by_marks(descending=descending)
    print("\n--- Students Sorted by Marks ---")
    print_students(results)


def main():
    manager = StudentManager()

    actions = {
        "1": add_student,
        "2": view_all,
        "3": update_student,
        "4": delete_student,
        "5": search_student,
        "6": filter_by_course,
        "7": filter_by_grade,
        "8": sort_by_marks,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "9":
            print("\nGoodbye! 👋")
            break
        elif choice in actions:
            try:
                actions[choice](manager)
            except Exception as e:
                # Safety net for any unexpected error, so the app never crashes
                print(f"\n❌ Unexpected error: {e}")
        else:
            print("\n❌ Invalid choice. Please enter a number between 1-9.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
