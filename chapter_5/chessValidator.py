import pprint

myBoard = {'a1' : 'bking', 'a2': 'bqueen', 'a3': 'bpawn', 'c3': 'bpawn'}



def validateBoard(board):
    # counters
    num_of_bking = 0
    num_of_wking = 0
    num_of_bpawn = 0
    num_of_wpawn = 0

    pos_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    pos_nums = ['1', '2', '3', '4', '5', '6', '7', '8']
    colours = ['b', 'w']
    chars = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    

    for pos,piece in board.items():
        currChar = piece[1:]
        print(pos)
        print(piece[0])
        print(pos[0] in pos_letters)
        print(pos[1] in pos_nums)
        print(piece[0] in colours)
        print(currChar in chars)
        
        if pos[0] in pos_letters and pos[1] in pos_nums and piece[0] in colours and currChar in chars:
            if piece[0] == 'w':
                if currChar == 'king':
                    num_of_wking = num_of_wking + 1
                if currChar == 'pawn':
                    num_of_wpawn = num_of_wpawn + 1
            
            else:
                if currChar == 'king':
                    num_of_bking = num_of_bking + 1
                if currChar == 'pawn':
                    num_of_bpawn = num_of_bpawn + 1

            if num_of_bpawn > 16 or num_of_wpawn > 16 or num_of_wking > 1 or num_of_bking > 1:
                return False

        else:
            return False


    return True



print(validateBoard(myBoard))



    

