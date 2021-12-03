# Advent of Code 2021
# Day 3
# Johnny Brown

def part1():
    input_rows = open("input","r").read().splitlines()
    # input_rows = [ int(row) for row in input_rows]

    numberLength = len(input_rows[0])

    for row in input_rows[1:]:
        if len(row) > numberLength:
            numberLength = len(row)
    
    currentIndex = 0

    zeroCount = 0
    oneCount = 0
    
    gammaRate = ""
    epsilonRate = ""

    while(currentIndex < numberLength):
        
        for number in input_rows:
            if number[currentIndex] == "0":
                zeroCount += 1
            elif number[currentIndex] == "1":
                oneCount += 1
        
        if zeroCount > oneCount:
            gammaRate += "0"
            epsilonRate += "1"
        elif oneCount > zeroCount:
            gammaRate += "1"
            epsilonRate += "0"
        
        currentIndex += 1
        zeroCount = 0
        oneCount = 0
    
    gammaRate = int(gammaRate,base=2)
    epsilonRate = int(epsilonRate,base=2)

    print(gammaRate)
    print(epsilonRate)

    power_consumption = (gammaRate * epsilonRate)

    print(power_consumption)
    
    # print(input_rows)



def main():
    part1()
if __name__ == "__main__":
    main()