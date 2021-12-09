from pprint import pprint


winningBoard,winnerScore,finalBoard,finalScore = [],None,[],None

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

def checkforWin(string_input):

    global winnerScore,finalScore

    global gameBoardList

    for board in gameBoardList.copy():
            for i in range(len(board)):
                hits = 0
                for j in range(len(board[0])):
                    if "*" in f"{board[i][j]}":
                        hits += 1
                        if hits == 5:
                            if winnerScore == None:
                                winnerScore = getBoardSum(board) * int(string_input)
                                gameBoardList.remove(board)
                                return
                            else:
                                if len(gameBoardList) > 1:
                                    gameBoardList.remove(board)
                                    return
                                else:
                                    finalScore = getBoardSum(board)
                                    gameBoardList.remove(board)
                                    return
                            
            for j in range(len(board[0])):
                hits = 0
                for i in range(len(board)):
                    if "*" in f"{board[i][j]}":
                        hits += 1
                        if hits == 5:
                            if winnerScore == None:
                                winnerScore = getBoardSum(board) * int(string_input)
                                gameBoardList.remove(board)
                                return
                            else:
                                if len(gameBoardList) > 1:
                                    gameBoardList.remove(board)
                                    return
                                else:
                                    finalScore = getBoardSum(board)
                                    gameBoardList.remove(board)
                                    return
def checkNumber(string_input):
    for board in gameBoardList:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == string_input:
                    board[i][j] = f"*{board[i][j]}"
                       
def main():
    generateGameBoards()
    
    for num in bingoInput:
        checkNumber(num)
        checkforWin(num)
        # pprint(len(gameBoardList))
        print(num)


    # print(f"Winner Score: {winnerScore}")
    # print(f"Loser Score: {finalScore}")


if __name__ == "__main__":
    main()


