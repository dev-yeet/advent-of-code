from pprint import pprint


winningBoard,winnerScore,finalBoard,finalScore,winnerList = [],None,[],None,[]

def generateGameBoards():
    
    fileLines = open("input","r")
    
    global bingoInput 
    
    bingoInput = fileLines.readline().split(",")

    tempGameBoard = []

    global gameBoardList
    gameBoardList = []

    for line in fileLines:
        if line != "\n":
            if len(tempGameBoard) < 5:
                tempGameBoard.append(line.split())
            else:
                gameBoardList.append(tempGameBoard.copy())
                tempGameBoard = []
                tempGameBoard.append(line.split())

def getBoardSum(list):
    
    sum = 0
    for i in range(len(list)):
        for j in range(len(list[0])):
            if "*" not in f"{list[i][j]}":
                sum += int(list[i][j])
    return sum

def checkforWin(board,num):

    global winnerScore,finalScore

    global gameBoardList

    for i in range(len(board)):
        hits = 0
        for j in range(len(board[0])):
            if "*" in f"{board[i][j]}":
                hits += 1
                if hits == 5:
                    return True
            
                    
    for j in range(len(board[0])):
        hits = 0
        for i in range(len(board)):
            if "*" in f"{board[i][j]}":
                hits += 1
                if hits == 5:
                    return True
                     
def checkNumber(string_input):
    for index,board in enumerate(gameBoardList):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == string_input:
                    board[i][j] = f"*{board[i][j]}"
        if checkforWin(board,string_input):
            if len(gameBoardList) > 1:
                print(index)
                tempGameBoardList.pop(index)
                global winnerList
                winnerList.append(string_input)
            else:
                return

                       
def main():
    generateGameBoards()
    
    global tempGameBoardList
    tempGameBoardList = gameBoardList.copy()
    
    for num in bingoInput:
        checkNumber(num)
    
    pprint(tempGameBoardList)
    # loserScore = getBoardSum(gameBoardList[0])
    # print(loserScore)

    # print(f"Winner Score: {winnerScore}")
    # print(f"Loser Score: {finalScore}")


if __name__ == "__main__":
    main()


