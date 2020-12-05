f = open('input.txt', 'r')
raw = f.read()
raw = raw.replace("F", "0")
raw = raw.replace("B", "1")
raw = raw.replace("L", "0")
raw = raw.replace("R", "1")
entries = raw.split('\n')[:-1]

print(f"A total of {len(entries)} entriess in this data.")

highest_num = 0
for entry in entries:
    row_digits = entry[:7]
    col_digits = entry[7:]
    row = int(row_digits, 2)
    col = int(col_digits, 2)
    seat_ID = row * 8 + col
    if seat_ID > highest_num:
        highest_num = seat_ID
print(highest_num)
