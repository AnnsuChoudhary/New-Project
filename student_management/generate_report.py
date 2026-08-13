from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
)
from PIL import Image as PILImage

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleBig", fontSize=26, leading=32, alignment=TA_CENTER,
                           spaceAfter=6, textColor=colors.HexColor("#1a1a2e")))
styles.add(ParagraphStyle(name="SubtitleC", fontSize=13, leading=18, alignment=TA_CENTER,
                           textColor=colors.HexColor("#555555"), spaceAfter=4))
styles.add(ParagraphStyle(name="SectionHead", fontSize=16, leading=20, spaceBefore=18,
                           spaceAfter=8, textColor=colors.HexColor("#16213e"),
                           fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="SubHead", fontSize=12, leading=16, spaceBefore=10,
                           spaceAfter=4, textColor=colors.HexColor("#0f3460"),
                           fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="BodyText2", fontSize=10.5, leading=15.5, spaceAfter=6,
                           alignment=4))
styles.add(ParagraphStyle(name="Caption", fontSize=9, leading=12, alignment=TA_CENTER,
                           textColor=colors.HexColor("#777777"), spaceAfter=14, spaceBefore=4))
styles.add(ParagraphStyle(name="BulletItem", fontSize=10.5, leading=15, leftIndent=16,
                           spaceAfter=3))

story = []


def img_fit(path, max_w, max_h):
    w, h = PILImage.open(path).size
    ratio = min(max_w / w, max_h / h)
    return Image(path, width=w * ratio, height=h * ratio)


# ---------- COVER PAGE ----------
story.append(Spacer(1, 1.6 * inch))
badge_table = Table([["SMS"]], colWidths=[1.1 * inch], rowHeights=[0.5 * inch])
badge_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#0f3460")),
    ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 16),
    ("ROUNDEDCORNERS", [8, 8, 8, 8]),
]))
badge_wrapper = Table([[badge_table]], colWidths=[6.4 * inch])
badge_wrapper.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER")]))
story.append(badge_wrapper)
story.append(Spacer(1, 0.25 * inch))
story.append(Paragraph("Student Management System", styles["TitleBig"]))
story.append(Paragraph("Project Report", styles["SubtitleC"]))
story.append(Spacer(1, 0.4 * inch))
story.append(Paragraph("Python Development — Task Submission", styles["SubtitleC"]))
story.append(Spacer(1, 1.8 * inch))

meta_table = Table([
    ["Technology Stack", "Python 3, Streamlit, JSON"],
    ["Interfaces", "Command-Line (CLI) + Web GUI"],
    ["Core Concepts", "OOP, File Handling, Exception Handling"],
    ["Repository Type", "Public GitHub Repository"],
], colWidths=[2.2 * inch, 3.3 * inch])
meta_table.setStyle(TableStyle([
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#0f3460")),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("LINEBELOW", (0, 0), (-1, -1), 0.5, colors.HexColor("#dddddd")),
    ("ALIGN", (0, 0), (0, -1), "LEFT"),
]))
story.append(meta_table)
story.append(PageBreak())

# ---------- 1. OBJECTIVE ----------
story.append(Paragraph("1. Objective", styles["SectionHead"]))
story.append(Paragraph(
    "The objective of this project is to develop a Python-based application that "
    "efficiently manages student records. The system allows users to add, update, "
    "delete, search, and filter student information through both a command-line "
    "interface and a web-based graphical interface, while applying core software "
    "engineering principles: Object-Oriented Programming, modular code structure, "
    "file-based persistence, and robust exception handling.",
    styles["BodyText2"]))

# ---------- 2. KEY FEATURES ----------
story.append(Paragraph("2. Key Features", styles["SectionHead"]))
features = [
    "<b>Student CRUD Operations</b> — Create, view, update, and delete student records.",
    "<b>Object-Oriented Programming</b> — A dedicated <font face='Courier'>Student</font> class encapsulates data and validation logic.",
    "<b>File Handling</b> — Records are persisted to a JSON file (<font face='Courier'>data/students.json</font>) and reloaded automatically on startup.",
    "<b>Search &amp; Filter</b> — Search by name (partial match), filter by course or grade, and sort by marks.",
    "<b>Exception Handling</b> — Custom exceptions (<font face='Courier'>StudentNotFoundError</font>, <font face='Courier'>DuplicateStudentError</font>, <font face='Courier'>InvalidInputError</font>) prevent crashes and give clear feedback.",
    "<b>Modular Code Structure</b> — Logic is separated into model, persistence, business-logic, and interface layers.",
    "<b>Dual Interface</b> — The same backend logic powers both a CLI (<font face='Courier'>main.py</font>) and a Streamlit web GUI (<font face='Courier'>app.py</font>).",
]
for f in features:
    story.append(Paragraph("•  " + f, styles["BulletItem"]))

# ---------- 3. SYSTEM ARCHITECTURE ----------
story.append(Paragraph("3. System Architecture", styles["SectionHead"]))
story.append(Paragraph(
    "The project follows a layered, modular architecture so that each file has a "
    "single responsibility. This makes the code easier to test, extend, and reuse "
    "across both interfaces.", styles["BodyText2"]))

arch_table = Table([
    ["File", "Responsibility"],
    ["student.py", "Student model class — attributes, field validation, grade calculation"],
    ["exceptions.py", "Custom exception classes for domain-specific errors"],
    ["file_handler.py", "Reads/writes student data to a JSON file; handles missing/corrupt files"],
    ["student_manager.py", "Business logic — CRUD, search, filter, sort operations"],
    ["main.py", "Command-line interface (menu-driven)"],
    ["app.py", "Web GUI interface (Streamlit) — reuses the same manager/model layer"],
], colWidths=[1.6 * inch, 4.2 * inch])
arch_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#16213e")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME", (0, 1), (0, -1), "Courier"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f5f8")]),
]))
story.append(arch_table)

story.append(Paragraph("Data Flow", styles["SubHead"]))
story.append(Paragraph(
    "Both interfaces (CLI and Web GUI) call the same <font face='Courier'>StudentManager</font> "
    "class, which validates operations, updates the in-memory list of "
    "<font face='Courier'>Student</font> objects, and persists changes to "
    "<font face='Courier'>data/students.json</font> via <font face='Courier'>FileHandler</font> "
    "after every change. This avoids duplicated logic and keeps both interfaces "
    "perfectly in sync.", styles["BodyText2"]))

story.append(Paragraph("Grading Logic", styles["SubHead"]))
story.append(Paragraph(
    "Grades are computed automatically from marks: A+ (90 and above), A (75-89), "
    "B (60-74), C (40-59), F (below 40).", styles["BodyText2"]))

story.append(PageBreak())

# ---------- 4. EXCEPTION HANDLING ----------
story.append(Paragraph("4. Exception Handling", styles["SectionHead"]))
story.append(Paragraph(
    "Three custom exception classes handle domain-specific error conditions so "
    "that the application never crashes on invalid input or missing records:",
    styles["BodyText2"]))
exc_table = Table([
    ["Exception", "Raised When"],
    ["InvalidInputError", "A field fails validation (empty name, non-numeric age/marks, out-of-range values)"],
    ["DuplicateStudentError", "An Add operation uses a Student ID that already exists"],
    ["StudentNotFoundError", "A lookup, update, delete, or search finds no matching record"],
], colWidths=[1.9 * inch, 3.9 * inch])
exc_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#16213e")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTNAME", (0, 1), (0, -1), "Courier"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f5f8")]),
]))
story.append(exc_table)
story.append(Spacer(1, 8))
story.append(Paragraph(
    "In both the CLI and GUI, these exceptions are caught at the interface layer "
    "and shown as a clear, user-facing message instead of a raw traceback.",
    styles["BodyText2"]))

# ---------- 5. WORKING SCREENS ----------
story.append(Paragraph("5. Working Screens", styles["SectionHead"]))

story.append(Paragraph("5.1 Command-Line Interface", styles["SubHead"]))
story.append(Paragraph(
    "The CLI provides a numbered menu covering all core operations. Below is an "
    "actual run showing the menu and the &quot;View All Students&quot; output.",
    styles["BodyText2"]))
story.append(img_fit("screenshots/0_cli_terminal.png", 5.8 * inch, 4.3 * inch))
story.append(Paragraph("Figure 1 — CLI menu and student list output", styles["Caption"]))

story.append(PageBreak())

story.append(Paragraph("5.2 Web GUI — Add Student", styles["SubHead"]))
story.append(img_fit("screenshots/1_add_student.png", 6.0 * inch, 4.2 * inch))
story.append(Paragraph("Figure 2 — Add Student form (Streamlit web interface)", styles["Caption"]))

story.append(Paragraph("5.3 Web GUI — View All Students", styles["SubHead"]))
story.append(img_fit("screenshots/2_view_all.png", 6.0 * inch, 4.0 * inch))
story.append(Paragraph("Figure 3 — All student records displayed in a live data table", styles["Caption"]))

story.append(PageBreak())

story.append(Paragraph("5.4 Web GUI — Update Student", styles["SubHead"]))
story.append(img_fit("screenshots/6_update.png", 6.0 * inch, 4.2 * inch))
story.append(Paragraph("Figure 4 — Update form pre-filled with the selected student's current data", styles["Caption"]))

story.append(Paragraph("5.5 Web GUI — Delete Student", styles["SubHead"]))
story.append(img_fit("screenshots/7_delete.png", 6.0 * inch, 3.2 * inch))
story.append(Paragraph("Figure 5 — Delete Student screen", styles["Caption"]))

story.append(PageBreak())

story.append(Paragraph("5.6 Web GUI — Search", styles["SubHead"]))
story.append(img_fit("screenshots/3_search.png", 6.0 * inch, 3.0 * inch))
story.append(Paragraph("Figure 6 — Search by name", styles["Caption"]))

story.append(Paragraph("5.7 Web GUI — Filter", styles["SubHead"]))
story.append(img_fit("screenshots/4_filter.png", 6.0 * inch, 3.0 * inch))
story.append(Paragraph("Figure 7 — Filter by course and grade", styles["Caption"]))

story.append(Paragraph("5.8 Web GUI — Sort by Marks", styles["SubHead"]))
story.append(img_fit("screenshots/5_sort.png", 6.0 * inch, 4.2 * inch))
story.append(Paragraph("Figure 8 — Students sorted by marks (high to low)", styles["Caption"]))

story.append(PageBreak())

# ---------- 6. DEPLOYMENT ----------
story.append(Paragraph("6. Deployment", styles["SectionHead"]))
story.append(Paragraph(
    "The web GUI (app.py) is deployed on Streamlit Community Cloud, a free hosting "
    "platform for Streamlit applications that deploys directly from a GitHub "
    "repository.", styles["BodyText2"]))
story.append(Paragraph("Live application link:", styles["SubHead"]))
story.append(Paragraph(
    "<font color='#0f3460'><u>[Add your deployed Streamlit Cloud URL here]</u></font>",
    styles["BodyText2"]))
story.append(Paragraph("GitHub repository link:", styles["SubHead"]))
story.append(Paragraph(
    "<font color='#0f3460'><u>[Add your public GitHub repository URL here]</u></font>",
    styles["BodyText2"]))

# ---------- 7. CHALLENGES ----------
story.append(Paragraph("7. Challenges &amp; Solutions", styles["SectionHead"]))
challenges = [
    ("Keeping CLI and GUI in sync",
     "Solved by putting all business logic in student_manager.py and having both "
     "main.py and app.py call the same methods, rather than duplicating logic."),
    ("Preventing crashes on bad input",
     "Solved with field-level validation inside the Student class and custom "
     "exceptions caught at the interface layer."),
    ("Handling corrupted or missing data files",
     "FileHandler catches FileNotFoundError and JSONDecodeError and falls back "
     "to an empty record set instead of crashing."),
]
for title, desc in challenges:
    story.append(Paragraph(title, styles["SubHead"]))
    story.append(Paragraph(desc, styles["BodyText2"]))

# ---------- 8. CONCLUSION ----------
story.append(Paragraph("8. Conclusion", styles["SectionHead"]))
story.append(Paragraph(
    "The Student Management System successfully meets all specified requirements: "
    "full CRUD functionality, Object-Oriented design, persistent file-based storage, "
    "search and filter capabilities, and comprehensive exception handling — all "
    "within a clean, modular code structure. The addition of a Streamlit-based web "
    "GUI alongside the original CLI demonstrates that the same core logic can "
    "reliably power multiple interfaces, and the project is deployed live for "
    "easy access and demonstration.", styles["BodyText2"]))

story.append(Spacer(1, 20))
story.append(Paragraph("— End of Report —", styles["SubtitleC"]))

doc = SimpleDocTemplate(
    "reports/Student_Management_System_Report.pdf",
    pagesize=A4,
    topMargin=0.7 * inch,
    bottomMargin=0.7 * inch,
    leftMargin=0.8 * inch,
    rightMargin=0.8 * inch,
    title="Student Management System - Project Report",
)
doc.build(story)
print("PDF generated successfully")
