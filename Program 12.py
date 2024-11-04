import pickle

def File_Create():
    with open("Employee.dat", "ab") as file:
        Employee_id = input("Enter Employee ID: ")
        Employee_name = input("Enter Employee Name: ")
        Employee_salary = int(input("Enter Employee Salary in rupees: "))
        Employee_design = input("Enter Employee designation: ")
        record = {"Employee_id": Employee_id, "Employee_name": Employee_name, "Employee_Salary": Employee_salary, "Employee_Designation": Employee_design}
        pickle.dump(record, file)

def File_Read():
    with open("Employee.dat", "rb") as file:
        print("\nRecords in Employee.dat:")
        while True:
            try:
                record = pickle.load(file)
                print(f"ID: {record['Employee_id']}, Name: {record['Employee_name']}, Salary: {record['Employee_Salary']}, Designation: {record['Employee_Designation']}")
            except EOFError:
                break

def Update_Data():
    records = []
    with open("Employee.dat", "rb") as file:
        while True:
            try:
                records.append(pickle.load(file))
            except EOFError:
                break
    for record in records:
            if (record['Employee_Designation']).lower() == "manager":
                record['Employee_Salary'] += 5000
    with open("Employee.dat", "wb") as file:
        for i in range(len(records)):
            pickle.dump(records[i], file)


print("Enter \'create\' to create new record")
print("Enter \'read\' to read record")
print("Enter \'update\' to search record")
print("Enter \'quit\' to quit")

while True:
    a = input("Enter choice: ")
    if a == "create":
        File_Create()
    elif a == "read":
        File_Read()
    elif a == "update":
        Update_Data()
    elif a == "quit":
        print("quitting..")
        break
    else:
        print("Invalid choice, please try again.")