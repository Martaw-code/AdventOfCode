file = open("../inputs/day3.txt","r")
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]

def bin2dec(n):
    return int(n,2) #base 2

lenCadenes = len(lines[0])
print(lenCadenes)

gamma = ""
epsilonRate = "" #bit invers de gamma

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
        epsilonRate += "1"
    else:
        gamma += "1"
        epsilonRate += "0"

gamma = bin2dec(gamma)
epsilonRate = bin2dec(epsilonRate)
        
powerConsumption = gamma * epsilonRate
print(f"Power Consumption: {powerConsumption}")


def filterNumbers(numbers, common):
    for i in range(len(numbers[0])):
        if len(numbers) == 1:
            break
        bit_count = sum(int(num[i]) for num in numbers)
        if common:
            desired_bit = '1' if bit_count >= len(numbers) / 2 else '0'
        else:
            desired_bit = '0' if bit_count >= len(numbers) / 2 else '1'
        numbers = [num for num in numbers if num[i] == desired_bit]
    return numbers[0]


oxygen_generator_rating = filterNumbers(lines.copy(), common=True)
co2_scrubber_rating = filterNumbers(lines.copy(), common=False)

oxygen_generator_rating_decimal = int(oxygen_generator_rating, 2)
co2_scrubber_rating_decimal = int(co2_scrubber_rating, 2)

life_support_rating = oxygen_generator_rating_decimal * co2_scrubber_rating_decimal
print(f"Life Support Rating: {life_support_rating}")