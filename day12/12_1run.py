f = open('input.txt', 'r')
raw = f.read()
actions = [ sequence[0] for sequence in raw.split('\n')[:-1] ]
values = [ int(sequence[1:]) for sequence in raw.split('\n')[:-1] ]
print(f'A total of {len(actions)} actions in this file')
facing_sequence = [ 'N', 'E', 'S', 'W' ]
facing_dict = {
    'N':0,
    'E':1,
    'S':2,
    'W':3
}
class Ship():
    def __init__(self):
        self.current_x = 0
        self.current_y = 0
        self.current_facing = 'E'
    def updateLocation(self, action, value):
        if action == 'N':
            self.current_y += value
        if action == 'S':
            self.current_y -= value
        if action == 'E':
            self.current_x += value
        if action == 'W':
            self.current_x -= value
        if action == 'L':
            clockwise_step = value/90
            self.current_facing = facing_sequence[int((facing_dict[self.current_facing] - clockwise_step)%4)]
        if action == 'R':
            clockwise_step = value/90
            self.current_facing = facing_sequence[int((facing_dict[self.current_facing] + clockwise_step)%4)]
        if action == 'F':
            self.updateLocation(self.current_facing, value)
ship = Ship()
for i in range(len(actions)):
    action = actions[i]
    value = values[i]
    ship.updateLocation(action, value)
manhattanDistance = abs(ship.current_x) + abs(ship.current_y)
print(manhattanDistance)
