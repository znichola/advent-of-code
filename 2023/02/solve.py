with open("input.txt", 'r') as file:
    game_data = file.readlines()

def getHands(line: str) -> [str]:
    return line.split(":")[1].split(";") 

def getCubes(line: str) -> [(int, str)]:
    cubes = line.split(",")
    def foo(l: str) -> (int, str):
        f = l.split()
        return (int(f[0]), f[1])
    return list(map(foo, cubes))

def getHandResults(cubes: [(int, str)]) -> (int, int, int):
    r = 0
    g = 0
    b = 0
    for c in cubes:
        if c[1] == "red":
            assert r == 0
            r = c[0]
        if c[1] == "green":
            assert g == 0
            g = c[0]
        if c[1] == "blue":
            assert b == 0
            b = c[0]
    return (r, g, b)

def parseGame(line: str) -> [(int, int, int)]:
    return list(map(lambda a: getHandResults(getCubes(a)), getHands(line)))

def gameMax(game: [(int, int, int)]) -> (int, int, int):
    r = 0
    g = 0
    b = 0
    for i in game:
        r = r if r > i[0] else i[0]
        g = g if g > i[1] else i[1]
        b = b if b > i[2] else i[2]
    return (r, g, b)

# print("res", list(map(lambda a: gameMax(parseGame(a)), game_data)))

games_max = [(i+1, gameMax(parseGame(el))) for i, el in enumerate(game_data)]

# only 12 red cubes, 13 green cubes, and 14 blue cubes
def check(g):
    c = g[1]
    if (c[0] > 12): return False
    if (c[1] > 13): return False
    if (c[2] > 14): return False
    return True

possible_games = list(filter(check, games_max))
print("res", games_max)
print("awnser", sum([el[0] for el in possible_games]))

# Bonus

games_max_no_id = [gameMax(parseGame(el)) for el in game_data]
print("bonus awnser", sum([el[0] * el[1] * el[2] for el in games_max_no_id ]))