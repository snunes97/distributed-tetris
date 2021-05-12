from threading import Thread


class Timer(Thread):
    def __init__(self, event, board):
        Thread.__init__(self)
        self.board = board
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1.0):
            self.board.tick()
