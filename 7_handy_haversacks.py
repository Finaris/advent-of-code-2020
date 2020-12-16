from collections import defaultdict

data = [line.strip() for line in open("data/7-input.txt").readlines()]

# Pre-process the rules.
rule_set = defaultdict(lambda: defaultdict(int))
for rule in data:
    source, items = rule.split(" contain ")
    for item in items.split(", "):
        item_components = item.split()
        count, sink = item_components[0], " ".join(item_components[1:])
        if sink == "other bags.":
            rule_set[source.replace("bags", "bag")] = None
        else:
            rule_set[source.replace("bags", "bag")][sink.replace("bags", "bag").replace(".", "")] = \
                int(count) if count.isdigit() else None


def all_children_bags(bag):
    bags = set()
    if bag not in rule_set or not rule_set[bag]:
        return bags

    for other_bag in rule_set[bag].keys():
        bags.add(other_bag)
        bags.update(all_children_bags(other_bag))
    return bags


def number_of_children(bag):
    if bag not in rule_set or not rule_set[bag]:
        return 0
    return sum(capacity*(1+number_of_children(child)) for child, capacity in rule_set[bag].items())


# Part 1
count = 0
for bag_type in rule_set.keys():
    if bag_type == "shiny gold bag":
        continue
    if "shiny gold bag" in all_children_bags(bag_type):
        count += 1
print(count)

# Part 2
print(number_of_children("shiny gold bag"))
