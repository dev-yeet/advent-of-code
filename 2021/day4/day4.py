from pprint import pprint


winningBoard,winnerScore,finalBoard,finalScore,winnersList = [],None,[],None,[]

def generateGameBoards():
    
    fileLines = open("input","r")
    
    global bingoInput 
    
    bingoInput = fileLines.readline().split(",")

    tempGameBoard = []

    global gameBoardList
    gameBoardList = []

    for line in fileLines:
        if len(line) > 1:                
            tempGameBoard.append(line.split())

            if len(tempGameBoard) == 5:
                gameBoardList.append(tempGameBoard)
                tempGameBoard = []
    
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
        tempBoard = board.copy()
        print(tempBoard)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == string_input:
                    board[i][j] = f"*{board[i][j]}"
        if checkforWin(board,string_input):
            if tempBoard not in winnersList:
                winnersList.append(tempBoard)
                winnersLastInputList.append(int(string_input))

                       
def main():
    generateGameBoards()

    global winnersList,winnersLastInputList
    winnersList,winnersLastInputList = [],[]

    for num in bingoInput:
        checkNumber(num)

        for winner in winnersList:
            if winner in gameBoardList:
                gameBoardList.remove(winner)
    
    winnerScore = getBoardSum(winnersList[0]) * winnersLastInputList[0]
    loserScore = getBoardSum(winnersList[-1]) * winnersLastInputList[-1]

    print(f"Winner Score: {winnerScore}")
    pprint(winnersList[0])


    print(f"Loser Score: {loserScore}")
    pprint(winnersList[-1])



if __name__ == "__main__":
    main()


