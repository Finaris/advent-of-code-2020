from collections import namedtuple

data = [line.strip() for line in open("data/3-input.txt").readlines()]
width, height = len(data[0]), len(data)
Point = namedtuple("Point", ["x", "y"])

# Part 1
start = Point(3, 1)
num_trees = 0
while start.y < height:
    if data[start.y][start.x % width] == "#":
        num_trees += 1
    start = Point(start.x + 3, start.y + 1)
print(num_trees)

# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1
for slope in slopes:
    slope_x, slope_y = slope
    start = Point(slope_x, slope_y)
    num_trees = 0
    while start.y < height:
        if data[start.y][start.x % width] == "#":
            num_trees += 1
        start = Point(start.x + slope_x, start.y + slope_y)
    result *= num_trees
print(result)
