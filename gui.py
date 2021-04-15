import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk as ttk


class Gui:

    BOARDX = 13
    BOARDY = 23

    def start_gui(self):

        master = tk.Tk()
        master.geometry("450x750")

        wall = Image.open("imgs/wall.png")
        wallImg = ImageTk.PhotoImage(wall)

        void = Image.open("imgs/void.png")
        voidImg = ImageTk.PhotoImage(void)

        block = Image.open("imgs/block.png")
        blockImg = ImageTk.PhotoImage(block)

        for col in range(self.BOARDX):
            for row in range(self.BOARDY):

                if col == 0 or col == self.BOARDX-1 or row == 0 or row == self.BOARDY-1:
                    wLabel = tk.Label(master, image=wallImg, pady="0", padx="0", bd=1)
                    wLabel.grid(row=row, column=col, sticky=tk.W)

                else:
                    vLabel = tk.Label(master, image=voidImg, pady="0", padx="0", bd=1)
                    vLabel.grid(row=row, column=col, sticky=tk.W)

        tk.mainloop()