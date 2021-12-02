# Advent of Code 2021
# Day 2
# Johnny Brown

def part1():
    input_file = open("input", "r")

    hPos = 0
    depth = 0

    rows = input_file.read().splitlines()
    for row in rows:

        temp_tuple = row.split(" ")

        commandFirstLetter = temp_tuple[0][0]
        count = int(temp_tuple[1])

        if commandFirstLetter == "f":
            hPos += count
        elif commandFirstLetter == "d":
            depth += count
        elif commandFirstLetter == "u":
            depth -= count
            
    print(f"Horizontal Position: {hPos}")
    print(f"Depth : {depth}")
    print(f"Product of Horizontal Position and Depth {hPos * depth}")


def part2():
    input_file = open("input", "r")

    hPos = 0
    depth = 0
    aim = 0

    rows = input_file.read().splitlines()
    for row in rows:

        temp_tuple = row.split(" ")

        commandFirstLetter = temp_tuple[0][0]
        count = int(temp_tuple[1])

        if commandFirstLetter == "f":
            hPos += count
            depth += (aim * count)
        elif commandFirstLetter == "d":
            aim += count
        elif commandFirstLetter == "u":
            aim -= count
            
    print(f"Horizontal Position: {hPos}")
    print(f"Depth : {depth}")
    print(f"Product of Horizontal Position and Depth {hPos * depth}")

def main():
    print("Part 1")
    part1()
    print("\nPart 2")
    part2()


if __name__ == "__main__":
    main() 