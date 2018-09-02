import os
os.system("cls")

class Board:
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    def display(self):
        print(" %s | %s | %s " %(self.cells[0], self.cells[1], self.cells[2]))
        print("----------")
        print(" %s | %s | %s " %(self.cells[3], self.cells[4], self.cells[5]))
        print("----------")
        print(" %s | %s | %s " %(self.cells[6], self.cells[7], self.cells[8]))
    def update(self, n, player):
        if(self.cells[n] == " "):
            self.cells[n] = player
    def winner(self, player):
        if(self.cells[0] == player and self.cells[1] == player and self.cells[2] == player):
            return True
        if(self.cells[3] == player and self.cells[4] == player and self.cells[5] == player):
            return True
        if(self.cells[6] == player and self.cells[7] == player and self.cells[8] == player):
            return True
        if(self.cells[0] == player and self.cells[3] == player and self.cells[6] == player):
            return True
        if(self.cells[1] == player and self.cells[4] == player and self.cells[7] == player):
            return True
        if(self.cells[2] == player and self.cells[5] == player and self.cells[8] == player):
            return True
        if(self.cells[0] == player and self.cells[4] == player and self.cells[8] == player):
            return True
        if(self.cells[2] == player and self.cells[4] == player and self.cells[6] == player):
            return True
    def tie(self):
        c = 0
        for i in self.cells:
            if i != " ":
                c = c + 1
        if c == 9:
            return True
        else:
            return False
    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

board = Board()

def refresh():
    os.system("cls")
    print("Welcome to the ultimate tic-tac-toe game \n")
    board.display()

while(True):
    refresh()
    choice_X = int(input("\n X Please Choose a number from 1 to 9. > "))
    board.update(choice_X, "X")
    refresh()
    if board.winner("X"):
        print("\n X is the winner \n")
        play = input("Would you like to play again ? (Y/N)")
        if play == 'Y':
            board.reset()
            continue
        else:
            break
    if board.tie():
        print("\n Its a tie \n")
        play = input("Would you like to play again ? (Y/N)")
        if play == 'Y':
            board.reset()
            continue
        else:
            break
    choice_O = int(input("\n O Please Choose a number from 1 to 9. > "))
    board.update(choice_O, "O")
    refresh()
    if board.winner("O"):
        print("\n O is the winner \n")
        play = input("Would you like to play again ? (Y/N)")
        if play == 'Y':
            board.reset()
            continue
        else:
            break
    if board.tie():
        print("\n Its a tie \n")
        play = input("Would you like to play again ? (Y/N)")
        if play == 'Y':
            board.reset()
            continue
        else:
            break
