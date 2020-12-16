from collections import Counter

data = [line.strip() for line in open("data/2-input.txt").readlines()]

# Part 1
count = 0
for line in data:
    policy, password = line.split(":")
    char_range, char = policy.split()
    char_min, char_max = char_range.split("-")

    counter = Counter(password)
    if char in counter and (int(char_min) <= counter[char] <= int(char_max)):
        count += 1
print(count)

# Part 2
count = 0
for line in data:
    policy, password = line.split(":")
    password = password.strip()
    char_range, char = policy.split()
    char_index_1, char_index_2 = char_range.split("-")
    char_1, char_2 = password[int(char_index_1)-1], password[int(char_index_2)-1]
    if (char_1 == char or char_2 == char) and char_1 != char_2:
        count += 1
print(count)
