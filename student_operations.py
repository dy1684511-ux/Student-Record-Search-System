"""File handling and student record operations."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            students = json.load(file)
        if not isinstance(students, list):
            raise ValueError("students.json must contain a list of records")
        students.sort(key=lambda item: int(item["student_id"]))
        return students
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Could not read student data: {error}")
        return []


def save_students(students):
    students.sort(key=lambda item: int(item["student_id"]))
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)


def add_student(students, record):
    if any(int(s["student_id"]) == record["student_id"] for s in students):
        return False
    students.append(record)
    save_students(students)
    return True


def update_student(students, student_id, updated_record):
    for index, student in enumerate(students):
        if int(student["student_id"]) == student_id:
            students[index] = updated_record
            save_students(students)
            return True
    return False


def delete_student(students, student_id):
    for index, student in enumerate(students):
        if int(student["student_id"]) == student_id:
            del students[index]
            save_students(students)
            return True
    return False
