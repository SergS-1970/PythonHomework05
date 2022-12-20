#Создайте программу для игры в ""Крестики-нолики"".

def printBoard(board):
    print('-------------')
    for i in range(3):
        print('|', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print ('-------------')
       
def movePlayer(sign):
    check = False
    while not check:
        move = input('Введите номер ячейки, куда поставить ' + sign + ': ')
        try:
            move = int(move)
        except:
            print('Нужно ввести число.')
        if move >= 1 and move <= 9:
            if str(board[move - 1]) not in 'XO':
                board[move - 1] = sign
                check = True
            else:
                print('Эта ячейка уже занята.')
        else:
            print('Введите число от 1 до 9.')
           
def controlWin(board):
    coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for item in coordinates:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return board[item[0]]
    return False
   
board = range(1,10)
board = list(map(str, board))

count = 0
win = False
while not win:
    printBoard(board)
    if count % 2 == 0:
        movePlayer('X')
    else:
        sign = 'O'
        movePlayer(sign)
    count += 1
    if count > 4:
        value = controlWin(board)
        if value:
            print(value + ' выиграл.')
            win = True
    if count == 9 and win == False:
        print('Ничья.')
        break
printBoard(board)