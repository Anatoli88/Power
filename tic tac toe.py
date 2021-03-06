choices = []

for x in range(0, 9):
    choices.append(str(x + 1))

playerOneTurn = True
winner = False


def printBoard() :
    print('\n -----')
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print(' -----')
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print(' -----')
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print(' -----\n')


while not winner:
    printBoard()

    if playerOneTurn:
        print("Игрок 1:")
    else:
        print("Игрок 2:")

    try:
        choice = int(input(">> "))
    except:
        print("Введите правильное поле")
        continue
    if choices[choice - 1] == 'X' or choices[choice-1] == 'O':
        print("Неверный ход, попробуйте еще")
        continue

    if playerOneTurn:
        choices[choice - 1] = 'X'
    else:
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range(0, 3):
        y = x * 3
        if choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]:  # скобки были лишними
            winner = True
            printBoard()
        if choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]:  # скобки были лишними
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or
       (choices[2] == choices[4] and choices[4] == choices[6])):
        winner = True
        printBoard()


print("Игрок " + str(int(playerOneTurn + 1)) + " выиграл!\n")
