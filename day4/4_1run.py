f = open('input.txt', 'r')
raw = f.read()
raw = raw.split('\n\n')
entries = [ entry.strip().replace('\n', ' ').split() for entry in raw]
print(f"A total of {len(entries)} entriess in this data.")

num_passport = 0
for entry in entries:
    if len(entry) == 8:
        num_passport += 1
        continue
    else:
        fields = [ field.split(':')[0] for field in entry ]
        if (not "cid" in fields) & (len(fields) == 7):
            num_passport += 1
            
print(num_passport)
