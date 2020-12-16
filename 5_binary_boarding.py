data = [line.strip() for line in open("data/5-input.txt").readlines()]

# Part 1


def binary_search(data_string, low, high, low_partition="F", high_partition="B"):
    if not data_string:
        if low != high:
            raise ValueError("??")
        return low

    average = int((low+high)/2)
    if data_string[0] == low_partition:
        return binary_search(data_string[1:], low, average, low_partition, high_partition)
    elif data_string[0] == high_partition:
        average += 1
        return binary_search(data_string[1:], average, high, low_partition, high_partition)
    raise ValueError("?")


def seat_id(boarding_pass):
    return binary_search(boarding_pass[:-3:], 0, 127)*8 + binary_search(boarding_pass[-3::], 0, 7, "L", "R")


seat_ids = {seat_id(boarding_pass) for boarding_pass in data}
print(max(seat_ids))

# Part 2
i = 0
while True:
    if i not in seat_ids and i-1 in seat_ids and i+1 in seat_ids:
        print(i)
        break
    i += 1
