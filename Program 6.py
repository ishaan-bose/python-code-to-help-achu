s = input("Enter a sentence: ")

Letters = {}
Digits = {}
SpecialChars = {}
for char in s:
    if char.isalpha():
        if char not in Letters:
            Letters[char] = 0
        Letters[char] += 1
    elif char.isdigit():
        if char not in Digits:
            Digits[char] = 0
        Digits[char] += 1
    else:
        if char not in SpecialChars:
            SpecialChars[char] = 0
        SpecialChars[char] += 1

print("Enter \'l\' for displaying letters dictionary")
print("Enter \'d\' for displaying digits dictionary")
print("Enter \'s\' to display special characters dictionary")
print("Enter \'q\' to quit")

while True:
    a = input("Enter choice: ")
    if a[0] == 'l':
        print(Letters)
    elif a[0] == 'd':
        print(Digits)
    elif a[0] == 's':
        print(SpecialChars)
    elif a[0] == 'q':
        print("quitting..")
        break
    else:
        print("invalid input")
