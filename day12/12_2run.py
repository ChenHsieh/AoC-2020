f = open('input.txt', 'r')
raw = f.read()
actions = [ sequence[0] for sequence in raw.split('\n')[:-1] ]
values = [ int(sequence[1:]) for sequence in raw.split('\n')[:-1] ]
print(f'A total of {len(actions)} actions in this file')
class Ship():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1
    def executeAction(self, action, value):
        if action == 'N':
            self.waypoint_y += value
        if action == 'S':
            self.waypoint_y -= value
        if action == 'E':
            self.waypoint_x += value
        if action == 'W':
            self.waypoint_x -= value
        if action == 'L':
            counter_clockwise_step = int(value/90)
            self.rotateWaypoint(4-counter_clockwise_step)
        if action == 'R':
            clockwise_step = int(value/90)
            self.rotateWaypoint(clockwise_step)
        if action == 'F':
            self.x = self.x + (self.waypoint_x * value)
            self.y = self.y + (self.waypoint_y * value)
    def rotateWaypoint(self, clockwise_step):
        new_x = (-0.5-(((-1)**clockwise_step)/2))*self.waypoint_x + (2-clockwise_step)*self.waypoint_y
        new_y = (clockwise_step-2)*self.waypoint_x + (-0.5-(((-1)**clockwise_step)/2))*self.waypoint_y
        self.waypoint_x = new_x
        self.waypoint_y = new_y
ship = Ship()
for i in range(len(actions)):
    action = actions[i]
    value = values[i]
    ship.executeAction(action, value)
manhattanDistance = abs(ship.x) + abs(ship.y)
print(manhattanDistance)
