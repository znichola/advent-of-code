import re

with open("input.txt", 'r') as file:
    input = file.readlines()

def extract_card(line: str) -> ([],[]):
    m = re.search(r".+: (.+?) \| (.+)", line)

    if m:
        l1 = [int(i) for i in m.group(1).split()]
        l2 = [int(i) for i in m.group(2).split()]
        return (l1, l2)
    else:
        return None

def winning_numbers(card):
    winning = card[0]
    my = card[1]
    return [m for m in my if m in winning]

def calc_part1(winning_numbers):
    # print(len(winning_numbers), winning_numbers)
    if len(winning_numbers) == 0:
        return 0
    return 2 ** (len(winning_numbers) - 1)


# print(extract_card(input[0]))
# print(2**(len(winning_numbers(extract_card(input[0]))) - 1))

print(sum([calc_part1(winning_numbers(extract_card(line))) for line in input]))