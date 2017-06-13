field = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def print_field(field):
    out_list = list()
    counter = 0
    for item in range(0, 9, 3):
        ritem = item + 3
        print(field[item:ritem])

def go(player, point): #making choice
    field[point] = player
    print_field(field)


def win(field): #check _who is winner
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for combination in win_combinations:
        if field[combination[0]] == field[combination[1]] == field[combination[2]]:
            winner = field[combination[0]]
            return winner


#print_field()
def main():

    print_field(field)
    while True: #main game process
        x_choice = int(input('Ход "Х": '))
        go('X', x_choice)
        if win(field):#win check after every choice
            print('Победил "Х"!')
            break
        o_choice = int(input('Ход "0": '))
        go('O', o_choice)
        if win(field):
            print('Победил "0"!')
            break
main()