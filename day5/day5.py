from collections import Counter

def get_endpoints(input_line):
    line = input_line.strip().replace(' -> ', ',')
    line = line.split(',')
    return [ int(i) for i in line ]

def get_coordinates(line):
    return line[0], line[1], line[2], line[3]

def is_diagonal(line):
    x1,y1,x2,y2 = get_coordinates(line)
    return abs(y2-y1) == abs(x2-x1)

def is_vertical_or_horizontal(line):
    x1,y1,x2,y2 = get_coordinates(line)
    return (x1 == x2 or y1 == y2)

def is_valid(line):
    return is_diagonal(line) or is_vertical_or_horizontal(line)

def get_points_for_line(line):
    x1,y1,x2,y2 = get_coordinates(line)
    x_step = -1 if x1 > x2 else 1
    y_step = -1 if y1 > y2 else 1

    points = []
    if is_diagonal(line):
        for i in range(abs(x2-x1)):
            points.append((x1 + x_step*i, y1 + y_step*i))
    else:
        if x1 == x2:
            points.extend([ (x1, y) for y in range(y1, y2, y_step) ])
        elif y1 == y2:
            points.extend([ (x, y1) for x in range(x1, x2, x_step) ])
    
    #include endpoints
    points.append((x1,y1))
    points.append((x2,y2))

    #remove deuplicates
    points = list(set(points))
    return sorted(points)

def get_points(validator=is_vertical_or_horizontal):
    with open('input.txt', 'r') as file:
        input = file.readlines()

    endpoints = [ get_endpoints(line) for line in input ]
    endpoints = list(filter(validator, endpoints))

    points = []
    for line in endpoints:
        points.extend(get_points_for_line(line))

    return points

def get_danger(points):
    #print(points)
    danger_points = [ point for point, count in Counter(points).items() if count > 1 ]
    #[ print(point, count) for point, count in Counter(points).items() ]
    return len(danger_points)

def part1():
    points = get_points()
    return get_danger(points)

def part2():
    points = get_points(is_valid)
    return get_danger(points)

#print(is_diagonal([0,4,4,0]), get_points_for_line([0,4,4,0]))
print(part1())
print(part2())