import math
import statistics

with open('input.txt', 'r') as file:
    input = file.readlines()

input = [ line.strip() for line in input ]
input = [ int(i) for i in input[0].split(',')]

def part1():
    median = int(statistics.median(input))
    print(median)
    distances = [ abs(i - median) for i in input ]
    return sum(distances)

def get_fuel(a):
    distances = [ abs(i - a) for i in input ]
    fuel = [ (d+1)*(d/2) for d in distances ] 
    return int(sum(fuel))

def part2():
    mean = statistics.mean(input) 
    print(mean)
    a = get_fuel(int(mean))
    b = get_fuel(math.ceil(mean))
    return min(a,b)

print(part1())
print(part2())