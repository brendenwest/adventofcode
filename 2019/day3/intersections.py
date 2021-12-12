
# part 1
def _getPoints(moves):
    moves = moves.split(",")
    points = set()
    position = [0,0]

    for move in moves:
        direction = move[0]
        distance = int(move[1:])
        for n in range(distance):
            if direction == "R":
                position[0] += 1
            elif direction == "L":
                position[0] -= 1
            elif direction == "U":
                position[1] += 1
            elif direction == "D":
                position[1] -= 1
            position = [position[0],position[1]]
            points.add("{0}_{1}".format(position[0],position[1]))
    return points

# part 2
def getPoints(moves):
    moves = moves.split(",")
    points = {}
    position = [0,0]
    steps = 0

    for move in moves:
        direction = move[0]
        distance = int(move[1:])

        for n in range(distance):
            steps += 1
            if direction == "R":
                position[0] += 1
            elif direction == "L":
                position[0] -= 1
            elif direction == "U":
                position[1] += 1
            elif direction == "D":
                position[1] -= 1
            position = [position[0],position[1]]
            key = "{0}_{1}".format(position[0],position[1])
            if not points.get(key):
                points[key] = steps
    return points

def _minDistance(points1, points2):
    origin = [0,0]
    min = None
    for i in points1.intersection(points2):
        point = i.split("_")
        distance = abs(int(point[0]) - origin[0]) + abs(int(point[1])-origin[1])
        if not min or distance < min:
            min = distance
    return min

def minDistance(points1, points2):
    origin = [0,0]
    min = None
    for key in set(points1).intersection(points2):
        steps = points1[key] + points2[key]
        if not min or steps < min:
            min = steps
    return min

inputs = open("input.txt", "r").readlines()
points1 = getPoints(inputs[0])
points2 = getPoints(inputs[1])
min = minDistance(points1, points2)
print("min =",min)
