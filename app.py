from flask import Flask, render_template, request, jsonify
from sympy import sympify, solve, diff, integrate, Symbol
import numpy as np

app = Flask(__name__)

def calculate_expression(expression):
    try:
        # Convert the expression to a SymPy object
        expr = sympify(expression)
        # Evaluate the expression
        result = float(expr.evalf())
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

def solve_equation(equation):
    try:
        # Split the equation into left and right sides
        left, right = equation.split('=')
        # Convert to SymPy expressions
        left_expr = sympify(left)
        right_expr = sympify(right)
        # Solve the equation
        solution = solve(left_expr - right_expr)
        return {"success": True, "result": [float(sol.evalf()) for sol in solution]}
    except Exception as e:
        return {"success": False, "error": str(e)}

def calculate_derivative(expression, variable='x'):
    try:
        # Convert the expression to a SymPy object
        expr = sympify(expression)
        # Calculate derivative
        derivative = diff(expr, variable)
        return {"success": True, "result": str(derivative)}
    except Exception as e:
        return {"success": False, "error": str(e)}

def calculate_integral(expression, variable='x'):
    try:
        # Create a symbol for the variable
        x = Symbol(variable)
        # Convert the expression to a SymPy object
        expr = sympify(expression)
        # Calculate indefinite integral
        integral = integrate(expr, x)
        return {"success": True, "result": str(integral)}
    except Exception as e:
        return {"success": False, "error": f"Error calculating integral: {str(e)}. Please enter a valid mathematical expression (e.g., x**2, sin(x), etc.)"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression')
    operation = data.get('operation', 'calculate')
    
    if operation == 'calculate':
        return jsonify(calculate_expression(expression))
    elif operation == 'solve':
        return jsonify(solve_equation(expression))
    elif operation == 'derivative':
        return jsonify(calculate_derivative(expression))
    elif operation == 'integral':
        return jsonify(calculate_integral(expression))
    else:
        return jsonify({"success": False, "error": "Invalid operation"})

if __name__ == '__main__':
    app.run(debug=True)