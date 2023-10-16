class Character:

    def __init__(self, name, race):
        self.name = name
        self.race = race
        # self.gold = 0
        # self.silver = 0
        self.copper = 0
    
    # This is called a 'setter'
    def set_currency(self, gold, silver, copper):
        self.copper = gold * 10000 + silver * 100 + copper

    # Called a 'getter'
    def get_currency(self):
        gold = self.copper // 10000
        silver = (self.copper % 10000) // 100
        copper = self.copper % 100
        return gold, silver, copper

class Chest:

    def __init__(self, items, gold, silver, copper):
        self.items = items
        self.gold = gold
        self.silver = silver
        self.copper = copper