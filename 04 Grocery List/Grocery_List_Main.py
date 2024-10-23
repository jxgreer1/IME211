# Grocery_List_Main.py

from Grocery_List_Functions import add_item, delete_item, replace_item, subset_list, get_first_item, get_last_item


def main():
    grocery_list = []

    while True:
        print("\nGrocery List Manager")
        print("1. Add item")
        print("2. Delete item")
        print("3. Replace item")
        print("4. Show a subset of the list")
        print("5. Show entire list")
        print("6. Show first item on the list")
        print("7. Show last item on the list")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to add: ")
            grocery_list = add_item(grocery_list, item)
            print(f"{item} added to the list.")

        elif choice == '2':
            item = input("Enter item to delete: ")
            grocery_list = delete_item(grocery_list, item)

        elif choice == '3':
            old_item = input("Enter item to replace: ")
            new_item = input("Enter new item: ")
            grocery_list = replace_item(grocery_list, old_item, new_item)

        elif choice == '4':
            start = input("What item should be the starting item?: ")
            end = input("What item should be the ending item?: ")
            print("Subset of the list:", subset_list(grocery_list, start, end))

        elif choice == '5':
            print("Full Grocery List:", grocery_list)

        elif choice == '6':
            print("First item on the list:", get_first_item(grocery_list))

        elif choice == '7':
            print("Last item on the list:", get_last_item(grocery_list))

        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
