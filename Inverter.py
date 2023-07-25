import numpy as np
from Adjoint import Adjoint
class Inverter(Adjoint):

    def invert(self):
        adjoint = self.find_adjoint()
        determinant = np.linalg.det(adjoint)

        if determinant == 0:
            raise ValueError("The matrix is not invertible.")
        else:
            inverse_matrix = adjoint / determinant
            return inverse_matrix


    def out_putI(self):
        invert1 = self.invert()
        print(invert1)
    
    def main(self):
        try:
            self.out_putI()
        except ValueError as e:
            print(f"Error: {e}")
    

if __name__ == "__main__":
    pass

    
