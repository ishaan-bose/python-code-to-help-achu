import mysql.connector

conn = mysql.connector.connect(host="localhost",user="user1",password="123")
cursor = conn.cursor()

print("Enter \'create\' to create a new record")
print("Enter \'display\' to display the records")
print("Enter \'update\' to update salary of manager")
print("Enter \'delete\' to delete record of employee based on id")
print("Enter \'quit\' to quit program")

while True:
    a = input("Enter choice: ")

    if a == "create":
        cursor.execute("CREATE DATABASE IF NOT EXISTS Company")
        cursor.execute("USE Company")
        
        cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (EmpID INT PRIMARY KEY,
Empname VARCHAR(50), designation VARCHAR(50), Salary INT)""")
        
        records = [
            (1, "A", "Manager", 50000),
            (2, "B", "Manager", 50000),
            (3, "C", "Developer", 200000),
            (4, "D", "Developer", 100000),
            (5, "E", "Senior Developer", 300000)
        ]
        
        cursor.executemany("INSERT INTO Employee (EmpID, Empname, designation, Salary) VALUES (%s, %s, %s, %s)", records)
        conn.commit()

    elif a == "display":
        cursor.execute("USE Company")
        cursor.execute("SELECT * FROM Employee")
        rows = cursor.fetchall()
        for row in rows:
            print(f"EmpID: {row[0]}, Name: {row[1]}, Designation: {row[2]}, Salary: {row[3]}")
    elif a == "update":
        cursor.execute("USE Company")
        cursor.execute("UPDATE Employee SET Salary = Salary + 5000 WHERE designation = 'Manager'")
        conn.commit()
    elif a == "delete":
        cursor.execute("USE Company")
        Delete = int(input("Enter Employee ID to delete: "))
        cursor.execute("DELETE FROM Employee WHERE EmpID = '%s'", (Delete,))
        conn.commit()
    elif a == "quit":
        print("quitting..")
        break
    else:
        print("Invalid input")

cursor.close()
conn.close()