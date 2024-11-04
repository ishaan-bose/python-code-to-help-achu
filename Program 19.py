import mysql.connector as msql

conn = msql.connect(host="localhost",user="user1",password="123")
cursor = conn.cursor()

print("Enter \'create\' to create a new record")
print("Enter \'display\' to display the records")
print("Enter \'display delhi\' to display record where city is delhi")
print("Enter \'delete\' to delete record of client based on client id")
print("Enter \'quit\' to quit program")

while True:
    a = input("Enter your choice: ")

    if a == "create":
        cursor.execute("CREATE DATABASE IF NOT EXISTS Company")
        cursor.execute("USE Company")
        
        cursor.execute("""
CREATE TABLE IF NOT EXISTS Client (ClientID INT PRIMARY KEY,
ClientName VARCHAR(50), City VARCHAR(50))""")
        
        records = [
            (1, "A", "Delhi"),
            (2, "B", "Bangalore"),
            (3, "C", "Mumbai"),
            (4, "D", "Delhi"),
            (5, "E", "Chennai")
        ]
        
        cursor.executemany("INSERT INTO Client (ClientID, ClientName, City) VALUES (%s, %s, %s)", records)
        conn.commit()

    elif a == "display":
        cursor.execute("USE Company")
        cursor.execute("SELECT * FROM Client")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ClientID: {row[0]}, Name: {row[1]}, City: {row[2]}")
    elif a == "display delhi":
        cursor.execute("USE Company")
        cursor.execute("SELECT * FROM Client")
        rows = cursor.fetchall()
        for row in rows:
            if row[2] == "Delhi":
                print(f"ClientID: {row[0]}, Name: {row[1]}, City: {row[2]}")  
    elif a == "delete":
        cursor.execute("USE Company")
        Delete = int(input("Enter Client ID to delete: "))
        cursor.execute("DELETE FROM Client WHERE ClientID = '%s'", (Delete,))
        conn.commit()
    elif a == "quit":
        print("quitting..")
        break
    else:
        print("Invalid input")

cursor.close()
conn.close()