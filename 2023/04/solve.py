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

# bonus

w_numbers = [len(winning_numbers(extract_card(line))) for line in input]
total_cards = [1 for _ in range(0, len(input))]

def recursive(index):
    print(f"{index=} {total_cards=}")
    if index >= len(w_numbers):
        return
    for i in range(index + 1, w_numbers[index] + index + 1):
        total_cards[i] += total_cards[index]
    return recursive(index + 1)

recursive(0)

# print(f"part2: {w_numbers}")
print(f"part2: {sum(total_cards)}")
