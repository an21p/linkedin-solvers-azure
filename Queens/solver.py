
from .utils import image_to_grid_array_auto, grid_array_to_png

QUEEN_VALUE = -1

class Solver:
    def __init__(self, blob):
        self.palette, self.arr = image_to_grid_array_auto(blob)
        assert len(self.palette) == len(self.arr)

    def place(self, row, matrix, colors):
        n = len(matrix)

        if row == n:
            return True
        
        for col in range(n):            
            if self.isSafe(row, col, matrix) and not matrix[row][col] in colors:
                colour = matrix[row][col]
                matrix[row][col] = QUEEN_VALUE
                colors.add(colour)
                if self.place(row+1, matrix, colors):
                    return True
                matrix[row][col] = colour
                colors.remove(colour)
        return False

    def isSafe(self, row, col, matrix):
        n = len(matrix)

        # check uppen col
        for i in range(row):
            if matrix[i][col] == QUEEN_VALUE:
                return False

        # check diagonals
        if col-1 >= 0 and matrix[row-1][col-1] == QUEEN_VALUE:
            return False
        if col+1 < n and matrix[row-1][col+1] == QUEEN_VALUE:
            return False
        
        return True


    def solve(self):
        colors = set()
        matrix = [[x for x in y] for y in self.arr]

        # If the solution exists
        if self.place(0, matrix, colors):
            return grid_array_to_png(self.arr, self.palette), \
                    grid_array_to_png(matrix, self.palette)
            
        else:
            return None, None

