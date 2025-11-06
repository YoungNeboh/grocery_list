# Create a simple menu-based grocery app:
# Add, remove, view items
# Exit with a summary of the list
# Bonus: Prevent duplicate entries, or save list to grocery.txt

def round_up(listed):
    # announce end of item taking, and print out the groceryList
    print("\nAlright, that will be all then!")
    print(f"Your finished list is:")
    for index, grocery_item in enumerate(listed, start=1):
        print(f"{index}. {grocery_item}")
    with open("/Users/macbook/PycharmProjects/personalWork/projects/groceryList/groceries.txt", "w") as file:
        for each in listed:
            file.write(each + "\n")
    exit()


def remove_item(listed):
    if listed:
        to_remove = input("What item would you like to remove? --> ").title()
        if to_remove in listed:
            listed.remove(to_remove)
            print(f"'{to_remove}' has been removed from the list")
        else:
            print(f"'{to_remove}' isn't in the grocery list")
    else:
        print("The list is currently empty")
    return ''


groceries = []
print("Hello! Create your grocery list here!")
while True:
    item = input("What would you like to add to your list?(Type 'r' to remove an item, or 'x' to cancel) --> ").title()


    if item == "R":     # if user wants to remove item
        remove_item(groceries)
        continue
    elif item == "X":   # if user wants to cancel
        if groceries:
            round_up(groceries)
        else:
            print("Your list is currently empty. See you next time!")
            exit()

    # check if item is already in the list
    if item not in groceries:
        groceries.append(item)
        print(f"'{item}' added to your list!")
    else:
        print(f"'{item}' is already in the list")
        reattempt = input("\nDo you have anything else you'd like to add? yes(y) / no(n)"
                          "(Type 'r' to remove an item, or 'x' to cancel) --> ").title()

        if reattempt == "R":  # if user wants to remove item
            remove_item(groceries)
            continue
        elif reattempt == "X":  # if user wants to cancel
            if groceries:
                round_up(groceries)
            else:
                print("Your list is currently empty. See you next time!")
                exit()
        elif reattempt in ("YES", "Y"):     # if user wants to add something to list
            continue
        elif reattempt in ("NO", "N"):      # if user doesn't want to add anything else
            round_up(groceries)
        else:
            print("Please type 'yes' or 'no'")


    # accept other items for the list
    while True:
        next_item = input("\nWould you like to add anything else to your list? yes(y) / no(n)"
                          "(Type 'r' to remove an item, or 'x' to cancel) --> ").title()

        if next_item == "R":  # if user wants to remove item
            remove_item(groceries)
            continue
        elif next_item == "X":  # if user wants to cancel
            if groceries:
                round_up(groceries)
            else:
                print("Your list is currently empty. See you next time!")
                exit()
        elif next_item in ("YES", "Y"):
            break   # go back to top-level loop
        elif next_item in ("NO", "N"):
            round_up(groceries)
        else:
            print("Please type in 'yes' or 'no'")
