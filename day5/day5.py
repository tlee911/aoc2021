def get_endpoints(input_line):
    line = input_line.strip().replace(' -> ', ',')
    line = line.split(',')
    return line

def get_coordinates(line):
    line = [ int(i) for i in line ]
    return line[0], line[1], line[2], line[3]

def is_line_valid(line):
    x1,y1,x2,y2 = get_coordinates(line)
    return (x1 == x2 or y1 == y2)

def get_points_for_line(line):
    assert is_line_valid(line)
    x1,y1,x2,y2 = get_coordinates(line)

    if x1 == x2:
        step = -1 if y1 > y2 else 1
        points = [ (x1, y) for y in range(y1, y2, step) ]
    elif y1 == y2:
        step = -1 if x1 > x2 else 1
        points = [ (x, y1) for x in range(x1, x2, step) ]
    
    #include endpoints
    points.append((x1,y1))
    points.append((x2,y2))

    #remove deuplicates
    points = list(set(points))
    return sorted(points)

def get_points():
    with open('input.txt', 'r') as file:
        input = file.readlines()

    endpoints = [ get_endpoints(line) for line in input ]
    endpoints = list(filter(is_line_valid, endpoints))

    points = []
    for line in endpoints:
        points.extend(get_points_for_line(line))

    return points


def part1():
    points = get_points()
    keys = sorted(list(set(points)))

    print(len(points), len(keys))

    i = 0
    danger = 0
    for point in keys:
        c = points.count(point)
        if i % 1000 == 0:
            print(i, point, c)
        if c > 1:
            danger += 1
        i += 1
    return danger

def part2():
    return

print(part1())
#print(part2())