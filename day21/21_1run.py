with open('input.txt', 'r') as f:
    raw = f.readlines()
allergen_lists = [ line.split(' (contains ')[1].strip(')\n').split(', ') for line in raw ]
ingredient_lists = [ line.split(' (contains ')[0].split(' ') for line in raw ]
allergen_dict = {}
allergen_list = []
ingredient_list = []
print(f'{len(ingredient_lists)} different foods')
for i in range(len(ingredient_lists)):
    for ingredient in ingredient_lists[i]:
        ingredient_list.append(ingredient)
    for allergen in allergen_lists[i]:
        allergen_list.append(allergen)
print(f'{len(set(ingredient_list))} ingredients')
print(f'{len(set(allergen_list))} allergens')
for allergen in allergen_list:
    allergen_dict[allergen] = []
for i in range(len(ingredient_lists)):
    for allergen in allergen_lists[i]:
        allergen_dict[allergen].extend(ingredient_lists[i])
#print(allergen_dict)
real_allergen_list = []
for allergen, ingredients in allergen_dict.items():
    print(len(ingredients))
    print(len(set(ingredients)))
    highest_ingredient_num = 0
    allergic_ingredient_candidate = ingredients[0]
    for ingredient in ingredients:
        current_ingredient_num = ingredients.count(ingredient)
        if current_ingredient_num > highest_ingredient_num:
            highest_ingredient_num = current_ingredient_num
            allergic_ingredient_candidate = ingredient
    allergen_dict[allergen] = allergic_ingredient_candidate
    real_allergen_list.append(allergic_ingredient_candidate)
print(allergen_dict)
print(real_allergen_list)
counter = 0
for i in range(len(ingredient_lists)):
    for ingredient in ingredient_lists[i]:
        if ingredient in real_allergen_list:
            continue
        counter +=  1
print(counter)
