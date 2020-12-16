data = [line.strip() for line in open("data/6-input.txt").readlines()]

groups, group = [], []
for line in data:
    if not line:
        groups.append(group)
        group = []
    else:
        group.append(line)
else:
    groups.append(group)

# Part 1
count = 0
for group in groups:
    chars = set()
    for quest in group:
        chars.update(set(quest))
    count += len(chars)
print(count)

# Part 2
count = 0
for group in groups:
    chars = set(group[0])
    for quest in group[1:]:
        chars = chars.intersection(set(quest))
    count += len(chars)
print(count)
