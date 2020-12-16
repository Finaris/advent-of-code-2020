data = [line.strip() for line in open("data/8-input.txt").readlines()]


# Part 1
visited_instructions = set()
i, acc = 0, 0
while i < len(data):
    if i in visited_instructions:
        break
    visited_instructions.add(i)

    instruction, value = data[i].split()
    if instruction == "nop":
        i += 1
    elif instruction == "acc":
        acc += int(value)
        i += 1
    elif instruction == "jmp":
        i += int(value)
    else:
        raise ValueError

# Part 2

