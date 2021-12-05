with open('input.txt', 'r') as file:
    input = file.readlines()

input = [ step.split() for step in input ]
input = [ {step[0]: int(step[1])} for step in input ]

def part1():
    x = 0
    y = 0
    for step in input:
        x += step.get('forward', 0)
        y += step.get('down', 0)
        y -= step.get('up', 0)
    print(x,y)
    return x * y

def part2():
    x = 0
    y = 0
    a = 0
    for step in input:
        x += step.get('forward', 0)
        y += step.get('forward', 0) * a

        #y += step.get('down', 0)
        a += step.get('down', 0)

        #y -= step.get('up', 0)
        a -= step.get('up', 0)
    print(x,y,a)
    return x * y

print(part2())