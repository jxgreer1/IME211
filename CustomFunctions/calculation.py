import math

def calculate_values(shape, radius):
    calculations = {
        "circle": {
            "Diameter": 2 * radius,
            "Circumference": 2 * math.pi * radius,
            "Area": math.pi * radius ** 2
        },
        "sphere": {
            "Diameter": 2 * radius,
            "Surface Area": 4 * math.pi * radius ** 2,
            "Volume": (4/3) * math.pi * radius ** 3
        }
    }
    return calculations.get(shape, {})
