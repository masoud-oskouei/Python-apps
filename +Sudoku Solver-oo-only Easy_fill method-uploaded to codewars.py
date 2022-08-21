class sudoku_game:
    def __init__(self,input_chart):
        self.board=[]
        self.temp=[]
        self.blanks = []
        for i in range(9):
            for j in range(9):
                self.board.append(input_chart[i][j])
        for i in range(81):
            self.temp.append(0)
        self.Box_indexes=[]
        for i in range(0,9,3):
            for j in range(0,9,3):
                self.Box_indexes.append((i,j))

    def draw(self,chart):
        for i in range(9):
            for j in range(9):
                print(f'{chart[self.ind(i,j)]} ',end="")
            print()
        print('-'*20)
    def ind(self,i,j):
        return (9*i+j)
    def count_in_row(self,array,row,num):
        count=0
        for column in range(9):
            if array[self.ind(row,column)]==num:
                count+=1
        return count
    def count_in_column(self,array,column,num):
        count=0
        for row in range(9):
            if array[self.ind(row,column)]==num:
                count+=1
        return count
    def count_in_box(self,array,box,num):
        count=0
        for row in range(box[0],box[0]+3):
            for column in range(box[1], box[1] + 3):
                if array[self.ind(row,column)]==num:
                    count+=1
        return count



    def uni_in_groups(self,array,num):
        for row in range(9):
            if self.count_in_row(array,row, num) > 1:
                return False
        for column in range(9):
            if self.count_in_column(array,column,num)>1: return False
        for box in self.Box_indexes:
            if self.count_in_box(array,box,num)>1: return False
        return True
    def mark_off(self,num):
        for row in range(9):
            if self.count_in_row(self.board,row,num)>0:
                for column in range(9):
                    self.temp[self.ind(row,column)]=11
        for column in range(9):
            if self.count_in_column(self.board,column,num)>0:
                for row in range(9):
                    self.temp[self.ind(row,column)]=11
        for box in self.Box_indexes:
            if self.count_in_box(self.board,box, num) > 0:
                for row in range(box[0], box[0] + 3):
                    for column in range(box[1], box[1] + 3):
                        self.temp[self.ind(row, column)] =11
        for i in range(81):
            if self.board[i]!=0:
                self.temp[i]=11

    def easy_fill(self):
        for num in range(1,10):
            self.temp = list(0 for x in range(81))  # reset temp
            self.mark_off(num)
            for row in range(9):
                if self.count_in_row(self.temp,row,0) == 1:
                    for column in range(9):
                        if self.temp[self.ind(row, column)] == 0:
                            self.board[self.ind(row, column)] = num

            for column in range(9):
                if self.count_in_column(self.temp,column,0) == 1:
                    for row in range(9):
                        if self.temp[self.ind(row, column)] == 0:
                            self.board[self.ind(row, column)] = num
            for box in self.Box_indexes:
                if self.count_in_box(self.temp,box, 0) == 1:
                    for row in range(box[0],box[0]+3):
                        for column in range(box[1], box[1] + 3):
                            if self.temp[self.ind(row, column)] == 0:
                                self.board[self.ind(row, column)] = num
    def easy_solve(self):
        prev_board=[]
        while sum(self.board)<405 and prev_board!=self.board:
            prev_board=self.board.copy()
            self.easy_fill()
        if sum(self.board)==405:
            print(" It is Solved with easy_fill method!")
        else:
            print(' We cannot go further using easy_fill method')
    def export(self):
        output=[]
        for i in range(9):
            ln=[]
            for j in range(9):
                ln.append(self.board[9*i+j])
            output.append(ln.copy())
        return output





def sudoku(array):
    game1=sudoku_game(array)
    print("initial state")
    game1.draw(game1.board)
    game1.easy_solve()
    print('resulted state')
    print(game1.export())
    return (game1.export())

''' cut here if you want to upload to codewars!!'''
sudoku([[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]])


















