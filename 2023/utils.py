import os
from dotenv import load_dotenv

def getInput(day):
    day_pad = '0' + str(day) if day < 10 else str(day)
    load_dotenv()
    if not os.path.isfile(f"inputs/day{day_pad}.txt"):
        os.system(f"curl https://adventofcode.com/2023/day/{day}/input --cookie session={os.environ['AOC_SESSION']} > inputs/day{day_pad}.txt")