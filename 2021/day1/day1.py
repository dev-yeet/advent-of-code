# Advent of Code 2021
# Day 1
# Johnny Brown

def part1():
    
    num_list = []

    input_file = open ("input" , "r")    
    numList = input_file.read().splitlines()
    numList = [ int(numString) for numString in numList]

    
    currentIndex = 0
    numIncrease = 0

    while(currentIndex < len(numList)):
        
        #skip first index as there's nothing to compare to
        if currentIndex == 0:
            currentIndex += 1
        # compare number in numList at current index with previous index
        else:
            #increase numIncrease variable if number at current index is greater than previous index
            if int(numList[currentIndex]) > int(numList[currentIndex - 1]):
                numIncrease += 1 
            currentIndex += 1
    print(f"Day 1 Part 1 Answer: {numIncrease}")

def part2():
    
    num_list = []

    input_file = open ("input" , "r")    
    numList = input_file.read().splitlines()
    numList = [ int(numString) for numString in numList]
    
    currentIndex = 0
    numIncrease = 0

    while(currentIndex < len(numList)):
        
        if currentIndex == 0:
            currentIndex += 1
        else:
            #try to calculate sums of three pair of current index + next two numbers and and previous index + next two numbers
            try:
                sum1 = numList[currentIndex] + numList[currentIndex + 1] + numList[currentIndex + 2]
                sum2 = numList[currentIndex - 1] + numList[currentIndex] + numList[currentIndex + 1]
                # increment numIncrease if sum1 is greater
                if (sum1 > sum2):
                    numIncrease += 1
            # catch IndexError
            except IndexError:
                pass
            currentIndex += 1
    print(f"Day 1 Part 2 Answer: {numIncrease}")


def main():
    part1()
    part2()



if __name__ == "__main__":
    main()
