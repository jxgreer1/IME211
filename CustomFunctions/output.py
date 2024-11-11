def display_results(results):
    if not results:
        print("No results to display.")
        return

    print("\nCalculation Results:")
    for key, value in results.items():
        print(f"{key}: {value:.2f}")
