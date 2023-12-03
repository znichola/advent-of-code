import re

with open("input.txt", 'r') as file:
    game_data = file.readlines()

def special(char: str):
     if char == ".": return False
     if char == "\n": return False
     if char.isdigit(): return False
     print(f"True {char}")
     return True

def is_special(i, j):
    # print(f"special [{i}, {j}]")
    if i < 0 or j < 0:
         return False
    try:
        return special(game_data[i][j])
    except:
        return False

def above_and_below(row, character, word):
    # print("above below")
    for i in range(len(word) + 2):
        if is_special(row-1, character - i): return True
        if is_special(row+1, character - i): return True
    return False

def check(row, character, word):
    # print(f"checking {word=}, at: ({row}, {character})")
    if (is_special(row, character) |
        is_special(row, character-len(word)-1) |
        above_and_below(row, character, word)):
        return True
    return False

cumulator = ""
all_numbers = list()
for r, row in enumerate(game_data):
    for c, character in enumerate(row):
        if character.isdigit():
                cumulator += character
        else:
             if cumulator != "":
                  n = int(cumulator)
                  if check(r, c, cumulator):
                        all_numbers.append(n)
                  else:
                       print(f"not match {cumulator=}")
                    #    exit()
                  cumulator = ""



print(f"{all_numbers}")
print(f"{sum(all_numbers)=}")

# ;dddddd'
# ;......'
# ;.1123.'
# ;......'
# ;dddddd'