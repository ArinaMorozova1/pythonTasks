class Matrix:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__lines = []
        
        for _ in range(rows):
            self.__lines.append([0] * cols)

    def __getitem__(self, index):
        i, j = index
        return self.__lines[i][j]

    def __setitem__(self, index, value):
        i, j = index
        self.__lines[i][j] = value

    def rows(self):
        return self.__rows

    def cols(self):
        return self.__cols

    def print(self):
        for line in self.__lines:
            print(*line)
            
    def transpose(self):
        rows = self.__rows
        cols = self.__cols
            
        self.__lines = [[self.__lines[j][i] for j in range(rows)]
                                for i in range(cols)]

        self.__rows = cols
        self.__cols = rows

class SparseMatrix:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__items = {}

    def __getitem__(self, index):
        if index in self.__items:
            return self.__items[index]
        
        self.__items[index] = 0
        return self.__items[index]
    
    def __setitem__(self, index, value):
        self.__items[index] = value
            
    def rows(self):
        return self.__rows

    def cols(self):
        return self.__cols

    def print(self):
        for i in range(self.__rows):
            for j in range(self.__cols):
                if (i, j) not in self.__items:
                    self.__items[(i, j)] = 0
                print(self.__items[(i, j)], end=' ')
            print()
            
    def transpose(self):
        new_items = self.__items
        self.__items = {}
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__items[(j, i)] = new_items[(i, j)]  
    
        self.__cols, self.__rows = self.__rows, self.__cols
