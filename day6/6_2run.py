f = open('input.txt', 'r')
raw = f.read().split('\n\n')
groups = [ group.strip() for group in raw ]
print(f"A total of {len(groups)} groups in this dataset.")
count_sum = 0

for group in groups:
    answers = group.split('\n')
    consensus_answer = answers[0]
    for answer in answers:
        consensus_answer = set(consensus_answer).intersection(answer)
    count = len(set(consensus_answer))
    count_sum += count

print(count_sum)
f.close()
