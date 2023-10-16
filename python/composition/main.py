import rpg

aragorn = rpg.Character('Aragorn', 'Human')
galadriel = rpg.Character('Galadriel', 'Elf')
frodo = rpg.Character('Frodo', 'Hobbit')

# frodo.gold = 10
# frodo.silver = 

frodo.set_currency(9, 47, 23)

chest = rpg.Chest(['longsword', 'iron helm'], 2, 25, 50)

print(chest.__dict__)
# print(aragorn.__dict__)
# print(frodo.__dict__)
# print(galadriel.__dict__)

print(frodo.get_currency())