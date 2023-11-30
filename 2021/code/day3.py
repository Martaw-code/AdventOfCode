file = open("../inputs/day3.txt","r")
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]

def bin2dec(n):
    return int(n,2) #base 2

lenCadenes = len(lines[0])
print(lenCadenes)

gamma = ""
epsilon_rate = "" #bit invers de gamma

for i in range(lenCadenes):
    num_zeros = 0
    num_uns = 0
    for line in lines:
        if (line[i] == '0'):
            num_zeros += 1
        else:
            num_uns += 1
    if (num_zeros > num_uns):
        gamma += "0"
        epsilon_rate += "1"
    else:
        gamma += "1"
        epsilon_rate += "0"

gamma = bin2dec(gamma)
epsilon_rate = bin2dec(epsilon_rate)
        
power_consumption = gamma * epsilon_rate
print(f"Power Consumption: {power_consumption}")