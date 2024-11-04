#skipping program 7

import random

rands = []
EvenRand = []

def Generate_Random(a, b):
    for i in range(5):
        rands.append(random.randint(a, b))

def Random_Even_Sum():
    while True:
        a = random.randint(1, 50)
        if a%2 == 0:
            EvenRand.append(a)
            break

print("Enter \'random\' for generating 5 random numbers to list")
print("Enter \'even random\' to generate even random numbers to another list")
print("Enter \'quit\' to quit program")

while True:
    a = input("\nEnter choice: ")
    if a[0:6] == "random":
        start = int(input("Enter range start: "))
        end = int(input("Enter range end: "))
        Generate_Random(start, end)
        print(rands)
    elif a[0:11] == "even random":
        Random_Even_Sum()
        print("Sum of random even's is: " + str(sum(EvenRand)))
    elif a[0:4] == "quit":
        print("quitting..")
        break
    else:
        print("Invalid input")