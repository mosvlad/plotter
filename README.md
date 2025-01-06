# Equation Plotter GUI

A Python-based graphical user interface for plotting mathematical equations and functions. This application allows users to visualize various mathematical expressions with an intuitive interface.

## Screenshots

### Main Application Window
![Main Interface](screenshots/main_interface.png)
*The main interface showing equation input, range controls, and plot area*


## Features

- Interactive equation input
- Customizable plot range
- Support for multiple mathematical functions
- Real-time visualization
- Built-in help system

## Supported Mathematical Functions

- Basic Operations: +, -, *, /, ** (power)
- Trigonometric: sin(), cos(), tan()
- Hyperbolic: sinh(), cosh(), tanh()
- Exponential and Logarithmic: exp(), log(), log10()
- Other: sqrt(), abs()
- Constants: pi, e

## Prerequisites

- Python 3.x
- Required Python packages:
  ```bash
  numpy
  matplotlib
  tkinter
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mosvlad/plotter.git
   cd plotter
   ```

2. Install the required packages:
   ```bash
   pip install numpy matplotlib
   ```
   Note: tkinter usually comes with Python installation

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Enter your equation in the input field:
   - Use 'x' as the variable
   - Example: x**2 + sin(x)

3. Set the x-axis range:
   - Default range is -10 to 10
   - Modify as needed for your equation

4. Click 'Plot' to visualize the equation

5. Use the 'Help' button to view available functions and syntax

## Example Equations

```
x**2 + sin(x)           # Quadratic with sine wave
sin(x) * cos(x)         # Product of trigonometric functions
exp(-x**2/2)           # Gaussian curve
sqrt(abs(x)) + sin(x)   # Combined functions
```

## GUI Components

- Equation Input Field: Enter your mathematical expression
- Range Input: Set the x-axis plotting range
- Plot Button: Generate the visualization
- Help Button: Display available functions and syntax
- Graph Area: Shows the plotted equation

## Error Handling

The application includes robust error handling for:
- Invalid mathematical expressions
- Incorrect input ranges
- Undefined mathematical operations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License

## Acknowledgments

- Built using Python's tkinter for GUI
- Matplotlib for plotting capabilities
- NumPy for mathematical operations

## Future Enhancements

- Support for multiple equation plotting
- Additional mathematical functions
- Plot customization options
- Export plot functionality
- Save/load equation presets