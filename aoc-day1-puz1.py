
inputFileName = r"C:\Users\Geoffrey House User\Documents\GitHub\advent-of-code\aoc-day1-puz1-input.txt"

maxCal = 0
totalCalHolder = []
currSum = 0
with open(inputFileName, 'r') as inFile:
    for line in inFile:
        #print(line.strip())
        if line.strip() != "":
            currEntry = int(line.strip())
            currSum += currEntry
        else:
            #print("New elf")
            if currSum > maxCal:
                maxCal = currSum
            totalCalHolder.append(currSum)
            currSum = 0
    if currSum > maxCal:
        maxCal = currSum
    totalCalHolder.append(currSum)

print(maxCal)

# This is sorted ascending
sortedCalHolder = sorted(totalCalHolder)

# Get the last 3 total calorie entries and sum them
sumTopThree = sum(sortedCalHolder[-3:])
print(sortedCalHolder)
print(f'Sum of the top three is: {sumTopThree}')