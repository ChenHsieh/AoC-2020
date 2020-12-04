f = open('input.txt', 'r')
map = f.read()
map = map.split('\n')[:-1]
print(f"A total of {len(map)} rows in this map.")
print(f"Every line has {len(map[0])} point")
num_tree = 0
for down in range(1, len(map)):
    right = (down * 3) % len(map[0])
    current_encounter = map[down][right]
    if current_encounter == "#":
        num_tree += 1
print(num_tree)
