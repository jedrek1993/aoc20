import re

def get_color(l):
    return " ".join(l.split(" ")[:2])

with open("day7/input.txt") as f:
    data = [l for l in f]

colors = ["shiny gold"]
tmp_colors = []

while True:
    for l in data:
        for c in colors:
            if c in l:
                tmp_colors.append(get_color(l))
    if len(set(colors)) == len(set(tmp_colors)):
        break
    colors = tmp_colors
    tmp_colors = []

print(len(set(colors))-1)

bags_in = {"color": "shiny gold", "count":1, "contain":[]}

def contain(color):
    for line in data:
        if line.startswith(color):
            break
    if "no other" in line:
        return []
    bags = re.findall(r'([0-9]) (\w+ \w+)', line)
    return [{"color":col, "count":int(count), "contain":contain(col)} for count, col in bags]

bags_in = {"color": "shiny gold", "count":1, "contain":contain("shiny gold")}

def count_bags(s):
    if not s['contain']:
        return s['count']
    return s['count'] * sum([count_bags(bag) for bag in s['contain']]) + s['count']

print(count_bags(bags_in)-1)