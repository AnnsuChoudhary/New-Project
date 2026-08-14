# 🎓 Student Management System

## Description

A comprehensive Python-based application designed to manage student records efficiently. This application empowers users to add, update, delete, search, and manage student information while implementing industry-standard Object-Oriented Programming concepts and robust file handling mechanisms. Built with modularity, scalability, and reliability in mind.

## Key Features

### 1. **Student CRUD Operations**
   - ✅ **Create** — Add new student records with validation
   - ✅ **Read** — View all students or individual student details
   - ✅ **Update** — Modify existing student information
   - ✅ **Delete** — Remove student records from the system

### 2. **Object-Oriented Programming (OOP)**
   - `Student` model class with encapsulation and validation
   - Custom exception classes for specific error scenarios
   - Separation of concerns: Model, Manager, File Handler, and CLI layers
   - Demonstration of constructors, methods, and data validation

### 3. **File Handling**
   - Persistent storage using JSON format (`data/students.json`)
   - Automatic file creation and initialization
   - Seamless read/write operations with data integrity
   - Easy data migration and backup capabilities

### 4. **Search & Filter**
   - **Search by Name** — Find students by full or partial name matching
   - **Filter by Course** — Display all students enrolled in a specific course
   - **Filter by Grade** — View students by their grade category
   - **Sort by Marks** — Organize students based on academic performance

### 5. **Exception Handling**
   - Custom exceptions: `DuplicateStudentError`, `StudentNotFoundError`, `InvalidInputError`
   - Comprehensive error management prevents application crashes
   - User-friendly error messages for better guidance
   - Input validation at every step

### 6. **Modular Code Structure**
   - **main.py** — CLI entry point with interactive menu
   - **student.py** — Student model class with validation logic
   - **student_manager.py** — Business logic for CRUD and search operations
   - **file_handler.py** — Data persistence layer
   - **exceptions.py** — Custom exception definitions
   - **app.py** — Web GUI interface (optional Streamlit version)

## Project Structure

```
student_management/
├── app.py                 # Web GUI entry point (Streamlit)
├── main.py                # CLI entry point with interactive menu
├── student.py             # Student class (model + validation)
├── student_manager.py     # CRUD, search, filter, sort operations
├── file_handler.py        # JSON read/write persistence layer
├── exceptions.py          # Custom exception classes
├── generate_report.py     # Report generation utilities
├── requirements.txt       # Python dependencies for GUI version
├── data/
│   └── students.json      # Persisted student records (auto-created)
├── reports/               # Generated reports storage
├── screenshots/           # Project screenshots/documentation
└── README.md              # Project documentation
```

## System Requirements

- **Python** 3.8 or higher
- **CLI version** — No external dependencies (uses standard library only)
- **Web GUI version** — Additional packages: `streamlit`, `pandas` (see `requirements.txt`)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd student_management
```

### 2. Verify Python Installation
```bash
python --version
```

## How to Run

### Option 1: CLI Version (Recommended for beginners)
```bash
python main.py
```
This launches an interactive command-line menu where you can manage student records.

### Option 2: Web GUI Version
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```
This opens a web-based interface in your browser for managing students.

## Usage Guide

### CLI Menu Options:
1. **Add Student** — Enter student details (ID, name, age, course, marks)
2. **View All Students** — Display all stored student records
3. **Update Student** — Modify an existing student's information
4. **Delete Student** — Remove a student record
5. **Search by Name** — Find a student by their name
6. **Filter by Course** — View all students in a specific course
7. **Filter by Grade** — Display students by grade category
8. **Sort by Marks** — List students sorted by their marks
9. **Exit** — Close the application

## Sample Data

Students are stored in `data/students.json` in the following format:
```json
{
  "students": [
    {
      "student_id": "S001",
      "name": "John Doe",
      "age": 20,
      "course": "Computer Science",
      "marks": 85
    }
  ]
}
```

## Deliverables

✅ **Public GitHub Repository**
   - Full source code hosted on GitHub
   - Version control with git history
   - Ready for collaboration and contributions

✅ **Source Code**
   - Clean, well-documented Python code
   - Follows PEP 8 style guidelines
   - Modular and maintainable architecture
   - Comprehensive inline comments

✅ **README Documentation**
   - Complete setup and installation instructions
   - Usage guide with examples
   - Project structure overview
   - Feature description and capabilities

## Error Handling Examples

The application gracefully handles:
- Duplicate student IDs
- Missing or invalid records
- Invalid input data (empty names, negative marks, etc.)
- File I/O errors
- User input validation

## Future Enhancements

- 📊 Advanced reporting and analytics
- 🔐 User authentication and role-based access
- 💾 Database integration (SQLite, MySQL)
- 📧 Email notifications for grade updates
- 📱 Mobile application version
- 🎨 Enhanced UI/UX with modern frameworks

## Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and create pull requests.

## License

This project is open source and available under the MIT License.

## Support

For questions, issues, or suggestions, please open an issue on the GitHub repository or contact the development team.

---

**Last Updated:** 2026
**Version:** 1.0.0
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
