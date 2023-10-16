import rpg

aragorn = rpg.Character('Aragorn', 'Human')
galadriel = rpg.Character('Galadriel', 'Elf')
frodo = rpg.Character('Frodo', 'Hobbit')

frodo.inv.set_currency(9, 47, 23)

chest = rpg.Chest(['longsword', 'iron helm'], 2, 25, 50)

# print(chest.inv.__dict__)
# print(aragorn.__dict__)
# print(frodo.__dict__)
# print(galadriel.__dict__)

# Frodo loots a chest!
chest.inv.transfer(frodo.inv)

print(f"Frodo's current inventory: {frodo.inv.__dict__}")
print(f"Frodo's current gold/silver/copper breakdown: {frodo.inv.get_currency()}")
print(f"Contents of chest: {chest.inv.__dict__}")