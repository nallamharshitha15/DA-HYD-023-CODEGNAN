# DATA ANALYST BATCH
# STUDENT ATTENDANCE & PERFORMANCE SYSTEM
import datetime
import os
students = {}
#INPUT FUNCTION 
def get_integer(message):
    """indentifing is it ing or string"""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")
#ADD STUDENT
def add_student():
    """adding student info"""
    sid = get_integer("Enter Student ID: ")
    if sid in students:
        print("Student ID already exists!")
        return
    name = input("Enter Student Name: ").strip()
    if not name or not name.replace(" ", "").isalpha():
        print("Invalid name!")
        return
    students[sid] = {
        "name": name,
        "batch": "Data Analyst",
        "attendance": {"total": 0, "attended": 0},
        "marks": {}
    }
    print("Student added successfully!")
#SELECT STUDENT
def select_student():
    """talking student info"""
    if not students:
        print("No students available!")
        return None
    choice = input("Search by 1.ID or 2.Name: ")
    if choice == "1":
        sid = get_integer("Enter ID: ")
        return sid if sid in students else None
    if choice == "2":
        name = input("Enter Name: ").strip().lower()
        found = [sid for sid in students
                 if students[sid]["name"].lower() == name]
        if len(found) == 1:
            return found[0]
        if len(found) > 1:
            print("Multiple students found:")
            for sid in found:
                print(sid, students[sid]["name"])
            sid = get_integer("Enter correct ID: ")
            return sid if sid in found else None
    print("Invalid selection!")
    return None
#ATTENDANCE 
def attendance(sid):
    """ taking student attendance"""
    total = get_integer("Total classes conducted: ")
    if total <= 0:
        print("Total classes must be greater than 0.")
        return
    attended = get_integer("Classes attended: ")
    if not 0 <= attended <= total:
        print("Invalid attended classes!")
        return
    students[sid]["attendance"] = {
        "total": total,
        "attended": attended
    }
    percent = attended / total * 100
    print(f"Attendance: {percent:.2f}%")
#ATTENDANCE PERCENTAGE 
def attendance_percentage(sid):
    """student attendance_percentage showing"""
    data = students[sid]["attendance"]
    if data["total"] == 0:
        print("Attendance not recorded!")
        return
    percent = data["attended"] / data["total"] * 100
    absent = data["total"] - data["attended"]
    print(f"Total Classes : {data['total']}")
    print(f"Attended      : {data['attended']}")
    print(f"Absent        : {absent}")
    print(f"Percentage    : {percent:.2f}%")
# SUBJECT MARKS 
def subject_marks(sid):
    subjects = ["Python", "MySQL", "Power BI"]
    for subject in subjects:
        while True:
            mark = get_integer(f"Enter {subject} marks: ")
            if 0 <= mark <= 100:
                students[sid]["marks"][subject] = mark
                break
            print("Marks must be between 0 and 100.")
    print("Marks saved successfully!")
# PERFORMANCE 
def performance(sid):
    """understanding student performance"""
    marks = students[sid]["marks"]
    if len(marks) != 3:
        print("Enter all subject marks first!")
        return
    print("\nSubject Performance:")
    for subject, mark in marks.items():
        print(f"{subject}: {mark}/100 -> {mark:.2f}%")
    total = sum(marks.values())
    average = total / 3
    highest = max(marks, key=marks.get)
    lowest = min(marks, key=marks.get)
    if average >= 90:
        category = "Excellent"
    elif average >= 75:
        category = "Very Good"
    elif average >= 60:
        category = "Good"
    elif average >= 40:
        category = "Average"
    else:
        category = "Poor"

    print(f"\nTotal       : {total}/300")
    print(f"Average     : {average:.2f}%")
    print(f"Strongest   : {highest} ({marks[highest]}%)")
    print(f"Weakest     : {lowest} ({marks[lowest]}%)")
    print(f"Category    : {category}")
# LOW ATTENDANCE 
def low_attendance():
    """stundet low-attendance"""
    found = [
        (sid, students[sid]["name"],
         students[sid]["attendance"]["attended"] /
         students[sid]["attendance"]["total"] * 100)
        for sid in students
        if students[sid]["attendance"]["total"] > 0
        and students[sid]["attendance"]["attended"] /
        students[sid]["attendance"]["total"] * 100 < 75
    ]
    if not found:
        print("No low attendance students.")
        return
    for sid, name, percent in found:
        print(f"{sid} | {name} | {percent:.2f}%")
# LOW PERFORMANCE 
def low_performance():
    """student low-perfromance"""
    found = []
    for sid in students:
        marks = students[sid]["marks"]

        if len(marks) == 3:
            average = sum(marks.values()) / 3

            if average < 50:
                found.append((sid, students[sid]["name"], average))
    if not found:
        print("No low-performing students.")
        return

    for sid, name, average in found:
        print(f"{sid} | {name} | {average:.2f}%")
#RANKING 
def ranking():
    """creating student ranking"""
    data = []
    for sid in students:
        marks = students[sid]["marks"]
        if len(marks) == 3:
            average = sum(marks.values()) / 3
            data.append((sid, students[sid]["name"], average))
    if not data:
        print("No complete marks available.")
        return
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][2] < data[j][2]:
                data[i], data[j] = data[j], data[i]
    for rank, student in enumerate(data, 1):
        print(
            f"Rank {rank}: "
            f"{student[0]} | {student[1]} | "
            f"{student[2]:.2f}%"
        )
#SAVE REPORT 
def save_report():
    """saving studnet report in .txt file"""
    if not students:
        print("No data to save!")
        return
    try:
        with open("DA_Batch_Report.txt", "w", encoding="utf-8") as file:

            file.write("DATA ANALYST BATCH REPORT\n")
            file.write(
                f"Date: {datetime.date.today()}\n\n")

            for sid, student in students.items():

                file.write(
                    f"ID: {sid} | Name: {student['name']}\n")

                att = student["attendance"]

                if att["total"] > 0:
                    percent = (
                        att["attended"] /
                        att["total"] * 100
                    )
                    file.write(
                        f"Attendance: {percent:.2f}%\n"
                    )

                marks = student["marks"]

                for subject, mark in marks.items():
                    file.write(
                        f"{subject}: {mark}/100\n"
                    )

                if len(marks) == 3:
                    average = sum(marks.values()) / 3
                    file.write(
                        f"Average: {average:.2f}%\n"
                    )

                file.write("-" * 30 + "\n")

        if os.path.exists("DA_Batch_Report.txt"):
            print("Report saved successfully!")

    except OSError as error:
        print("File error:", error)
#STUDENT MENU
def student_menu(sid):
    while True:
        print(f"\n--- {students[sid]['name']} ---")
        print("1. Attendance")
        print("2. Attendance Percentage")
        print("3. Subject Marks")
        print("4. Performance")
        print("5. Back")
        choice = input("Enter choice: ")
        if choice == "1":
            attendance(sid)
        elif choice == "2":
            attendance_percentage(sid)
        elif choice == "3":
            subject_marks(sid)
        elif choice == "4":
            performance(sid)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
#MAIN MENU 
while True:
    print("\n===== DATA ANALYST BATCH =====")
    print("1. Add Student")
    print("2. Select Student")
    print("3. Low Attendance")
    print("4. Low Performance")
    print("5. Student Ranking")
    print("6. Save Report")
    print("7. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        sid = select_student()
        if sid is not None:
            student_menu(sid)
    elif choice == "3":
        low_attendance()
    elif choice == "4":
        low_performance()
    elif choice == "5":
        ranking()
    elif choice == "6":
        save_report()
    elif choice == "7":
        print("System closed.")
        break
    else:
        print("Invalid choice!")
