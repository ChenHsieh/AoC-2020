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
    appearance_range = rule[0].split("-")
    max = int(appearance_range[1])
    min = int(appearance_range[0])
    appearance = pwd.count(char)
    if min <= appearance <= max:
        num_valid +=1

print(num_valid)

f.close()
