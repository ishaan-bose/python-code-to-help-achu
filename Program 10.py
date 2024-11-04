def ReadFile():
    with open("Story.txt", "r") as file:
        for line in file:
            print(line, end='')


def displayWithS():
    with open("Story.txt", "r") as file:
        for line in file:
            if line[0].lower() == 's':
                print(line, end='')


def displayWithHash():
    with open("Story.txt", "r") as file:
        content = file.read().split()
        print("\nWords separated by '#':")
        print("#".join(content))

print("Enter \'display\' to display the file")
print("Enter \'display s\' to display lines starting with s")
print("Enter \'display #\' to display words seperated by #")
print("Enter \'quit\' to quit")

while True:
    a = input("Enter choice: ")

    if a == "display":
        ReadFile()
        print("\n")
    elif a[0:9] == "display s":
        displayWithS()
    elif a[0:9] == "display #":
        displayWithHash()
    elif a[0:4] == "quit":
        print("quitting..")
        break
    else:
        print("Invalid input")