def write_to_file(data):
    with open("Story.txt", "w") as file:
        file.write(data)

def read_from_file():
    with open("Story.txt", "r") as file:
        content = file.read()
        print("\n\n"+content+"\n\n")


def file_statistics():
    with open("Story.txt", "r") as file:
        content = file.read()
        total_chars = len(content)
        total_words = len(content.split())
        total_digits = sum(c.isdigit() for c in content)
        
        print(f"Total characters: {total_chars}")
        print(f"Total words: {total_words}")
        print(f"Total digits: {total_digits}")

print("Enter \'write\' to write text")
print("Enter \'display\' to display text")
print("Enter \'stats\' to display the statistics of story")
print("Enter \'quit\' to quit")

while True:
    a = input("\nEnter choice: ")
    if a[0:5] == "write":
        text = input("Enter the text: ")
        write_to_file(text)
    elif a[0:7] == "display":
        print("the story is: ")
        read_from_file()
    elif a[0:5] == "stats":
        file_statistics()
    elif a[0:4] == "quit":
        print("quitting..")
        break
    else:
        print("Invalid input")