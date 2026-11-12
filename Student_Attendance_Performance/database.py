
import mysql.connector

def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Harshitha@123",
        database="student_management"
    )

    return connection


try:
    con = get_connection()
    print("MySQL connected successfully!")
    con.close()

except mysql.connector.Error as error:
    print("Connection error:", error)
