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
    print(f"\nstarting for {value}")
    return cnv(cnv(cnv(cnv(cnv(cnv(cnv(value, seed_to_soil), soil_to_fertilizer), fertilizer_to_water), water_to_light), light_to_temperature), temperature_to_humidity), humidity_to_location)

# print(f"{seeds=}")
# print(f"{seed_to_soil=}")
# print(f"{soil_to_fertilizer=}")
# print(f"{fertilizer_to_water=}")
# print("-----------")
# c = conversion_chain(14)
# print(f"{c=}")

print(f"part 1: {min([conversion_chain(s) for s in seeds])}")