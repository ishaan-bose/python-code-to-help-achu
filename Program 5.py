#programs 1 - 4 already done seperately

nums = [int(x) for x in input("Enter space seperated numbers: ").split()]

def OddEvenChange(inputList):
    for i in range(len(inputList)):
        if inputList[i] % 2 == 0:
            inputList[i] //= 2  # Halve the even number
        else:
            inputList[i] *= 2   # Double the odd number

def Mode(inputList):
    frequency = {}
    for num in inputList:
        if num not in frequency:
            frequency[num] = 0
        frequency[num] += 1
    maxFrequency = 0
    modeVal = 0
    for i in frequency.keys():
        if frequency.get(i) > maxFrequency:
            maxFrequency = frequency.get(i)
            modeVal = i

    print(f"{modeVal} is the mode of frequency {maxFrequency}")

def Find(inputList, element):
    try:
        index = inputList.index(element)
        print(f"location of first occurence is {index+1}")
    except ValueError:
        print("element not found")

print("\nEnter \'mode\' to find the mode of the list, \'modify\' to doulbe the odd values and halve the even values")
print("Enter \'quit\' to quit, \'find\' to find a particular element in the list")
while True:
    a = input("\nEnter choice: ")
    if a[0:4] == "mode":
        Mode(nums)
    elif a[0:4] == "find":
        Find(nums, int(input("Enter element to find: ")))
    elif a[0:4] == "quit":
        print("exitting..")
        break
    elif a[0:6] == "modify":
        OddEvenChange(nums)
        print(nums)
    else:
        print("invalid input")