import mysql.connector

conn = mysql.connector.connect(host="localhost",user="user1",password="123")
cursor = conn.cursor()

print("Enter \'create\' to create a new record")
print("Enter \'display\' to display the records")
print("Enter \'search\' to search for a product based on id")
print("Enter \'quit\' to quit program")

while True:
    a = input("Enter your choice: ")

    if a == "create":
        cursor.execute("CREATE DATABASE IF NOT EXISTS Company")
        cursor.execute("USE Company")
        
        cursor.execute("""
CREATE TABLE IF NOT EXISTS Product (Pid INT PRIMARY KEY,
Pname VARCHAR(50), Qty INT, Price INT)""")
        
        records = [
            (1, "Table", 14, 30000),
            (2, "Chair", 36, 15000),
            (3, "Bed", 30, 48000),
            (4, "Painting", 15, 7000),
            (5, "Sofa", 20, 43000)
        ]
        
        cursor.executemany("INSERT INTO Product (Pid, Pname, Qty, Price) VALUES (%s, %s, %s, %s)", records)
        conn.commit()

    elif a == "display":
        cursor.execute("USE Company")
        cursor.execute("SELECT * FROM Product")
        rows = cursor.fetchall()
        for row in rows:
            print(f"Product ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]}, Price: {row[3]}")
    elif a == "search":
        searchPid = int(input("Enter Product to search: "))
        cursor.execute("SELECT * FROM Product WHERE Pid = %s", (searchPid,))
        result = cursor.fetchone()
        if result:
            print("Product ID:", result[0], "Name:", result[1], "Quantity:", result[2], "Price:", result[3])
        else:
            print("Product not found.")
    elif a == "quit":
        print("quitting..")
        break
    else:
        print("Invalid input")

cursor.close()
conn.close()