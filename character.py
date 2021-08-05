class Character:
    def __init__(self):
        self.stats = None
        self.race = None
        self.character_class = None
        self.level = None
        self.alignment = None
        self.feats = "N/A"
        self.inventory = "N/A"

    def set_stats(self, sb):
        self.stats = sb

    def set_race(self, r):
        self.race = r

    def set_char(self, cc):
        self.character_class = cc

    def set_level(self, lev):
        self.level = lev

    def set_align(self, al):
        self.alignment = al

    def get_x(self):
        pass

    def make_file(self):
        pass