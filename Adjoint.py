import numpy as np
from Main import MatrixApp
class Adjoint(MatrixApp):

    def find_adjoint(self):
        n = len(self.matrix)
        adjoint = np.zeros((n, n), dtype=int)

        for i in range(n):
            for j in range(n):
                minor = self.get_minor(i, j)
                cofactor = (-1) ** (i + j) * np.linalg.det(minor)
                adjoint[j, i] = cofactor
                self.steps.append((i, j, minor.tolist(), cofactor))

        return adjoint

    
    def out_putA(self):
        adjoint_matrix = self.find_adjoint()
        print(adjoint_matrix)
    
    def main(self):
        try:
            self.out_putA()
        except ValueError as e:
            print(f"Error: {e}")
    
if __name__ == "__main__":
    pass

