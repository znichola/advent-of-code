import re

with open("input.txt", 'r') as file:
    input = file.readlines()


def parse_seeds():
    for line in input:
        if line.startswith("seeds:"):
            s = line.removeprefix("seeds:")
            return [int(i) for i in s.split()]

def parse_map(match):
    matching = False
    map_list = []
    for line in input:
        if line.startswith(match):
            matching = True
            continue
        if matching and line == "\n":
            break
        if matching:
            t = [int(i) for i in line.split()]
            map_list.append((t[0], t[1], t[2]))
    return map_list

def cnv(value, value_maps):
    # print(f"{value_maps}")
    for m in value_maps:
        dst = m[0]
        src = m[1]
        rng = m[2]
        if value < src:
            continue
        if value > src + rng:
            continue
        # print(f"{dst - src + value}")
        return dst - src + value
    # print(f"no val {value}")
    return value

seeds = parse_seeds()
seed_to_soil = parse_map("seed-to-soil")
soil_to_fertilizer = parse_map("soil-to-fertilizer")
fertilizer_to_water = parse_map("fertilizer-to-water")
water_to_light = parse_map("water-to-light")
light_to_temperature =parse_map("light-to-temperature")
temperature_to_humidity = parse_map("temperature-to-humidity")
humidity_to_location = parse_map("humidity-to-location")

def conversion_chain(value):
    a = cnv(cnv(cnv(cnv(cnv(cnv(cnv(value, seed_to_soil), soil_to_fertilizer), fertilizer_to_water), water_to_light), light_to_temperature), temperature_to_humidity), humidity_to_location)
    # print(f"for {value} its {a}")
    return a

# print(f"{seeds=}")
# print(f"{seed_to_soil=}")
# print(f"{soil_to_fertilizer=}")
# print(f"{fertilizer_to_water=}")
# print("-----------")
# c = conversion_chain(14)
# print(f"{c=}")

print(f"part 1: {min([conversion_chain(s) for s in seeds])}")

# part 2 

def regen_seeds(seeds):
    return [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

def min_per_seed(seed, lowest = None):
    print(f"checking seed{seed}")
    for s in range(seed[0], seed[0] + seed[1]):
        c = conversion_chain(s)
        if lowest == None:
            lowest = c
        if c < lowest:
            lowest = c
    return lowest


new_seeds = regen_seeds(seeds)

print(new_seeds)
# print(f"loweest per seed: {[min_per_seed(s) for s in new_seeds]}")
# seeds: 2149186375 163827995 1217693442 67424215 365381741 74637275 1627905362 77016740 22956580 60539394 586585112 391263016 2740196667 355728559 2326609724 132259842 2479354214 184627854 3683286274 337630529

# print(min([20358600, 31599214, 507296260, 913213391, 1794751573, 230207722, 65527228, 25430814, 433957126, 252411123]))

# part 1: 31599214
# [(2149186375, 163827995), (1217693442, 67424215), (365381741, 74637275), (1627905362, 77016740), (22956580, 60539394), (586585112, 391263016), (2740196667, 355728559), (2326609724, 132259842), (2479354214, 184627854), (3683286274, 337630529)]
# checking seed(2149186375, 163827995)
# checking seed(1217693442, 67424215)
# checking seed(365381741, 74637275)
# checking seed(1627905362, 77016740)
# checking seed(22956580, 60539394)
# checking seed(586585112, 391263016)
# checking seed(2740196667, 355728559)
# checking seed(2326609724, 132259842)
# checking seed(2479354214, 184627854)
# checking seed(3683286274, 337630529)
# loweest per seed: [20358600, 31599214, 507296260, 913213391, 1794751573, 230207722, 65527228, 25430814, 433957126, 252411123]