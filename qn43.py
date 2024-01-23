# Write a Python program to remove an item from a tuple. \
game=('football','vollyball','basketball')
# converting tuple into list
list_game=list(game)
list_game.remove('vollyball')
# again converting list into tuples
game=tuple(list_game)
print(game)
