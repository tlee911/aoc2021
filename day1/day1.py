with open('input.txt', 'r') as file:
    input = file.readlines()

input = [ int(i.rstrip()) for i in input ]

def part1():
    increases = 0
    for i in range(1,len(input)-1):
        if input[i-1] < input[i]:
            increases += 1
    return increases

def part2(window=3):
    increases = 0
    for i in range(len(input)):
        try:
            input[i+window]
        except IndexError:
            break
        value = sum(input[i:i+window])
        next_value = sum(input[i+1:i+1+window])
        if next_value > value:
            increases += 1
    return increases

print(part2())