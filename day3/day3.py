with open('input.txt', 'r') as file:
    input = file.readlines()

input = [ line.strip() for line in input ]

def get_values_at_index(i, l):
    values = []
    for line in l:
        values.append((line[i]))
    return values

def get_counts_at_index(i, l):
    values = get_values_at_index(i, l)
    zero = values.count('0')
    one = values.count('1')
    return (zero, one)

def get_most_common_at_index(i, l):
    zero, one = get_counts_at_index(i, l)
    if zero == one:
        return '1'
    return '1' if one > zero else '0'

def part1():
    gamma = []
    for i in range(len(input[0])):
        gamma.append(get_most_common_at_index(i, input))
    
    epsilon = [ '1' if i=='0' else '0' for i in gamma ]
    gamma = ''.join(gamma)
    epsilon = ''.join(epsilon)
    #print(gamma)
    #print(epsilon)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    #print(gamma, epsilon)
    return gamma * epsilon


def get_least_common_at_index(i, l):
    b = get_most_common_at_index(i, l)
    return '0' if b == '1' else '1'

def get_rating(f):
    input_list = input.copy()
    i = 0
    while len(input_list) > 1:
        keep = []
        keep_value = f(i, input_list)
        for item in input_list:
            if item[i] == keep_value:
                keep.append(item)
        input_list = keep.copy()
        #print(i, len(input_list))
        i += 1
    return int(input_list[0], 2)

def get_o2():
    return get_rating(get_most_common_at_index)

def get_co2():
    return get_rating(get_least_common_at_index)

def part2():
    o2 = get_o2()
    co2 = get_co2()
    print(o2, co2)
    return o2 * co2

print(part1())
print(part2())