from threading import Thread
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk as ttk
from multiprocessing import Process, Manager
import time

class Gui(Thread):
    def __init__(self, queue):
        Thread.__init__(self)

        self.queue = queue
        self.tick = Process(target=self.update_gui, args=self.queue)

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

        self.tick.start()

        tk.mainloop()

    def update_gui(self):

        while True:
            time.sleep(1)
            print("SPORTING CAMPIAO CHEIO DO COVID")
            for row in range(len(self.board.board)):
                for col in range(len(self.board.board[row])):

                    if col == 1 or col == 2:
                        wLabel = tk.Label(self.master, image=self.blockImg, pady="0", padx="0", bd=1)
                        wLabel.grid(row=row, column=col, sticky=tk.W)

            self.master.update_idletasks()
            self.master.update()

    def run(self):
        self.update_gui()
