import os
import sys
from dotenv import load_dotenv

def getInput(day):
    day_pad = '0' + str(day) if day < 10 else str(day)
    load_dotenv()
    if not os.path.isfile(f"inputs/day{day_pad}.txt"):
        os.system(f"curl https://adventofcode.com/2024/day/{day}/input --cookie session={os.environ['AOC_SESSION']} > inputs/day{day_pad}.txt")

    if len(sys.argv) > 1:
        return open("inputs/test.txt", "r").read().splitlines()
    else:
        return open(f"inputs/day{day_pad}.txt", "r").read().splitlines()

def check2DBounds(inputs, x, y):
    return y >= 0 and y < len(inputs) and x >= 0 and x < len(inputs[y])
