from converter import Converter  # Assuming the Converter class is in a file called converter.py

def main():
    print_instructions()

def print_instructions():
    print("Welcome to the Converter, Sorter, and Solver tool!")
    print("To use the converter, call the convert() function with the following arguments:")
    print("convert(from_unit, to_unit, value)")
    print("Where:")
    print("- from_unit: 'dec' for Decimal, 'bin' for Binary, 'hex' for Hexadecimal")
    print("- to_unit: 'dec' for Decimal, 'bin' for Binary, 'hex' for Hexadecimal")
    print("- value: the value to be converted (integer for Decimal, string for Binary/Hexadecimal)")

    print("\nTo use the sorter, call the sort() function with the following arguments:")
    print("sort(sort_type, data)")
    print("Where:")
    print("- sort_type: 'dict' for Dictionary, 'list' for List")
    print("- data: the data to be sorted (dictionary or list, provided in Python syntax)")

    print("\nTo solve an equation, call the solve_equation() function with the equation as a string argument.")
    print("For example:")
    print('solve_equation("2 * x + 3")')

    print("\nTo solve an inequality, call the solve_inequality() function with the inequality as a string argument.")
    print("For example:")
    print('solve_inequality("x >= 5")')

def convert(from_unit, to_unit, value):
    return Converter.convert(from_unit, to_unit, value)

def sort(sort_type, data):
    return Converter.sort(sort_type, data)

def solve_equation(equation):
    return Converter.solve_equation(equation)

def solve_inequality(inequality):
    return Converter.solve_inequality(inequality)

if __name__ == "__main__":
    main()