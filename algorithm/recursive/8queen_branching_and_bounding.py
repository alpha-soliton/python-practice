class Nqueen:
    def __init__(self, length: int) -> None:
        self.length = length
        self.pos = [0] * self.length
        self.flag_row = [False] * self.length
        self.flag_diagonal_1 =  [False] * (self.length * 2 - 1) # / direction
        self.flag_diagonal_2 =  [False] * (self.length * 2 - 1) # \ direction   
        self.ans_count = 0

    def put(self) -> None:
        for i in range(self.length):
            print(f'{self.pos[i]:2}', end=' ')
        print()

    def put(self) -> None:
        for j in range(self.length):
            for i in range(self.length):
                print('■' if self.pos[i] == j else '□', end = '')
            print()
        print()

    def set(self, i: int) -> None:
        for j in range(self.length):
            if (not self.flag_row[j] and not self.flag_diagonal_1[i + j]
                    and not self.flag_diagonal_2[i - j + self.length-1]):
                self.pos[i] = j
                if i == self.length-1:
                    self.ans_count += 1
                    self.put()
                else:
                    self.flag_row[j] = self.flag_diagonal_1[i+j] = self.flag_diagonal_2[i-j+self.length-1] = True
                    self.set(i + 1)
                    self.flag_row[j] = self.flag_diagonal_1[i+j] = self.flag_diagonal_2[i-j+self.length-1] = False

    def print_ans_num(self) -> None:
        print(f'The answer is {self.ans_count} ways.')

if __name__ == '__main__':
    length = int(input('Input the length of the board : '))
    nquenn = Nqueen(length)
    nquenn.set(0)
    nquenn.print_ans_num()
