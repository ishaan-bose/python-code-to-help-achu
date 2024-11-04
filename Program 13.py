import csv

def Create_csv():
    with open("Login.csv", "a", newline="") as file:
        writer = csv.writer(file)
        uid = input("Enter User ID: ")
        passwd = input("Enter Password: ")
        writer.writerow([uid, passwd])

def Read_csv():
    with open("Login.csv", "r") as file:
        reader = csv.reader(file)
        print("\nRecords in Login:")
        for row in reader:
            print(f"UID: {row[0]}, Password: {row[1]}")

def Search_csv(uid):
    found = False
    with open("Login.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == uid:
                print(f"User found - UID: {row[0]}")
                found = True
                break
        if not found:
            print("User not found.")

print("Enter \'create\' to create new record")
print("Enter \'read\' to read record")
print("Enter \'search\' to search record")
print("Enter \'quit\' to quit")

while True:
    a = input("\nEnter choice: ")
    if a == "create":
        Create_csv()
    elif a == "read":
        Read_csv()
    elif a == "search":
        Search_csv(input("Enter uid to search: "))
    elif a == "quit":
        print("quitting..")
        break
    else:
        print("Invalid input")