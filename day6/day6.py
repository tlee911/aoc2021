class Fish:
    def __init__(self, ages):
        self.start = ages
        self.day = 0
        self.new = 8 #start counter
        self.rollover = 6
        self.pop_counter = {}
        for i in range(self.new + 1):
            self.pop_counter[i] = self.start.count(i)
        #print(self.pop_counter)

    def next_day(self):
        new_pop = {}
        for i in range(1, self.new+1):
            new_pop[i-1] = self.pop_counter[i]
        new_pop[self.new] = self.pop_counter[0]
        new_pop[self.rollover] += self.pop_counter[0]
        self.pop_counter = new_pop
        self.day += 1
        return new_pop

    def get_pop_counter_at_day(self, day):
        for i in range(day):
            self.next_day()
        return self.pop_counter

    def get_pop_at_day(self, day):
        counter = self.get_pop_counter_at_day(day)
        return sum(counter.values())



with open('input.txt', 'r') as file:
    input = file.readlines()

input = input[0].strip().split(',')
input = [ int(i) for i in input ]

test_input = [3,4,3,1,2]

TEST = False
input = test_input if TEST else input

def part1():
    fish1 = Fish(input)
    return fish1.get_pop_at_day(80)

def part2():
    fish2 = Fish(input)
    return fish2.get_pop_at_day(256)

print(part1())
print(part2())