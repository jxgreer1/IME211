def getType():
    while True:  #loop to keep asking for apartments
        try:
            # Display the type of Apartments
            print("\nType of Apartments for Rent:")
            print("1) Studio")
            print("2) One-Bedroom")
            print("3) Two-Bedroom")
            print("4) EXIT PROGRAM")

            # Ask what apartment the user wants
            kind = int(input("Enter the type of apartment you wish to rent (1-3 or 4 to EXIT PROGRAM): "))

            # If the user selects 4 leave the program
            if kind == 4:
                print("Exiting program. Thank you!")
                exit()

            # check that the user selected an actual input 1-3
            if kind not in [1, 2, 3]:
                print("Invalid apartment type. Please enter 1, 2, or 3.")
                continue  # restart if not valid

            # check if user wants furnished
            furnished = input("Do you want the apartment furnished (Y/N)? ")

            # check furnished input
            if furnished not in ['Y', 'N']:
                print("Invalid input. Please enter 'Y' or 'N'.")
                continue  # loop if not valid

            # return the apartment and if its furnished/unfurnished
            return kind, furnished
        except ValueError:
            # NO LETTERS
            print("Invalid input. Please enter apartment type.")


# determine rent based off type and furnished
def determineRent(kind, furnished):
    # dict of all possible answers
    apartment_details = [
        {"type": "Studio", "deposit": 800, "unfurnished": 1200, "furnished": 1500},
        {"type": "One-Bedroom", "deposit": 1000, "unfurnished": 1500, "furnished": 1800},
        {"type": "Two-Bedroom", "deposit": 1200, "unfurnished": 1850, "furnished": 2050}
    ]
    # dict to respond to right type
    apartment = apartment_details[kind - 1]  # Subtract 1 to adjust for zero-based indexing.

    # is it furnished y or n
    rent = apartment["furnished"] if furnished == 'Y' else apartment["unfurnished"]
    # Get deposit
    deposit = apartment["deposit"]

    # return all the numbers
    return apartment["type"], rent, deposit


#display the rent, furnished, type, and the deposit
def displayRent(apartment_type, furnished, rent, deposit):
    # Determine if the apartment is furnished
    furnishing_status = "Furnished" if furnished == 'Y' else "Unfurnished"

    # Display it all
    print(f"\nDescription : {apartment_type} {furnishing_status}")
    print(f"Deposit     : ${deposit}")
    print(f"Rent        : ${rent}\n")


#Main function that controls everything
def main():
    while True:
        print("IME-211-01 – Rent Challenge\nBy Jack Greer")
        print("Due November 21st 2024\n")
        print(" ***************************************")
        print(" *          SMITH HOME REALTY          *")
        print(" ***************************************")
        kind, furnished = getType()

        apartment_type, rent, deposit = determineRent(kind, furnished)
        displayRent(apartment_type, furnished, rent, deposit)



if __name__ == "__main__":
    main()







