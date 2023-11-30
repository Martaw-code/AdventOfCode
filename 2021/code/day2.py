file = open("2021/inputs/day2.txt","r")
lines = file.readlines()
file.close()

lines = [line.strip().split() for line in lines] #strip per treure el \n i el split per tenir la ins i el numero

x = 0
y = 0
aim = 0
for line in lines:
    if (line[0] == "forward"):
        x += int(line[1])
        y += aim*int(line[1])
    elif (line[0] == "down"):
        aim += int(line[1])
    else:
         aim -= int(line[1])
##PART 2
print(x*y)



