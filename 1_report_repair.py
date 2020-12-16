import sys

data = {int(line.strip()) for line in open("data/1-input.txt").readlines()}

# Part 1
for val in data:
    if 2020 - val in data:
        print(val*(2020-val))
        break

# Part 2
for val_1 in data:
    for val_2 in data:
        if 2020 - val_1 - val_2 in data:
            print(val_1*val_2*(2020-val_1-val_2))
            sys.exit()
