from tkinter import *
from tkinter import messagebox
import random
class Board:
    color={
        '2': '#776e65',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        self.root = Tk()
        self.root.title("2048 Game")
        self.gamearea = Frame(self.root)
        self.board = []
        self.gridCell = [[0]*4 for i in range(4)]
        self.compress = False
        self.merge  = False
        self.moved = False
        self.score = 0

        for i in range(4):
            rows = []
            for j in range(4):
                l = Label(self.gamearea, text='', font=('arial', 22, 'bold'),width=4, height=2)
                l.grid(row=i,column=j, padx=7, pady=7)

                rows.append(l)

            self.board.append(rows)
        self.gamearea.grid()

        def reverse(self):
            for k in range(4):
                i = 0
                j = 3
                while(i<j):
                    self.gridCell[k][i], self.gridCell[k][j] = self.gridCell[k][j], self.gridCell[k][i]
                    i+=1
                    j-=1

                def transpose(self):
                    pass