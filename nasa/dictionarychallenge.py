#!/usr/bin/python3

import argparse


parser = argparse.ArgumentParser('get statistics for a hero')
parser.add_argument('hero', help='takes in a hero argument')
parser.add_argument('stat', help ='takes in statistic')
args = parser.parse_args()

  

values = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

try:
    print(f"{args.hero.title()}'s {args.stat} is {values[args.hero][args.stat]}")
except:
    print("You entered a wrong argument")
    


