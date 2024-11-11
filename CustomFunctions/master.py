from input import get_input
from calculation import calculate_values
from output import display_results

def main():
    shape, radius = get_input()
    results = calculate_values(shape, radius)
    display_results(results)

if __name__ == "__main__":
    main()
