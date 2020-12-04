f = open('input.txt', 'r')
map = f.read()
map = map.split('\n')[:-1]
print(f"A total of {len(map)} rows in this map.")
print(f"Every line has {len(map[0])} point")

mul_num_tree = 1
def getNumTree(base_down, slope):
    num_tree = 0
    for down in range(base_down, len(map), base_down):
        right = int((down * slope) % len(map[0]))
        current_encounter = map[down][right]
        if current_encounter == "#":
            num_tree += 1
    return num_tree
slope = [1, 3, 5, 7, 1/2]
for i, base_down in enumerate([1, 1, 1, 1, 2]):
    mul_num_tree = mul_num_tree * getNumTree(base_down, slope[i])
print(mul_num_tree)   

