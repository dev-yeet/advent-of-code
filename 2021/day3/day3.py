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


def deleterow(input_list,index,bit):

    temp_input_list = input_list.copy()

    for row in temp_input_list:
        if int(row[index]) == bit:
            input_list.remove(row)
    
    print(input_list)

    
def findOxygenRating(input_list):
     
    numberLength = len(input_list[0])

    for row in input_list[1:]:
        if len(row) > numberLength:
            numberLength = len(row)
    
    currentIndex = 0
    while(currentIndex < numberLength):
        zeroCount = 0
        oneCount = 0
        
        for number in input_list:
            if number[currentIndex] == "0":
                zeroCount += 1
            elif number[currentIndex] == "1":
                oneCount += 1

        if zeroCount > oneCount:
            deleterow(input_list,currentIndex,1)
        elif oneCount > zeroCount:
            deleterow(input_list,currentIndex,0)
        else:
            deleterow(input_list,currentIndex,0)
        currentIndex += 1
    
    return(input_list[0])

def findCO2Rating(input_list):
     
    numberLength = len(input_list[0])

    for row in input_list[1:]:
        if len(row) > numberLength:
            numberLength = len(row)
    
    currentIndex = 0
    
    while(currentIndex < numberLength and len(input_list) > 1):
        zeroCount = 0
        oneCount = 0
        
        for number in input_list:
            if number[currentIndex] == "0":
                zeroCount += 1
            elif number[currentIndex] == "1":
                oneCount += 1

        if zeroCount < oneCount:
            deleterow(input_list,currentIndex,1)
        elif oneCount < zeroCount:
            deleterow(input_list,currentIndex,0)
        else:
            deleterow(input_list,currentIndex,1)
        currentIndex += 1


    return(input_list[0])

def part2():

    input_rows = open("input","r").read().splitlines()

    oxygenRating = findOxygenRating(input_rows.copy())
    co2Rating = findCO2Rating(input_rows.copy() )

    oxygenRating = int(oxygenRating,base=2)
    co2Rating = int(co2Rating,base=2)

    print(oxygenRating)
    print(co2Rating)
    print(oxygenRating * co2Rating)

   


# life support rating = oxygen generator rating * CO2 Scrubber Rating 



def main():
    # part1()
    part2()


if __name__ == "__main__":
    main()