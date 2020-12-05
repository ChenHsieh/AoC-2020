f = open('input.txt', 'r')
raw = f.read()
raw = raw.replace("F", "0")
raw = raw.replace("B", "1")
raw = raw.replace("L", "0")
raw = raw.replace("R", "1")
entries = raw.split('\n')[:-1]

print(f"A total of {len(entries)} entriess in this data.")

seat_ID_list =[]
for entry in entries:
    row_digits = entry[:7]
    col_digits = entry[7:]
    row = int(row_digits, 2)
    col = int(col_digits, 2)
    seat_ID = row * 8 + col
    seat_ID_list.append(seat_ID)
seat_ID_list.sort()
row_min = seat_ID_list[0]/8
seat_ID_min = row_min * 8 + 7
for i, seat_ID in enumerate(seat_ID_list):
    if seat_ID <= seat_ID_min:
        continue
    if seat_ID + 1 == seat_ID_list[i+1]:
        continue
    print(seat_ID + 1)
    break
    
