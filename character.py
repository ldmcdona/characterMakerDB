class character:
    def __init__(self, stats, race, character_class, level, alignment, skills, feats, abilities, inventory, spells):
        self.stats = stats
        self.race = race
        self.character_class = character_class
        self.level = level
        self.alignment = alignment
        self.skills = skills
        self.feats = feats
        self.abilities = abilities
        self.inventory = inventory
        self.spells = spells

    def get_x(self):
        pass

    def make_file(self):
        pass