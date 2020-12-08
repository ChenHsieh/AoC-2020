f = open('input.txt', 'r')
raw = f.readlines()
rules = [ rule.strip('\n') for rule in raw ]
print(f'Threr are {len(rules)} rules')
import re
class BagClass:    
    def __init__(self, bag_rule):
        self.outer_bags = []
        bags = bag_rule.split('contain')
        self.bag_type = bags[0][:-5].strip()
        self.inner_bags = re.findall(r'(?P<bag_number>\d|\w*) (?P<bag_type>\w* \w*) bag', bags[1])
    def add_outer_bag(self, outer_bag):
        self.outer_bags.append(outer_bag)
bags = {}
for rule in rules:
    bag = BagClass(rule)
    bags[bag.bag_type] = bag
for bag in bags:
    for inner_bag in bags[bag].inner_bags:
        child_bag_type = inner_bag[1]
        if child_bag_type == 'no other':
            break
        child_bag = bags[child_bag_type]
        child_bag.add_outer_bag(bag)
checking_rules = 1
current_checking_bags = ['shiny gold']
container_bags = []
checked_bags = []
while checking_rules:
    next_round_checking_bags = []
    current_checking_bags = list(set(current_checking_bags))
    for current_checking_bag_type in current_checking_bags:
        if current_checking_bag_type in checked_bags:
            continue        
        checked_bags.append(current_checking_bag_type)
        current_checking_bag = bags[current_checking_bag_type]
        next_round_checking_bags.extend(current_checking_bag.outer_bags)
        container_bags.extend(current_checking_bag.outer_bags)
    current_checking_bags = next_round_checking_bags
    if next_round_checking_bags == []:
        checking_rules = 0
print(len(set(container_bags)))
f.close()
