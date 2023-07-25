import numpy as np

class MatrixApp:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = None
        self.steps = []

    def get_minor(self, row, col):
        return np.delete(np.delete(self.matrix, row, axis=0), col, axis=1)

    def get_input(self, input_matrix):
        self.matrix = np.array(input_matrix, dtype=int)