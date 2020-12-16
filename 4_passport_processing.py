import re

data = [line.strip() for line in open("data/4-input.txt").readlines()]

# Pre-process the passports.
passports = []
current_passport = {}
for line in data:
    if line == "":
        passports.append(current_passport)
        current_passport = {}
    else:
        for field in line.split():
            key, value = field.split(":")
            current_passport[key] = value
else:
    passports.append(current_passport)

# Part 1
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
num_valid_passports = 0
for passport in passports:
    if required_fields.issubset(set(passport.keys())):
        num_valid_passports += 1
print(num_valid_passports)

# Part 2
eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

num_valid_passports = 0
for passport in passports:
    if required_fields.issubset(set(passport.keys())):
        if not 1920 <= int(passport["byr"]) <= 2002:
            continue
        if not 2010 <= int(passport["iyr"]) <= 2020:
            continue
        if not 2020 <= int(passport["eyr"]) <= 2030:
            continue

        if not re.match("^[0-9]+(cm|in)", passport["hgt"]):
            continue
        num = int(passport["hgt"][:-2:])
        unit = passport["hgt"][-2:]
        if (unit == "in" and not (59 <= num <= 76)) or (unit == "cm" and not (150 <= num <= 193)):
            continue

        if not re.match("^#([0-9]|[a-f]){6}", passport["hcl"]):
            continue

        if passport["ecl"] not in eye_colors:
            continue
        if len(passport["pid"]) != 9:
            continue
        num_valid_passports += 1
print(num_valid_passports)
