f = open("001input.txt",'r')
expense = f.readlines()
expense = [ int(num.strip()) for num in expense ]
print(f"A total of {len(expense)} lines are in the file")
solved = 0
for i,num1 in enumerate(expense):
    print(f"Examing the {i} number")
    for j in range(i, len(expense)):
        num2 = expense[j]
        sum = num1 + num2
        print(sum)
        if sum == 2020:
            mul = num1 * num2
            print(mul)
            solved = 1
            break
    if solved  == 1:
        break
f.close()
