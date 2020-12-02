f = open("002input.txt",'r')
raw = f.readlines()
raw = [ lines.strip() for lines in raw ]
print(f"A total of {len(raw)} lines are in the file")

rules = [ lines[ :lines.index(':') ] for lines in raw ]
pwds = [ lines[lines.index(':')+2: ] for lines in raw ]

num_valid = 0
for i, pwd in enumerate(pwds):
    rule = rules[i].split(" ")
    char = rule[1]
    two_place = rule[0].split("-")
    place1idx = int(two_place[0]) - 1
    place2idx = int(two_place[1]) - 1
    value1 = pwd[place1idx] == char
    value2 = pwd[place2idx] == char
    if value1 ^ value2:
        num_valid +=1

print(num_valid)

f.close()
