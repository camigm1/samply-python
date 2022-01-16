
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

board()

def main():
    print("Congratulations, you won the game!")

def playerTurn():
    i = 0
    turn = 1
    while i <= 9:
        if turn%2 == 1:
            playerOne = int(input("x's turn to choose a square (1-9):"))
            if playerOne == line_1[0]:
                line_1[0] = 'X'
                if line_1[0] =='X' and line_2[0] =='X' and line_3[0] == 'X':
                    main()
                    break
                elif line_1[0] =='X' and line_1[1] == 'X' and line_3[2] == 'X':
                    main()
                    break
                elif line_1[0] == 'X' and line_2[1] == 'X' and line_3[2] == 'X':
                    main()
                    break
            elif playerOne == line_1[1]:
                line_1[1] = 'X'
                if line_1[1] =='X' and line_2[1] =='X' and line_3[1] == 'X':
                    main()
                    break
                elif line_1[0] =='X' and line_1[1] == 'X' and line_3[2] == 'X':
                    main()
                    break
            elif playerOne == line_1[2]:
                line_1[2] = 'X'
                if line_1[2] =='X' and line_2[2] =='X' and line_3[2] == 'X':
                    main()
                    break
                elif line_3[0] =='X' and line_2[1] == 'X' and line_1[2] == 'X':
                    main()
                    break
            elif playerOne == line_2[0]:
                line_2[0] = 'X'
                if line_1[0] =='X' and line_2[0] =='X' and line_3[0] == 'X':
                    main()
                    break
                elif line_2[0] =='X' and line_2[1] == 'X' and line_2[2] =='X':
                   main()
                   break
            elif playerOne == line_2[1]:
                line_2[1] = 'X'
                if line_1[1] =='X' and line_2[1] =='X' and line_3[1] == 'X':
                    main()
                    break
                elif line_2[0] =='X' and line_2[1] == 'X' and line_2[2] =='X':
                    main()
                elif line_3[0] =='X' and line_2[1] == 'X' and line_1[2] == 'X':
                    main()
                    break 
                elif line_1[0] == 'X' and line_2[1] == 'X' and line_3[2] == 'X':
                    main()
                    break  
            elif playerOne == line_2[2]:
                line_2[2] = 'X'
                if line_1[2] =='X' and line_2[2] =='X' and line_3[2] == 'X':
                    main()
                    break
                elif line_2[0] =='X' and line_2[1] == 'X' and line_2[2] =='X':
                    main()
                    break
            elif playerOne == line_3[0]:
                line_3[0] = 'X'
                if line_1[0] =='X' and line_2[0] =='X' and line_3[0] == 'X':
                    main()
                    break
                elif line_3[0] =='X' and line_2[1] == 'X' and line_1[2] == 'X':
                    main()
                    break
            elif playerOne == line_3[1]:
                line_3[1] = 'X'
                if line_1[1] =='X' and line_2[1] =='X' and line_3[1] == 'X':
                    main()
                    break
                elif line_3[0] == 'X' and line_3[1] == 'X' and line_3[2] == 'X':
                    main()
                    break
            elif playerOne == line_3[2]:
                line_3[2] = 'X'
                if line_1[2] =='X' and line_2[2] =='X' and line_3[2] == 'X':
                    main()
                    break
                elif line_3[0] == 'X' and line_3[1] == 'X' and line_3[2] == 'X':
                    main()
                    break
                elif line_1[0] == 'X' and line_2[1] == 'X' and line_3[2] == 'X':
                    main()
                    break
            i+=1
            turn+=1
            board()
        elif turn%2 == 0:
            playerTwo = int(input("o's turn to choose a square (1-9):"))
            if playerTwo == line_1[0]:
                line_1[0] = 'O'
                if line_1[0] =='O' and line_2[0] =='O' and line_3[0] == 'O':
                    main()
                    break
                elif line_1[0] =='O' and line_1[1] == 'O' and line_1[2] == 'O':
                    main()
                    break
                elif line_1[0] == 'O' and line_2[1] == 'O' and line_3[2] == 'O':
                    main()
                    break
            elif playerTwo == line_1[1]:
                line_1[1] = 'O'
                if line_1[1] =='O' and line_2[1] =='O' and line_3[1] == 'O':
                    main()
                    break
                elif line_1[0] =='O' and line_1[1] == 'O' and line_1[2] == 'O':
                    main()
                    break
            elif playerTwo == line_1[2]:
                line_1[2] = 'O'
                if line_1[0] =='O' and line_1[1] == 'O' and line_1[2] == 'O':
                    main()
                    break
                elif line_1[2] =='O' and line_2[2] =='O' and line_3[2] == 'O':
                    main()
                    break
                elif line_3[0] =='O' and line_2[1] == 'O' and line_1[2] == 'O':
                    main()
                    break
            elif playerTwo == line_2[0]:
                line_2[0] = 'O'
                if line_1[0] =='O' and line_2[0] =='O' and line_3[0] == 'O':
                    main()
                    break
                elif line_2[0] =='O' and line_2[1] == 'O' and line_2[2] =='O':
                    main()
                    break
            elif playerTwo == line_2[1]:
                line_2[1] = 'O'
                if line_1[1] =='O' and line_2[1] =='O' and line_3[1] == 'O':
                    main()
                    break
                elif line_2[0] =='O' and line_2[1] == 'O' and line_2[2] =='O':
                    main()
                    break
                elif line_3[0] =='O' and line_2[1] == 'O' and line_1[2] == 'O':
                    main()
                    break
            elif playerTwo == line_2[2]:
                line_2[2] = 'O'
                if line_1[2] =='O' and line_2[2] =='O' and line_3[2] == 'O':
                    main()
                    break
                elif line_2[0] =='O' and line_2[1] == 'O' and line_2[2] =='O':
                    main()
                    break
            elif playerTwo == line_3[0]:
                line_3[0] = 'O'
                if line_1[0] =='O' and line_2[0] =='O' and line_3[0] == 'O':
                    main()
                    break
                elif line_3[0] == 'O' and line_3[1] == 'O' and line_3[2] == 'O':
                    main()
                    break
                elif line_3[0] =='O' and line_2[1] == 'O' and line_1[2] == 'O':
                    main()
                    break
            elif playerTwo == line_3[1]:
                line_3[1] = 'O'
                if line_1[1] =='O' and line_2[1] =='O' and line_3[1] == 'O':
                    main()
                    break
                elif line_3[0] == 'O' and line_3[1] == 'O' and line_3[2] == 'O':
                    main()
                    break
            elif playerTwo == line_3[2]:
                line_3[2] = 'O'
                if line_1[2] =='O' and line_2[2] =='O' and line_3[2] == 'O':
                    main()
                    break
                elif line_3[0] == 'O' and line_3[1] == 'O' and line_3[2] == 'O':
                    main()
                    break
                elif line_1[0] == 'O' and line_2[1] == 'O' and line_3[2] == 'O':
                    main()
                    break
            i+=1
            turn+=1
            board()


playerTurn()


    



# 
#     if line_1[0] =='O' and line_2[0] =='O' and line_3[0] == 'O':
#         main()
#         break
#     elif line_1[1] =='O' and line_2[1] =='O' and line_3[1] == 'O':
#         main()
#         break
#     elif line_1[2] =='O' and line_2[2] =='O' and line_3[2] == 'O':
#         main()
#         break
#     elif line_1[0] =='O' and line_1[1] == 'O' and line_1[2] == 'O'
#         main()
#         break
# #     elif line_2[0] =='O' and line_2[1] == 'O' and line_2[2] =='O':
# #         main()
# #         break
#       elif line_3[0] == 'O' and line_3[1] == 'O' and line_3[2] == 'O':
#           main()
#           break
# #     elif line_3[0] =='O' and line_2[1] == 'O' and line_1[2] == 'O':
# #         main()
# #         break
#     # elif line_1[0] == 'O' and line_2[1] == 'O' and line_3[2] == 'O':
#     #     main()
#     #     break

 


