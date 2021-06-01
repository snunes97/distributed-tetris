class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.active_piece = None

    def add_score(self, points):
        self.score += points

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

    def set_active_piece(self, piece):
        self.active_piece = piece

    def get_active_piece(self):
        return self.active_piece
