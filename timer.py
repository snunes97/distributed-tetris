from threading import Thread

class Timer(Thread):
    def __init__(self, event, board, gui):
        Thread.__init__(self)
        self.board = board
        self.gui = gui
        self.stopped = event
        self.firstRun = True

    def run(self):
        if self.firstRun:
            self.board.print_board()
            self.gui.start()

        while not self.stopped.wait(1.0):
            self.board.tick()
            self.gui.update_gui()
