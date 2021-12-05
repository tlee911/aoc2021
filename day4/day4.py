class Board():
    def __init__(self, numbers):
        '''
        <numbers> should be a list of integers to form a square of length <size>
        '''
        self.numbers = [ int(i) for i in numbers ]
        assert len(numbers) == 25
        self.size = 5 #hardcode to avoid sqrt float precision issues
        self.marked = [ 0 for i in numbers ]
        self.last_marked = None

    def mark(self, number):
        '''
        Mark a number on the bingo board, and check if that makes bingo
        '''
        if number in self.numbers:
            self.marked[self.numbers.index(number)] = 1
            self.last_marked = number
        return self.is_bingo()

    def is_bingo(self):
        marked = self.marked.copy()
        rows = []
        while len(marked) >= self.size:
            rows.append(marked[:self.size])
            marked = marked[self.size:]
        #print(rows)

        marked = self.marked.copy()
        columns = []
        for i in range(self.size):
            column = []
            for j in range(self.size):
                column.append(marked[i + (j * self.size)])
            columns.append(column)
        #print(columns)

        row_sums = [ sum(row) for row in rows ]
        col_sums = [ sum(col) for col in columns ]
        sums = row_sums + col_sums
        #print(len(row_sums), len(col_sums))
        return True if self.size in sums else False

    def get_unmarked_numbers(self):
        unmarked = []
        for i in range(len(self.numbers)):
            if self.marked[i] == 0:
                unmarked.append(self.numbers[i])
        return unmarked

    def sum_unmarked(self):
        return sum(self.get_unmarked_numbers())

    def get_score(self):
        if not self.is_bingo():
            print('WARN: Getting score of non-winning board')
        return self.last_marked * self.sum_unmarked()

    def find_bingo(self, calls):
        '''
        Given a list of called numbers, find the index at which bingo occurs
        '''
        for i in range(len(calls)):
            call = calls[i]
            #print(call)
            if self.mark(call):
                return i
        return None
            


def get_boards(contents, board_length=25):
    boards = []
    numbers = []

    for line in contents:
        line = line.strip()
        
        if line:
            line = [ int(i) for i in line.split() ]
            numbers.extend(line)

    #assert len(numbers) == 2500        
    while len(numbers) >= board_length:
        board = Board(numbers[:board_length])
        boards.append(board)
        numbers = numbers[board_length:]

    #assert len(boards) == 100
    return boards
        
def get_first_bingo(boards):
    for call in calls:
        #print(call)
        for board in boards:
            #print(board.marked)
            if board.mark(call):
                print('BINGO! Number: {call}, Board: {board}'.format(call=call, board=boards.index(board)))
                return board
    return None


with open('input.txt', 'r') as file:
    input = file.readlines()

calls = [ int(i) for i in input[0].strip().split(',') ]
boards = get_boards(input[1:])


def part1():
    board = get_first_bingo(boards)
    return board.get_score()

def part2():
    bingo_indexes = [ board.find_bingo(calls) for board in boards ]
    last_bingo = max(bingo_indexes)
    #print(bingo_indexes.index(last_bingo))
    board = boards[bingo_indexes.index(last_bingo)]
    return board.get_score()

print(part1())
print(part2())