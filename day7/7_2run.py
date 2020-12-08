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
def getChildBagNum(bag_type):
    current_checking_bag = bags[bag_type]
    num_bags = 1
    for inner_bag in current_checking_bag.inner_bags:
        num_inner_bag = inner_bag[0]
        type_inner_bag = inner_bag[1]
        if type_inner_bag == 'no other':
            return num_bags
        num_bags += int(num_inner_bag) * getChildBagNum(type_inner_bag)
    return num_bags
print(getChildBagNum('shiny gold')-1)
f.close()

