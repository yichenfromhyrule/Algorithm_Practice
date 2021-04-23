import random
def generateBoard(words):
    # I am not sure if I understand this question correctly,
    # seems the generateBoard only needs to return a list
    # with 2 cards for each word and the Boolean = false
    result_list = []
    for word in words:
        word_card = [word, False]
        result_list.append(word_card)
        result_list.append(word_card)
    # You may want the list in a random order
    random.shuffle(result_list)
    return result_list

def displayBoard(board):
    # Go through the cards in board
    # i is the card's index
    # print the "index:" at first
    # If card is face-down, print "???"
    # Else print card's name
    for i in range(len(board)):
        print(i, ": ", end="")
        if(board[i][1]==False):
            print("???")
        else:
            print(board[i][0])
    return None

def getFlippedCards(board):
    result_list=[]
    # Go through the cards in board
    # i is the card's index
    # If card is face-up, add card's index to result_list
    for i in range(len(board)):
        if board[i][1]==True:
            result_list.append(i)
    return result_list

def pickIndex(board):
    picked_index = input("Pick a card index:")
    # Check the user input's type and value
    if picked_index.isnumeric():
        picked_index=int(picked_index)
        if picked_index >= len(board) or picked_index <0:
            print("Out of range. Pick a valid card.")
            pickIndex(board)
        else:
            # Flip the picked_index card
            if(board[picked_index][1]==True):
                print("You've already flipped that card. Pick a different card.")
                pickIndex(board)
            else:
                board[picked_index] = [board[picked_index][0], not board[picked_index][1]]
                return picked_index
    else:
        print("That's not an integer!")
        pickIndex(board)

def playMemoryGame(words):
    # A
    print("Welcome to Memory!")
    board = generateBoard(words)
    displayBoard(board)

    #B & C
    expect_result = [i for i in range(len(board))]
    print(expect_result)
    while(getFlippedCards(board)!=expect_result):
        move = 0
        for i in range(2):
            index_1 = int(pickIndex(board))
            displayBoard(board)
            index_2 = int(pickIndex(board))
            displayBoard(board)
            # D
            # Check if there are two cards be flipped
            if(board[index_1][0]==board[index_2][0]):
                print("Good guess!")
            else:
                print("Try again")
                # Flip these two card to back
                board[index_1][1] = False
                board[index_2][1] = False
            print("---")
            move+=1

    print("Good game! You took %d moves to clear the board."%move)



if __name__ == '__main__':
    words = ["dog","cat","bird"]
    playMemoryGame(words)
