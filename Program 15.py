stack = []

print("Enter \'push\' to push a doctor onto stack")
print("Enter \'pop\' to pop a doctor from stack")
print("Enter \'display\' to display stack")
print("Enter \'quit\' to quit")

while True:
    a = input("\nEnter your choice: ")
    
    if a == "push":
        doc_id = input("Enter Doc_ID: ")
        doc_name = input("Enter Doc_name: ")
        
        doctor = {"Doc_ID": doc_id, "Doc_name": doc_name}
        stack.append(doctor)     
    elif a == "pop":
        if len(stack) > 0:
            doctor = stack.pop()
            print(f"Popped: Doctor ID: {doctor['Doc_ID']}, Name: {doctor['Doc_name']}")
        else:
            print("Can't pop, empty stack")          
    elif a == "display":
        print("note: last element of stack is the one added most recently")
        for i in range(len(stack)):
            print(f"Doc_ID: {stack[i].get('Doc_ID')}, Doc_name: {stack[i].get('Doc_name')}")         
    elif a == "quit":
        print("quitting..")
        break
        
    else:
        print("Invalid input")