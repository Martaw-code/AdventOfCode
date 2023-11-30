file = open("2021/inputs/day1.txt","r")
lines = file.readlines()
file.close()

lines = [int(line) for line in lines]
print(lines)

numberIncreasesPart1 = 0
for i in range(1, len(lines)):
    if (lines[i-1] < lines[i]):
          numberIncreasesPart1 += 1

##PART 1
print(numberIncreasesPart1)

numberIncreasesPart2 = 0
for i in range(1, len(lines)-2):
    if (lines[i-1] + lines[i] + lines[i+1] < lines[i] + lines[i+1] + lines[i+2]):
          numberIncreasesPart2 += 1
    
 ##PART 2
print(numberIncreasesPart2)   
