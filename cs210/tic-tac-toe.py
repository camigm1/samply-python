
#Camila Gallegos


# print("1|2|3")
# print("-+-+-")
# print("4|5|6")
# print("-+-+-")
# print("7|8|9")


line_1 = [1,2,3]
line_2 = [4,5,6]
line_3 = [7,8,9]


def board():
 print(line_1)
 print(line_2)
 print(line_3)

def playerTurn():
    i = 0
    turn = 1
    while i <= 9:
        if turn%2 == 1:
            playerOne = int(input("x's turn to choose a square (1-9):"))
            if playerOne == line_1[0]:
                line_1[0] = X
            elif playerOne == line_1[1]:
                line_1[1] = X
            elif playerOne == line_1[2]:
                line_1[2] = X
            elif playerOne == line_2[0]:
                line_2[0] = X
            elif playerOne == line_2[1]:
                line_2[1] = X
            elif playerOne == line_2[2]:
                line_2[2] = X
            elif playerOne == line_3[0]:
                line_3[0] = X
            elif playerOne == line_3[1]:
                line_3[1] = X
            elif playerOne == line_3[2]:
                line_3[2] = X
            i+=1
            turn+=1
            board()
        elif turn%2 == 0:
            playerTwo = input("o's turn to choose a square (1-9):")
            i+=1
            turn+=1
            board()



    
# def playerOne_Tic():
#     if playerOne == line_1[0]:
#         line_1[0] = 
# board()
# playerTurn()   


# playerTwo = float(input("o's turn to choose a square (1-9):"))


# def playerTwo_Tic():
#  for x in line_1:
#     if( playerTwo == x):
#         line_1[i]= x
#  for x in line_2:
#     if( playerTwo == x):
#         line_2[i] = x
#  for x in line_3:
#     if (playerTwo == x):
#         line_3[i] = x





 


