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


st.title("🎓 Student Management System")
st.caption("Python OOP • File Handling • Exception Handling • Search & Filter")

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
            student_id = st.text_input("Student ID")
            age = st.text_input("Age")
            marks = st.text_input("Marks")
        with col2:
            name = st.text_input("Name")
            course = st.text_input("Course")
        submitted = st.form_submit_button("Add Student", type="primary")

        if submitted:
            try:
                student = manager.add_student(student_id, name, age, course, marks)
                st.success(f"✅ Added: {student}")
            except (InvalidInputError, DuplicateStudentError) as e:
                st.error(f"❌ {e}")

# ---------- View All ----------
with tabs[1]:
    st.subheader("All Students")
    students = manager.list_all()
    st.dataframe(students_to_df(students), width='stretch', hide_index=True)
    st.caption(f"Total: {len(students)} student(s)")

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
                new_age = st.text_input("Age", value=str(current.age))
            with col2:
                new_course = st.text_input("Course", value=current.course)
                new_marks = st.text_input("Marks", value=str(current.marks))
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
    keyword = st.text_input("Enter name or part of it")
    if keyword:
        try:
            results = manager.search_by_name(keyword)
            st.dataframe(students_to_df(results), width='stretch', hide_index=True)
        except StudentNotFoundError as e:
            st.warning(f"⚠️ {e}")

# ---------- Filter ----------
with tabs[5]:
    st.subheader("Filter Students")
    col1, col2 = st.columns(2)
    with col1:
        course_filter = st.text_input("Filter by course (e.g. CS)")
        if course_filter:
            results = manager.filter_by_course(course_filter)
            st.write(f"**{len(results)} result(s) in {course_filter.upper()}**")
            st.dataframe(students_to_df(results), width='stretch', hide_index=True)
    with col2:
        grade_filter = st.selectbox("Filter by grade", ["", "A+", "A", "B", "C", "F"])
        if grade_filter:
            results = manager.filter_by_grade(grade_filter)
            st.write(f"**{len(results)} result(s) with Grade {grade_filter}**")
            st.dataframe(students_to_df(results), width='stretch', hide_index=True)

# ---------- Sort ----------
with tabs[6]:
    st.subheader("Sort by Marks")
    order = st.radio("Order", ["High to Low", "Low to High"], horizontal=True)
    results = manager.sort_by_marks(descending=(order == "High to Low"))
    st.dataframe(students_to_df(results), width='stretch', hide_index=True)

st.divider()
st.caption("Student Management System — built with Python, OOP, and Streamlit")
