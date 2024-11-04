import csv

def Create_csv():
    with open("Address.csv", "a", newline="") as file:
        writer = csv.writer(file)
        name = input("Enter name: ")
        mobno = input("Enter mobile no.: ")
        email = input("Enter email: ")
        writer.writerow([name, mobno, email])

def Read_csv():
    with open("Address.csv", "r") as file:
        reader = csv.reader(file)
        print("\nRecords in Address.csv:")
        for row in reader:
            print(f"name: {row[0]}, mobile no.: {row[1]}, email: {row[2]}")

def Search_csv(mobno):
    found = False
    with open("Address.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == mobno:
                print(f"mobile no. found, adding to NewAddress.csv")
                with open("NewAddress.csv", "a", newline="") as Newfile:
                    writer = csv.writer(Newfile)
                    writer.writerow(row)
                found = True
                break
        if not found:
            print("mobile no. not found")

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
        Search_csv(input("Enter mobile no. to search: "))
    elif a == "quit":
        print("quitting..")
        break
    else:
        print("Invalid input")