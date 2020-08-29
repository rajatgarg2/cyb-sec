#Two Player Tic Tac Toe game 

'''The board we are using will contain keys like in a calculator , which will
   be implemented using dictionary.Initially it's value will be empty space 
   and then after every move we will change the value according to player's
   choice of move.'''
   
   
theBoard = {7:' ', 8:' ', 9:' ',
            4:' ', 5:' ', 6:' ',
            1:' ', 2:' ', 3:' '}


board_keys = []


for key in theBoard:
    board_keys.append(key)
    
    
'''we have to print the updated board every time a player makes a move ,
   for that purpose we will make a function to print the board everytime
   by calling this function.'''
   
   
def printBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
 
    
 
#This is the main function where all magic begins

def game():
    turn = 'X'
    count = 0
    
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn, " + turn + ". Make a move!")
              
        move=int(input())
        
        if theBoard[move]==' ':
            theBoard[move]=turn;
            count += 1
        else:
            print('That place is already filled.\nMake another move!')
            continue
        
        #Now we will check if player X or 0 has won , for every move after
        #5 moves.
        
        if count >=5:
               if theBoard[7]==theBoard[8]==theBoard[9] !=' ':
                printBoard(theBoard)
                print("\nGame Over .\n")
                print("****" +turn+ " won. ****")
                break
               elif theBoard[4]==theBoard[5]==theBoard[6] !=' ':
                 printBoard(theBoard)
                 print("\nGame Over .\n")
                 print("****" +turn+ " won. ****")
                 break
               elif theBoard[1]==theBoard[2]==theBoard[3] !=' ':
                 printBoard(theBoard)
                 print("\nGame Over .\n")
                 print("****" +turn+ " won. ****")
                 break
               elif theBoard[1]==theBoard[4]==theBoard[7] !=' ':
                 printBoard(theBoard)
                 print("\nGame Over .\n")
                 print("****" +turn+ " won. ****")
                 break
               elif theBoard[2]==theBoard[5]==theBoard[8] !=' ':
                 printBoard(theBoard)
                 print("\nGame Over .\n")
                 print("****" +turn+ " won. ****")
                 break
               elif theBoard[3]==theBoard[6]==theBoard[9] !=' ':
                 printBoard(theBoard)
                 print("\nGame Over .\n")
                 print("****" +turn+ " won. ****")
                 break
               elif theBoard[7]==theBoard[5]==theBoard[3] !=' ':
                 printBoard(theBoard)
                 print("\nGame Over .\n")
                 print("****" +turn+ " won. ****")
                 break
               elif theBoard[1]==theBoard[5]==theBoard[9] !=' ':
                 printBoard(theBoard)
                 print("\nGame Over .\n")
                 print("****" +turn+ " won. ****")
                 break
             
        #If neither X nor 0 wins and the board is full, we'll declare
        #the result as tie
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            
        #Now we have to change the player after every move.
        if turn == 'X':
            turn = '0'
        else:
            turn ='X'
            
    #Now we will ask if player wants to restart the game or not.
    restart=input('Do you want to play Again?(y/n) : ')
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theBoard[key]=' '
        game()
                        
game()