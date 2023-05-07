'''You can reuse a variable'''

'''Amount of snakes in the zoo'''
amountSnakes = 0
zooEast = 3
amountSnakes = amountSnakes + zooEast

zooWest = 2
zooNorth = 5
amountSnakes = amountSnakes + zooWest + zooNorth

zooSouth = 1
amountSnakes = amountSnakes + zooSouth

print('The total of snakes in the city\'s zoo is:', amountSnakes)


'''You can do it, but an easier way'''
centralZoo = 3
amountSnakes += centralZoo
print('The total of snakes in the city\'s zoo is:', amountSnakes)
