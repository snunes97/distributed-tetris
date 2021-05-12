import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk as ttk


class Gui:
    def __init__(self):
        self.BOARDX = 13
        self.BOARDY = 23

        self.master = tk.Tk()
        self.master.geometry("450x750")

        wall = Image.open("imgs/wall.png")
        self.wallImg = ImageTk.PhotoImage(wall)

        void = Image.open("imgs/void.png")
        self.voidImg = ImageTk.PhotoImage(void)

        block = Image.open("imgs/block.png")
        self.blockImg = ImageTk.PhotoImage(block)

    def start_gui(self):

        for col in range(self.BOARDX):
            for row in range(self.BOARDY):

                if col == 0 or col == self.BOARDX-1 or row == 0 or row == self.BOARDY-1:
                    wLabel = tk.Label(self.master, image=self.wallImg, pady="0", padx="0", bd=1)
                    wLabel.grid(row=row, column=col, sticky=tk.W)

                else:
                    vLabel = tk.Label(self.master, image=self.voidImg, pady="0", padx="0", bd=1)
                    vLabel.grid(row=row, column=col, sticky=tk.W)

        tk.mainloop()

    def update_gui(self, board):

        for row in range(len(board)):
            for col in range(len(board[row])):

                if col == 1 or col == 2:
                    wLabel = tk.Label(self.master, image=self.blockImg, pady="0", padx="0", bd=1)
                    wLabel.grid(row=row, column=col, sticky=tk.W)



