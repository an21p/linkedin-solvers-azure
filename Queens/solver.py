
from .utils import image_to_grid_array_auto, grid_array_to_png

QUEEN_VALUE = True

def hasQueen(value):
    """
    Check if the value is a queen.
    """
    return value == QUEEN_VALUE or (isinstance(value, tuple) and value[1] == QUEEN_VALUE)

class Solver:
    def __init__(self, blob):
        self.palette, self.arr = image_to_grid_array_auto(blob)
        assert len(self.palette) == len(self.arr)

    def place(self, row, matrix, colors):
        n = len(matrix)

        if row == n:
            return True
        
        for col in range(n):           
            color_key, _ = matrix[row][col]
            if self.isSafe(row, col, matrix) and not color_key in colors:
                matrix[row][col] = (color_key, QUEEN_VALUE)
                colors.add(color_key)
                if self.place(row+1, matrix, colors):
                    return True
                matrix[row][col] = (color_key, False)
                colors.remove(color_key)
        return False

    def isSafe(self, row, col, matrix):
        n = len(matrix)

        # check uppen col
        for i in range(row):
            if hasQueen(matrix[i][col]):
                return False

        # check diagonals
        if col-1 >= 0 and hasQueen(matrix[row-1][col-1]):
            return False
        if col+1 < n and hasQueen(matrix[row-1][col+1]):
            return False
        
        return True


    def solve(self):
        colors = set()
        solution = [[x for x in y] for y in self.arr]

        # If the solution exists
        if self.place(0, solution, colors):
            return grid_array_to_png(self.arr, self.palette), \
                    grid_array_to_png(solution, self.palette)
            
        else:
            return None, None


if __name__ == "__main__":
    # Example usage
    import sys

    # if len(sys.argv) != 2:
    #     print("Usage: python solver.py <image_path>")
    #     sys.exit(1)

    image_path = sys.argv[1] if len(sys.argv) > 1 else "/Users/pishias/code/python/queens/data/0_input.png"
    with open(image_path, "rb") as f:
        image_blob = f.read()

    solver = Solver(image_blob)
    matrix, solution = solver.solve()

    if solution and matrix:
        with open("output/2_solution.png", "wb") as f:
            f.write(solution)
        with open("output/1_matrix.png", "wb") as f:
            f.write(matrix)
        print("Solution found and saved as solution.png and matrix.png")
    else:
        print("No solution found.")
