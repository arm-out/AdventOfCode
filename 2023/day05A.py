import sys
from utils import getInput

DAY = 5
getInput(DAY)

f = open("inputs/day05.txt", "r")
input = f.read().splitlines()


seeds = []
seed_soil = {}
soil_fert = {}
fert_water = {}
water_light = {}
light_temp = {}
temp_humidity = {}
humidity_loc = {}

curr = 0
prev = False
for i in range(len(input)):
    line = input[i]
    if prev:
        prev = False
        continue
    if line == "":
        curr += 1
        prev = True
        continue
    if curr == 0:
        seeds = [int(x) for x in line.split(":")[1].split(" ") if x.isnumeric()]
    if curr == 1:
        source = int(line.split(" ")[1])
        dest = int(line.split(" ")[0])
        ranges = int(line.split(" ")[2])
        seed_soil[(source, ranges)] = dest
    if curr == 2:
        source = int(line.split(" ")[1])
        dest = int(line.split(" ")[0])
        ranges = int(line.split(" ")[2])
        soil_fert[(source, ranges)] = dest
    if curr == 3:
        source = int(line.split(" ")[1])
        dest = int(line.split(" ")[0])
        ranges = int(line.split(" ")[2])
        fert_water[(source, ranges)] = dest
    if curr == 4:
        source = int(line.split(" ")[1])
        dest = int(line.split(" ")[0])
        ranges = int(line.split(" ")[2])
        water_light[(source, ranges)] = dest
    if curr == 5:
        source = int(line.split(" ")[1])
        dest = int(line.split(" ")[0])
        ranges = int(line.split(" ")[2])
        light_temp[(source, ranges)] = dest
    if curr == 6:
        source = int(line.split(" ")[1])
        dest = int(line.split(" ")[0])
        ranges = int(line.split(" ")[2])
        temp_humidity[(source, ranges)] = dest
    if curr == 7:
        source = int(line.split(" ")[1])
        dest = int(line.split(" ")[0])
        ranges = int(line.split(" ")[2])
        humidity_loc[(source, ranges)] = dest

locs = []
for seed in seeds:
    info = {'seed': seed}
    for (source, ranges) in seed_soil:
        if seed in range(source, source+ranges):
            info['soil'] = seed_soil[(source, ranges)] + seed - source
    if 'soil' not in info.keys():
        info['soil'] = seed

    for (source, ranges) in soil_fert:
        if info['soil'] in range(source, source+ranges):
            info['fert'] = soil_fert[(source, ranges)] + info['soil'] - source
    if 'fert' not in info.keys():
        info['fert'] = info['soil']
    
    for (source, ranges) in fert_water:
        if info['fert'] in range(source, source+ranges):
            info['water'] = fert_water[(source, ranges)] + info['fert'] - source
    if 'water' not in info.keys():
        info['water'] = info['fert']
    
    for (source, ranges) in water_light:
        if info['water'] in range(source, source+ranges):
            info['light'] = water_light[(source, ranges)] + info['water'] - source
    if 'light' not in info.keys():
        info['light'] = info['water']
    
    for (source, ranges) in light_temp:
        if info['light'] in range(source, source+ranges):
            info['temp'] = light_temp[(source, ranges)] + info['light'] - source
    if 'temp' not in info.keys():
        info['temp'] = info['light']
    
    for (source, ranges) in temp_humidity:
        if info['temp'] in range(source, source+ranges):
            info['humidity'] = temp_humidity[(source, ranges)] + info['temp'] - source
    if 'humidity' not in info.keys():
        info['humidity'] = info['temp']
    
    for (source, ranges) in humidity_loc:
        if info['humidity'] in range(source, source+ranges):
            info['loc'] = humidity_loc[(source, ranges)] + info['humidity'] - source
    if 'loc' not in info.keys():
        info['loc'] = info['humidity']

    locs.append(info['loc'])


print(min(locs))

