f = open('input.txt', 'r')
raw = f.readlines()
instructions = [ line.strip('\n') for line in raw ]
print(f'A total of {len(raw)} lines in this boot code.')
operations = [ instruction.split(' ')[0] for instruction in instructions ]
arguments = [ instruction.split(' ')[1] for instruction in instructions ]
accumulator = 0
executed_lines = []
current_line = 0
def processArgument(number, argument):
    if argument[0] == '-':
        number = number - int(argument[1:])
    if argument[0] == '+':
        number = number + int(argument[1:])
    return number
while True:
    if current_line in executed_lines:
        break
    executed_lines.append(current_line)
    operation = operations[current_line]
    argument = arguments[current_line]
    if operation == 'acc':
        accumulator = processArgument(accumulator, argument)
        current_line += 1
    if operation == 'jmp':
        current_line = processArgument(current_line, argument)
    if operation == 'nop':
        current_line += 1
print(accumulator)
f.close()
