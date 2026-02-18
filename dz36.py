import itertools


suit = ['♠', '♥', '♦', '♣']
nominal_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "V", "D", "K", "T"]

the_deck = itertools.product(suit, nominal_value)
combinations = list(itertools.combinations(the_deck, 5))

print(combinations)

with open("combinations.txt", "w", encoding="utf8") as file:
    record = file.write(str(combinations))