import mysql.connector

conn = mysql.connector.connect(host="localhost",user="user1",password="123")
cursor = conn.cursor()

print("Enter \'create\' to create a new record")
print("Enter \'display\' to display the records")
print("Enter \'quit\' to quit program")

while True:
    a = input("Enter your choice: ")

    if a == "create":
        cursor.execute("CREATE DATABASE IF NOT EXISTS school")
        cursor.execute("USE school")
        
        cursor.execute("""
CREATE TABLE IF NOT EXISTS student (Rollno INT PRIMARY KEY,
Stu_Name VARCHAR(50), Stream VARCHAR(50), Percentage FLOAT)""")
        
        records = [
            (1, "A", "Math", 82.2),
            (2, "B", "CS", 77.6),
            (3, "C", "Biology", 96.8),
            (4, "D", "CS", 97.2),
            (5, "E", "Biology", 78.5)
        ]
        
        cursor.executemany("INSERT INTO student (Rollno, Stu_Name, Stream, Percentage) VALUES (%s, %s, %s, %s)", records)
        conn.commit()

    elif a == "display":
        cursor.execute("USE school")
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        for row in rows:
            print(f"Rollno: {row[0]}, Name: {row[1]}, Stream: {row[2]}, Percentage: {row[3]}")

    elif a == "quit":
        print("quitting..")
        break
    else:
        print("Invalid input")

cursor.close()
conn.close()