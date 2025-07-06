# AI Calculator

A powerful calculator application that uses SymPy for advanced mathematical computations. This calculator can perform basic arithmetic operations, solve equations, calculate derivatives, and compute integrals.

## Features

- Basic arithmetic calculations
- Equation solving
- Derivative calculation
- Integral computation
- Modern and responsive UI
- Error handling and user feedback

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the files
2. Navigate to the project directory
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`
3. Enter your mathematical expression in the input field
4. Select the desired operation (Basic Calc, Solve Equation, Derivative, or Integral)
5. Click the Calculate button to see the result

## Examples

### Basic Calculation
- Input: `2 * 3 + 5`
- Result: `11`

### Solving Equations
- Input: `2*x + 5 = 10`
- Result: `x = 2.5`

### Derivatives
- Input: `x**2 + 2*x + 1`
- Result: `2*x + 2`

### Integrals
- Input: `x**2`
- Result: `x**3/3 + C`

## Error Handling

The calculator provides clear error messages when:
- Invalid mathematical expressions are entered
- Equations cannot be solved
- Derivatives or integrals cannot be computed

## Technologies Used

- Flask (Web framework)
- SymPy (Symbolic mathematics library)
- Bootstrap (UI framework)
- JavaScript (Frontend functionality)

## License

This project is open source and available under the MIT License.