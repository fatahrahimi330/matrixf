from flask import Flask, render_template, request
import numpy as np
from Adjoint import Adjoint
from Inverter import Inverter

app = Flask(__name__)        
@app.route('/', methods=['GET', 'POST'])
def calculate_matrix_operation():
    if request.method == 'POST':
        rows = int(request.form['rows'])
        columns = int(request.form['columns'])
        operation = request.form['operation']  # Get the selected operation from the form

        input_matrix = []
        for i in range(rows):
            row = []
            for j in range(columns):
                try:
                    element = int(request.form[f'element-{i}-{j}'])
                    row.append(element)
                except ValueError:
                    raise ValueError("Invalid input. Please enter an integer.")
            input_matrix.append(row)

        if operation == 'adjoint':
            try:
                adjoint = Adjoint(rows, columns)
                adjoint.get_input(input_matrix)
                adjoint_matrix = adjoint.find_adjoint()

                # Store data for adjoint
                input_matrix_data = adjoint.matrix.tolist()
                adjoint_matrix_data = adjoint_matrix.tolist()
                steps_data = adjoint.steps

                return render_template('result.html', input_matrix_data=input_matrix_data, adjoint_matrix_data=adjoint_matrix_data, steps_data=steps_data)
            except ValueError as e:
                    error_message1 = "only square matrices can have adjoints, and for a square matrix to have an adjoint, it must also be invertible. Non-square matrices do not have adjoints, and the concept of the adjoint is not applicable to them!"
                    return render_template("error.html", error_message1=error_message1)
        elif operation == 'inverse':
            try:
                invert1 = Inverter(rows, columns)
                invert1.get_input(input_matrix)
                inverse_matrix = invert1.invert()

                # Store data for inverse
                input_matrix_data_inverse = invert1.matrix.tolist()
                inverse_matrix_data = inverse_matrix.tolist()
                steps_data_inverse = invert1.steps

                return render_template('result.html', input_matrix_data_inverse=input_matrix_data_inverse, inverse_matrix_data=inverse_matrix_data, steps_data_inverse=steps_data_inverse)
            except ValueError as e:
                error_message = "Not invertible! 'det(A) = 0'"
                return render_template("error.html", error_message=error_message)
    return render_template('index.html')

# ... (Rest of the app setup)

if __name__ == '__main__':
    app.run(debug=True)