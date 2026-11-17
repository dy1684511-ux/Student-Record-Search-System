"""Student Record Search System - DAA project using Binary Search."""
from binary_search import binary_search_student
from student_operations import load_students, save_students, add_student, update_student, delete_student


def read_int(message):
    while True:
        try:
            return int(input(message).strip())
        except ValueError:
            print("Please enter a valid whole number.")


def read_float(message):
    while True:
        try:
            value = float(input(message).strip())
            if 0 <= value <= 100:
                return value
            print("Enter a value between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def read_text(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty.")


def print_student(student):
    print("\n--------------- STUDENT DETAILS ---------------")
    print(f"Student ID : {student['student_id']}")
    print(f"Name       : {student['name']}")
    print(f"Course     : {student['course']}")
    print(f"Department : {student['department']}")
    print(f"Semester   : {student['semester']}")
    print(f"Marks      : {student['marks']}")
    print(f"CGPA       : {student['cgpa']}")
    print("------------------------------------------------")


def get_record(student_id=None):
    if student_id is None:
        student_id = read_int("Enter Student ID: ")
    return {
        "student_id": student_id,
        "name": read_text("Enter student name: "),
        "course": read_text("Enter course (e.g. MCA): "),
        "department": read_text("Enter department: "),
        "semester": read_int("Enter semester: "),
        "marks": read_float("Enter marks (0-100): "),
        "cgpa": read_float("Enter CGPA (0-10): ") if False else None,
    }


def read_cgpa():
    while True:
        try:
            value = float(input("Enter CGPA (0-10): ").strip())
            if 0 <= value <= 10:
                return value
            print("CGPA must be between 0 and 10.")
        except ValueError:
            print("Please enter a valid number.")


def create_record(student_id=None):
    if student_id is None:
        student_id = read_int("Enter Student ID: ")
    return {
        "student_id": student_id,
        "name": read_text("Enter student name: "),
        "course": read_text("Enter course (e.g. MCA): "),
        "department": read_text("Enter department: "),
        "semester": read_int("Enter semester: "),
        "marks": read_float("Enter marks (0-100): "),
        "cgpa": read_cgpa(),
    }


def search_student(students):
    target_id = read_int("Enter Student ID to search: ")
    student, comparisons, trace = binary_search_student(students, target_id)
    print("\nBinary Search steps:")
    for step_number, step in enumerate(trace, start=1):
        print(f"{step_number}. {step}")
    print(f"Total comparisons: {comparisons}")
    if student:
        print_student(student)
    else:
        print("Student record not found.")


def view_students(students):
    if not students:
        print("No student records available.")
        return
    print("\nSTUDENT RECORDS (sorted by Student ID)")
    print("ID\tName\t\tCourse\tSemester\tMarks\tCGPA")
    print("-" * 72)
    for s in students:
        print(f"{s['student_id']}\t{s['name']:<16}\t{s['course']:<12}\t{s['semester']}\t\t{s['marks']}\t{s['cgpa']}")
    print(f"\nTotal students: {len(students)}")


def main():
    students = load_students()
    while True:
        print("\n========== STUDENT RECORD SEARCH SYSTEM ==========")
        print("1. Add Student Record")
        print("2. View All Student Records")
        print("3. Search Student by ID (Binary Search)")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Exit")
        print("==================================================")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            record = create_record()
            if add_student(students, record):
                print("Student record added and saved successfully.")
            else:
                print("This Student ID already exists. Use a unique ID.")
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            student_id = read_int("Enter Student ID to update: ")
            existing, _, _ = binary_search_student(students, student_id)
            if existing:
                print("Enter the updated details:")
                updated = create_record(student_id)
                update_student(students, student_id, updated)
                print("Student record updated successfully.")
            else:
                print("Student record not found.")
        elif choice == "5":
            student_id = read_int("Enter Student ID to delete: ")
            if delete_student(students, student_id):
                print("Student record deleted successfully.")
            else:
                print("Student record not found.")
        elif choice == "6":
            save_students(students)
            print("Your records are saved. Thank you!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
