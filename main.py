import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math


class EquationPlotterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Equation Plotter")
        self.root.geometry("800x800")

        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.setup_equation_input()
        self.setup_range_input()
        self.setup_plot_button()
        self.setup_plot_canvas()
        self.setup_help_button()
        self.define_available_functions()

    def setup_equation_input(self):
        equation_frame = ttk.LabelFrame(self.main_frame, text="Input Equation", padding="5")
        equation_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        equation_label = ttk.Label(equation_frame, text="y =")
        equation_label.grid(row=0, column=0, padx=5)

        self.equation_var = tk.StringVar(value="x**2 + sin(x)")
        self.equation_entry = ttk.Entry(equation_frame, textvariable=self.equation_var, width=50)
        self.equation_entry.grid(row=0, column=1, padx=5)

    def setup_range_input(self):
        range_frame = ttk.LabelFrame(self.main_frame, text="Plot Range", padding="5")
        range_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        range_label = ttk.Label(range_frame, text="X Range:")
        range_label.grid(row=0, column=0, padx=5)

        self.x_min_var = tk.StringVar(value="-10")
        self.x_max_var = tk.StringVar(value="10")

        x_min_entry = ttk.Entry(range_frame, textvariable=self.x_min_var, width=10)
        x_min_entry.grid(row=0, column=1, padx=5)

        range_separator = ttk.Label(range_frame, text="to")
        range_separator.grid(row=0, column=2, padx=5)

        x_max_entry = ttk.Entry(range_frame, textvariable=self.x_max_var, width=10)
        x_max_entry.grid(row=0, column=3, padx=5)

    def setup_plot_button(self):
        plot_button = ttk.Button(self.main_frame, text="Plot", command=self.plot_equation)
        plot_button.grid(row=2, column=0, columnspan=2, pady=10)

    def setup_plot_canvas(self):
        self.figure, self.ax = plt.subplots(figsize=(8, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.main_frame)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

    def setup_help_button(self):
        help_button = ttk.Button(self.main_frame, text="Help", command=self.show_help)
        help_button.grid(row=4, column=0, columnspan=2, pady=5)

    def define_available_functions(self):
        self.functions_text = """Available functions:
• Basic: +, -, *, /, **, sqrt()
• Trigonometric: sin(), cos(), tan()
• Hyperbolic: sinh(), cosh(), tanh()
• Exponential: exp(), log(), log10()
• Constants: pi, e
Example: x**2 + sin(x) + 2*cos(x)"""

    def evaluate_equation(self, equation_str, x):
        safe_mathematical_functions = {
            'x': x,
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'exp': np.exp,
            'log': np.log,
            'log10': np.log10,
            'sqrt': np.sqrt,
            'pi': np.pi,
            'e': np.e,
            'sinh': np.sinh,
            'cosh': np.cosh,
            'tanh': np.tanh,
            'abs': abs
        }

        try:
            return eval(equation_str, {"__builtins__": {}}, safe_mathematical_functions)
        except Exception as e:
            raise ValueError(f"Error evaluating equation: {str(e)}")

    def plot_equation(self):
        try:
            self.ax.clear()
            x_range_start = float(self.x_min_var.get())
            x_range_end = float(self.x_max_var.get())
            x_values = np.linspace(x_range_start, x_range_end, 1000)

            equation_input = self.equation_var.get()
            y_values = self.evaluate_equation(equation_input, x_values)

            self.create_plot(x_values, y_values, equation_input)
            self.canvas.draw()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def create_plot(self, x_values, y_values, equation_text):
        self.ax.plot(x_values, y_values, 'b-', label=f'y = {equation_text}')
        self.ax.grid(True, alpha=0.3)
        self.ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        self.ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_title(f'Plot of y = {equation_text}')
        self.ax.legend()

    def show_help(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Help")
        help_window.geometry("250x250")

        help_text = ttk.Label(help_window, text=self.functions_text, justify=tk.LEFT)
        help_text.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = EquationPlotterGUI(root)
    root.mainloop()