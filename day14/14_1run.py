with open('input.txt', 'r') as f:
    raw = f.read()
sections = raw.split('mask = ')[1:]
memory = {}
def maskValue(value, mask):
    value = bin(value).replace('0b','')
    value = value.zfill(36)
    for i in range(36):
        if mask[i] ==  'X':
            continue
        value = value[:i] + mask[i] + value[i+1:]
    return int(value, 2)   
for section in sections:
    instructions = section.split('mem[')
    mask = instructions[0].strip()
    for instruction in instructions[1:]:
        segment_point = instruction.index(']')
        address = instruction[:segment_point].strip()   
        value = int(instruction[segment_point+4:].strip())
        maskedValue = maskValue(value, mask)
        memory[address] = maskedValue
sum_value = 0
for address, maskedValue in memory.items():
    sum_value += maskedValue
print(sum_value)
