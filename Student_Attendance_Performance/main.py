
# DATA ANALYST BATCH
# STUDENT ATTENDANCE & PERFORMANCE SYSTEM

from database import get_connection
import datetime
import os


# INPUT FUNCTION
def get_integer(message):
    """Identifying integer input"""

    while True:
        try:
            return int(input(message))

        except ValueError:
            print("Please enter a valid number.")


# ADD STUDENT
def add_student():
    """Adding student information to MySQL"""

    sid = get_integer("Enter Student ID: ")

    name = input("Enter Student Name: ").strip()

    if not name or not name.replace(" ", "").isalpha():
        print("Invalid name!")
        return

    con = get_connection()
    cursor = con.cursor()

    try:
        query = """
        INSERT INTO students
        (student_id, student_name, batch)
        VALUES (%s, %s, %s)
        """

        values = (sid, name, "Data Analyst")

        cursor.execute(query, values)
        con.commit()

        print("Student added successfully!")

    except Exception as error:
        con.rollback()
        print("Error:", error)

    finally:
        cursor.close()
        con.close()


# SELECT STUDENT
def select_student():
    """Selecting student by ID or Name"""

    con = get_connection()
    cursor = con.cursor()

    try:
        choice = input("Search by 1.ID or 2.Name: ")

        if choice == "1":

            sid = get_integer("Enter ID: ")

            cursor.execute(
                "SELECT student_id FROM students WHERE student_id = %s",
                (sid,)
            )

            result = cursor.fetchone()

            if result:
                return result[0]

            print("Student not found!")

        elif choice == "2":

            name = input("Enter Name: ").strip()

            cursor.execute(
                """
                SELECT student_id, student_name
                FROM students
                WHERE LOWER(student_name) = LOWER(%s)
                """,
                (name,)
            )

            results = cursor.fetchall()

            if len(results) == 1:
                return results[0][0]

            elif len(results) > 1:

                print("Multiple students found:")

                for row in results:
                    print(row[0], row[1])

                sid = get_integer("Enter correct ID: ")

                if any(row[0] == sid for row in results):
                    return sid

                print("Invalid Student ID!")

            else:
                print("Student not found!")

        else:
            print("Invalid selection!")

        return None

    finally:
        cursor.close()
        con.close()


# ATTENDANCE
def attendance(sid):
    """Recording student attendance"""

    total = get_integer("Total classes conducted: ")

    if total <= 0:
        print("Total classes must be greater than 0.")
        return

    attended = get_integer("Classes attended: ")

    if not 0 <= attended <= total:
        print("Invalid attended classes!")
        return

    con = get_connection()
    cursor = con.cursor()

    try:
        query = """
        INSERT INTO attendance
        (student_id, total_classes, attended_classes)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
        total_classes = %s,
        attended_classes = %s
        """

        values = (sid, total, attended, total, attended)

        cursor.execute(query, values)
        con.commit()

        percent = attended / total * 100

        print("Attendance saved successfully!")
        print(f"Attendance: {percent:.2f}%")

    except Exception as error:
        con.rollback()
        print("Error:", error)

    finally:
        cursor.close()
        con.close()


# ATTENDANCE PERCENTAGE
def attendance_percentage(sid):
    """Displaying student attendance percentage"""

    con = get_connection()
    cursor = con.cursor()

    try:
        query = """
        SELECT total_classes, attended_classes
        FROM attendance
        WHERE student_id = %s
        """

        cursor.execute(query, (sid,))
        data = cursor.fetchone()

        if data is None:
            print("Attendance not recorded!")
            return

        total, attended = data

        if total == 0:
            print("Attendance not recorded!")
            return

        absent = total - attended
        percent = attended / total * 100

        print("\nAttendance Details")
        print("Total Classes :", total)
        print("Attended      :", attended)
        print("Absent        :", absent)
        print(f"Percentage    : {percent:.2f}%")

    finally:
        cursor.close()
        con.close()


# SUBJECT MARKS
def subject_marks(sid):
    """Entering subject marks"""

    subjects = ["Python", "MySQL", "Power BI"]

    con = get_connection()
    cursor = con.cursor()

    try:
        for subject in subjects:

            while True:
                mark = get_integer(f"Enter {subject} marks: ")

                if 0 <= mark <= 100:
                    break

                print("Marks must be between 0 and 100.")

            query = """
            INSERT INTO marks
            (student_id, subject, marks)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE marks = %s
            """

            values = (sid, subject, mark, mark)

            cursor.execute(query, values)

        con.commit()

        print("Marks saved successfully!")

    except Exception as error:
        con.rollback()
        print("Error:", error)

    finally:
        cursor.close()
        con.close()


# PERFORMANCE
def performance(sid):
    """Understanding student performance"""

    con = get_connection()
    cursor = con.cursor()

    try:
        query = """
        SELECT subject, marks
        FROM marks
        WHERE student_id = %s
        """

        cursor.execute(query, (sid,))
        rows = cursor.fetchall()

        if len(rows) != 3:
            print("Enter all subject marks first!")
            return

        marks = {}

        print("\nSubject Performance:")

        for subject, mark in rows:
            marks[subject] = mark

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

    finally:
        cursor.close()
        con.close()


# LOW ATTENDANCE
def low_attendance():
    """Finding students with attendance below 75%"""

    con = get_connection()
    cursor = con.cursor()

    try:
        query = """
        SELECT
            s.student_id,
            s.student_name,
            ROUND(
                a.attended_classes * 100.0 /
                a.total_classes, 2
            ) AS attendance_percentage
        FROM students s
        INNER JOIN attendance a
        ON s.student_id = a.student_id
        WHERE a.total_classes > 0
        AND a.attended_classes * 100.0 /
            a.total_classes < 75
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print("No low attendance students.")
            return

        print("\nLow Attendance Students")

        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]:.2f}%")

    finally:
        cursor.close()
        con.close()


# LOW PERFORMANCE
def low_performance():
    """Finding students with average marks below 50"""

    con = get_connection()
    cursor = con.cursor()

    try:
        query = """
        SELECT
            s.student_id,
            s.student_name,
            ROUND(AVG(m.marks), 2) AS average_marks
        FROM students s
        INNER JOIN marks m
        ON s.student_id = m.student_id
        GROUP BY s.student_id, s.student_name
        HAVING COUNT(m.subject) = 3
        AND AVG(m.marks) < 50
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print("No low-performing students.")
            return

        print("\nLow Performance Students")

        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]}%")

    finally:
        cursor.close()
        con.close()


# STUDENT RANKING
def ranking():
    """Creating student ranking"""

    con = get_connection()
    cursor = con.cursor()

    try:
        query = """
        SELECT
            s.student_id,
            s.student_name,
            ROUND(AVG(m.marks), 2) AS average_marks
        FROM students s
        INNER JOIN marks m
        ON s.student_id = m.student_id
        GROUP BY s.student_id, s.student_name
        HAVING COUNT(m.subject) = 3
        ORDER BY average_marks DESC
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print("No complete marks available.")
            return

        print("\nStudent Ranking")

        for rank, row in enumerate(rows, 1):

            print(
                f"Rank {rank}: "
                f"{row[0]} | {row[1]} | {row[2]}%"
            )

    finally:
        cursor.close()
        con.close()


# SAVE REPORT
def save_report():
    """Saving student report in TXT file"""

    con = get_connection()
    cursor = con.cursor()

    try:
        cursor.execute(
            "SELECT student_id, student_name FROM students"
        )

        students = cursor.fetchall()

        if not students:
            print("No data to save!")
            return

        with open(
            "DA_Batch_Report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write("DATA ANALYST BATCH REPORT\n")
            file.write(
                f"Date: {datetime.date.today()}\n\n"
            )

            for sid, name in students:

                file.write(
                    f"ID: {sid} | Name: {name}\n"
                )

                # Attendance details
                cursor.execute(
                    """
                    SELECT total_classes, attended_classes
                    FROM attendance
                    WHERE student_id = %s
                    """,
                    (sid,)
                )

                att = cursor.fetchone()

                if att and att[0] > 0:

                    total, attended = att
                    percent = attended / total * 100

                    file.write(
                        f"Attendance: {percent:.2f}%\n"
                    )

                # Subject marks
                cursor.execute(
                    """
                    SELECT subject, marks
                    FROM marks
                    WHERE student_id = %s
                    """,
                    (sid,)
                )

                marks = cursor.fetchall()
                total_marks = 0

                for subject, mark in marks:

                    total_marks += mark

                    file.write(
                        f"{subject}: {mark}/100\n"
                    )

                if len(marks) == 3:

                    average = total_marks / 3

                    file.write(
                        f"Average: {average:.2f}%\n"
                    )

                file.write("-" * 30 + "\n")

        if os.path.exists("DA_Batch_Report.txt"):
            print("Report saved successfully!")

    except OSError as error:
        print("File error:", error)

    finally:
        cursor.close()
        con.close()


# STUDENT MENU
def student_menu(sid):

    con = get_connection()
    cursor = con.cursor()

    try:
        cursor.execute(
            """
            SELECT student_name
            FROM students
            WHERE student_id = %s
            """,
            (sid,)
        )

        result = cursor.fetchone()

    finally:
        cursor.close()
        con.close()

    if result is None:
        print("Student not found!")
        return

    student_name = result[0]

    while True:

        print(f"\n--- {student_name} ---")
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


# MAIN MENU
def main():

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

        try:

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

        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
