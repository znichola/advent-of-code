with open("input.txt", 'r') as file:
    game_data = file.readlines()

gear_dict = {}
gear_dict_parts = {}

def add_dict(g, word):
    if g in gear_dict:
        gear_dict[g].append(int(word))
    else:
        gear_dict[g] = [int(word)]

def special(char: str):
    if char == ".": return False
    if char == "\n": return False
    if char.isdigit(): return False
    print(f"True {char}")
    return True

def is_special(i, j, word):
    # print(f"special [{i}, {j}]")
    if i < 0 or j < 0:
         return False
    try:
        if special(game_data[i][j]):
            if (game_data[i][j] == "*"):
                add_dict((i, j), word)
            return True
        return False
    except Exception:
        return False

def check(row, character, word):
    # print(f"checking {word=}, at: ({row}, {character})")
    t = 0
    t += is_special(row, character, word)
    t += is_special(row, character-len(word)-1, word)
    for i in range(len(word) + 2):
        t += is_special(row-1, character - i, word)
        t += is_special(row+1, character - i, word)
    return t > 0

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

print(f"dict {gear_dict}")
# foo = list(filter(lambda a: len(gear_dict[a]) == 2, gear_dict))
foo = {k: v for k, v in gear_dict.items() if len(v) == 2}
bar = [v[0] * v[1] for k, v in foo.items()]
print(f"{foo=}")
print(f"{bar=}")
print(f"bonus: {sum(bar)}")
# ;dddddd'
# ;......'
# ;.1123.'
# ;......'
# ;dddddd'