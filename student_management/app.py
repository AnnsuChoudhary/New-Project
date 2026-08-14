"""
Student Management System - Web GUI (Streamlit)
Reuses the same StudentManager / Student / FileHandler / exceptions
as the CLI (main.py) — no duplicated business logic.

Run locally with: streamlit run app.py
"""

import streamlit as st
import pandas as pd

from student_manager import StudentManager
from exceptions import StudentNotFoundError, DuplicateStudentError, InvalidInputError

st.set_page_config(page_title="Student Management System", page_icon="🎓", layout="wide")

GRADE_COLORS = {
    "A+": "#1e824c", "A": "#2ecc71", "B": "#f1c40f",
    "C": "#e67e22", "F": "#e74c3c",
}

# ---------- Init ----------
if "manager" not in st.session_state:
    st.session_state.manager = StudentManager()

manager = st.session_state.manager


def students_to_df(students):
    if not students:
        return pd.DataFrame(columns=["ID", "Name", "Age", "Course", "Marks", "Grade"])
    return pd.DataFrame([{
        "ID": s.student_id,
        "Name": s.name,
        "Age": s.age,
        "Course": s.course,
        "Marks": s.marks,
        "Grade": s.grade(),
    } for s in students])


def show_table(students, empty_message="No records found."):
    if not students:
        st.info(empty_message)
        return
    df = students_to_df(students)

    def color_grade(val):
        color = GRADE_COLORS.get(val, "#888888")
        return f"background-color: {color}22; color: {color}; font-weight: 600;"

    styled = df.style.map(color_grade, subset=["Grade"]).format({"Marks": "{:.1f}"})
    st.dataframe(
        styled,
        width='stretch',
        hide_index=True,
    )
    st.caption(f"Total: {len(students)} student(s)")


st.title("🎓 Student Management System")
st.caption("Python OOP • File Handling • Exception Handling • Search & Filter")

# ---------- Dashboard metrics ----------
all_students = manager.list_all()
m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Students", len(all_students))
if all_students:
    avg_marks = sum(s.marks for s in all_students) / len(all_students)
    top_course = max(
        {s.course for s in all_students},
        key=lambda c: sum(1 for s in all_students if s.course == c)
    )
    top_scorer = max(all_students, key=lambda s: s.marks)
    m2.metric("Average Marks", f"{avg_marks:.1f}")
    m3.metric("Most Popular Course", top_course)
    m4.metric("Top Scorer", f"{top_scorer.name.split()[0]} ({top_scorer.marks:.0f})")
else:
    m2.metric("Average Marks", "—")
    m3.metric("Most Popular Course", "—")
    m4.metric("Top Scorer", "—")

st.divider()

tabs = st.tabs([
    "➕ Add", "📋 View All", "✏️ Update", "🗑️ Delete",
    "🔍 Search", "🎯 Filter", "↕️ Sort"
])

# ---------- Add ----------
with tabs[0]:
    st.subheader("Add New Student")
    with st.form("add_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            student_id = st.text_input("Student ID", placeholder="e.g. S001")
            age = st.number_input("Age", min_value=3, max_value=100, value=18, step=1)
            marks = st.number_input("Marks", min_value=0.0, max_value=100.0, value=0.0, step=0.5)
        with col2:
            name = st.text_input("Name", placeholder="e.g. Alice Sharma")
            course = st.text_input("Course", placeholder="e.g. CS")
        submitted = st.form_submit_button("Add Student", type="primary")

        if submitted:
            try:
                student = manager.add_student(student_id, name, age, course, marks)
                st.success(f"✅ Added: {student}")
                st.rerun()
            except (InvalidInputError, DuplicateStudentError) as e:
                st.error(f"❌ {e}")

# ---------- View All ----------
with tabs[1]:
    st.subheader("All Students")
    show_table(manager.list_all(), empty_message="No students yet — add one from the ➕ Add tab.")

# ---------- Update ----------
with tabs[2]:
    st.subheader("Update Student")
    all_ids = [s.student_id for s in manager.list_all()]
    if not all_ids:
        st.info("No students to update yet.")
    else:
        sel_id = st.selectbox("Select Student ID", all_ids)
        current = manager.find_by_id(sel_id)
        with st.form("update_form"):
            col1, col2 = st.columns(2)
            with col1:
                new_name = st.text_input("Name", value=current.name)
                new_age = st.number_input("Age", min_value=3, max_value=100, value=current.age, step=1)
            with col2:
                new_course = st.text_input("Course", value=current.course)
                new_marks = st.number_input("Marks", min_value=0.0, max_value=100.0, value=float(current.marks), step=0.5)
            update_submitted = st.form_submit_button("Update Student", type="primary")

            if update_submitted:
                try:
                    student = manager.update_student(
                        sel_id, name=new_name, age=new_age,
                        course=new_course, marks=new_marks
                    )
                    st.success(f"✅ Updated: {student}")
                    st.rerun()
                except (StudentNotFoundError, InvalidInputError) as e:
                    st.error(f"❌ {e}")

# ---------- Delete ----------
with tabs[3]:
    st.subheader("Delete Student")
    all_ids = [s.student_id for s in manager.list_all()]
    if not all_ids:
        st.info("No students to delete yet.")
    else:
        del_id = st.selectbox("Select Student ID to delete", all_ids, key="del_select")
        st.warning(f"You're about to permanently delete student **{del_id}**.")
        if st.button("🗑️ Delete Student", type="primary"):
            try:
                student = manager.delete_student(del_id)
                st.success(f"✅ Deleted: {student}")
                st.rerun()
            except StudentNotFoundError as e:
                st.error(f"❌ {e}")

# ---------- Search ----------
with tabs[4]:
    st.subheader("Search by Name")
    keyword = st.text_input("Enter name or part of it", placeholder="e.g. alice")
    if keyword:
        try:
            results = manager.search_by_name(keyword)
            show_table(results)
        except StudentNotFoundError as e:
            st.warning(f"⚠️ {e}")
    else:
        st.caption("Start typing to search.")

# ---------- Filter ----------
with tabs[5]:
    st.subheader("Filter Students")
    col1, col2 = st.columns(2)
    with col1:
        course_filter = st.text_input("Filter by course", placeholder="e.g. CS")
        if course_filter:
            results = manager.filter_by_course(course_filter)
            st.write(f"**{len(results)} result(s) in {course_filter.upper()}**")
            show_table(results)
    with col2:
        grade_filter = st.selectbox("Filter by grade", ["", "A+", "A", "B", "C", "F"])
        if grade_filter:
            results = manager.filter_by_grade(grade_filter)
            st.write(f"**{len(results)} result(s) with Grade {grade_filter}**")
            show_table(results)

# ---------- Sort ----------
with tabs[6]:
    st.subheader("Sort by Marks")
    order = st.radio("Order", ["High to Low", "Low to High"], horizontal=True)
    results = manager.sort_by_marks(descending=(order == "High to Low"))
    show_table(results)

st.divider()
st.caption("Student Management System — built with Python, OOP, and Streamlit")