def process_input(i):
    return i.replace('B','1').replace('F','0').replace('R','1').replace('L','0').strip()

def to_id(i):
    return int(i[:-3],2)*8 + int(i[-3:], 2)

with open("input.txt") as f:
    data = [process_input(line) for line in f]

ids = [to_id(i) for i in data]

print(max(ids))

for i in range(min(ids), max(ids)):
    if i not in ids:
        print(i)