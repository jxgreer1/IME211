def get_input():
    print("Welcome! This calculator provides geometric values based on a given shape and radius.")
    shapes = ["circle", "sphere"]

    while True:
        shape = input("Enter the shape (circle/sphere): ")
        if shape in shapes:
            break
        print("Invalid shape. Please select either 'circle' or 'sphere'.")

    while True:
        radius_input = input("Enter the radius: ")
        if radius_input.isdigit() or (radius_input.replace('.', '', 1).isdigit() and radius_input.count('.') < 2):
            #https://www.pythoncheatsheet.org/builtin/issubclass#examples
            radius = float(radius_input)
            if radius > 0:
                break
        print("Invalid input. Please enter a positive numerical value.")

    return shape, radius

if __name__ == "__main__":
    shape, radius = get_input()
    print(f'You have selected a {shape} with a radius of {radius}.')
