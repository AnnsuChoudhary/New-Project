# 🎓 Student Management System

A Python-based console application to manage student records — built with
Object-Oriented Programming, file handling (JSON persistence), and robust
exception handling.

## Features

- **CRUD Operations** — Add, view, update, and delete student records
- **Search & Filter** — Search by name, filter by course or grade, sort by marks
- **OOP Design** — `Student` model class with validation and grade calculation
- **File Handling** — Records persisted to `data/students.json`
- **Exception Handling** — Custom exceptions for duplicate IDs, missing
  records, and invalid input, so the app never crashes on bad data
- **Modular Structure** — Separate layers for model, persistence, business
  logic, and CLI

## Project Structure

```
student_management/
├── main.py              # CLI entry point / menu
├── student.py           # Student class (model + validation)
├── student_manager.py   # CRUD, search, filter, sort logic
├── file_handler.py      # JSON read/write layer
├── exceptions.py        # Custom exception classes
├── data/
│   └── students.json    # Persisted student records (auto-created)
└── README.md
```

## Requirements

- Python 3.8+
- CLI version: no external dependencies (standard library only)
- Web GUI version: `streamlit`, `pandas` (see `requirements.txt`)

## How to Run

### CLI version
```bash
git clone <your-repo-url>
cd student_management
python main.py
```

### Web GUI version
```bash
pip install -r requirements.txt
streamlit run app.py
```
This opens the app in your browser at `http://localhost:8501`. Both the CLI
(`main.py`) and the GUI (`app.py`) share the exact same underlying logic
(`student.py`, `student_manager.py`, `file_handler.py`, `exceptions.py`) —
no duplicated code, just two different interfaces on top of it.

## Live Demo

🔗 **Deployed app:** _[add your Streamlit Cloud URL here after deploying]_

## Usage

On launch you'll see a menu:

```
1. Add Student
2. View All Students
3. Update Student
4. Delete Student
5. Search Student by Name
6. Filter by Course
7. Filter by Grade
8. Sort by Marks
9. Exit
```

Enter a number and follow the prompts. Data is automatically saved to
`data/students.json` after every change.

### Example: Adding a student
```
Enter Student ID: S001
Enter Name: Alice Sharma
Enter Age: 20
Enter Course: CS
Enter Marks: 92

✅ Student added successfully:
ID: S001 | Name: Alice Sharma | Age: 20 | Course: CS | Marks: 92.0 | Grade: A+
```

## Design Notes

| Layer | Responsibility |
|---|---|
| `student.py` | Data model + field validation (raises `InvalidInputError`) |
| `file_handler.py` | Reads/writes JSON, handles missing/corrupt files gracefully |
| `student_manager.py` | Business logic: CRUD, search, filter, sort |
| `main.py` | CLI menu, user I/O, exception display |
| `exceptions.py` | `StudentNotFoundError`, `DuplicateStudentError`, `InvalidInputError` |

Grades are auto-calculated from marks:
`A+ (90+) · A (75-89) · B (60-74) · C (40-59) · F (<40)`

## Author

Your Name — Python Development Task Submission
