class Character:

    def __init__(self, name, race, health, attack):
        self.name = name
        self.race = race
        # self.copper = 0
        self.health = health
        self.attack = attack 
        self.inv = Inventory([], 0, 0, 0)
    
    def battle(self, other):
        print(f"{self.name} attacks {other.name}!")
        # match(self.role):
            # case 'Wizard':
                # print(f"{self.name} attacks {other.name} with a spell!")
            # case 'Burglar':
                # print(f"{self.name} attacks {other.name} with a sneaking skill!")

class Ranger(Character): # INHERITS the character class (all attr and methods)

    # The Ranger battle class overrides the Character battle class
    def battle(self, other): 
        print(f"{self.name} attacks {other.name} with a Ranger skill!")

    def recruit_undead(self):
        pass

class Mage(Character): 
    def battle(self, other): 
        print(f"{self.name} attacks {other.name} with a Frost skill!")

class Burglar(Character): 
    def battle(self, other): 
        print(f"{self.name} attacks {other.name} with a sneaky stab skill!")

class Wizard(Character): 
    def battle(self, other): 
        print(f"{self.name} attacks {other.name} with a Fireball skill!")

class Chest:

    def __init__(self, items, gold, silver, copper):
        # Chest in itself "has a" Inventory
        self.inv = Inventory(items, gold, silver, copper) #self.inv is attribute, Inventory() is an instance of another class

class Inventory:
    
    def __init__(self, items, gold, silver, copper):
        self.items = items # list
        # self.gold = gold
        # self.silver = silver
        # self.copper = copper 
        self.set_currency(gold, silver, copper) # Delegation
    
    def transfer(self, to_inv): # 'transfer' better to use than 'loot' as it's multipurpose
        # Add all the items from from_inv to to_inv
        to_inv.items.extend(self.items)
        # Delete all the items from the from_inv
        self.items = []
        # Add the currency from from_inv to to_inv
        to_inv.copper += self.copper
        # Set currency of from_inv to 0
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