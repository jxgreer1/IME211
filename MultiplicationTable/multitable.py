try:

    size = int(input("Please provide the size of the multiplication table: "))

    if size < 0:
        print("Number must be positive.")
    else:

        table = []


        for row in range(size + 1):
            current_row = []
            for i in range(size + 1):
                current_row.append(row * i)
            table.append(current_row)

        for row in table:
            print(row)
except ValueError:
    print("value must me whole.")

