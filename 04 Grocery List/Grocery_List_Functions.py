# Grocery_List_Functions.py
# To test, run Grocery_List_Main.py

def add_item(grocery_list, item):

    grocery_list.append(item)

    return grocery_list


def delete_item(grocery_list, item):

    grocery_list.remove(item)

    return grocery_list


def replace_item(grocery_list, old_item, new_item):

    grocery_list.replace(old_item, new_item)

    return grocery_list


def subset_list(grocery_list, start_item, end_item):
    # Using the 'grocery_list' list, 'start_item', and 'end_item' variables,
    # Create a new list variable that includes all the items from the start_item to the end_item (inclusive)
    # Store this new list as 'subset_grocery_list'

    subset_grocery_list = grocery_list[start_item:end_item]

    return subset_grocery_list


def get_first_item(grocery_list):
    # Using the 'grocery_list' list, variable, store the first item in the list as 'first_item'

    first_item=grocery_list[0]

    return first_item


def get_last_item(grocery_list):
    # Using the 'grocery_list' list, variable, store the last item in the list as 'last_item'

    last_item=grocery_list[-1]

    return last_item
