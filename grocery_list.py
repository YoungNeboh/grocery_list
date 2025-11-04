# Create a simple menu-based grocery app:
# Add, remove, view items
# Exit with a summary of the list
# Bonus: Prevent duplicate entries, or save list to grocery.txt

def round_up(listed):
    # announce end of item taking, and print out the groceryList
    print("\n Alright that will be all then!")
    print(f"Your finished list is:")
    for i, g in enumerate(listed, start=1):
        print(f"{i}. {g}")
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
    item = input("What would you like to add to your list?(Type 'r' to remove an item) --> ").title()

    # check if 'r' was typed
    if item == "R":
        item = remove_item(groceries)

    # check if item is already in the list
    if item not in groceries:
        groceries.append(item)
        print(f"'{item}' added to your list!")
    else:
        print(f"'{item}' is already in the list")
        reattempt = input("Do you have anything else you'd like to add? yes(y) / no(n)"
                          "(Type 'r' to remove an item) --> ").lower()
        if reattempt == "R":
            item = remove_item(groceries)
        elif reattempt in ("yes", "y"):
            continue
        elif reattempt in ("no", "n"):
            round_up(groceries)
        else:
            print("Please type 'yes' or 'no'")


    # accept other items for the list
    while True:
        next_item = input("\n Would you like to add anything else to your list? yes(y) / no(n) ").lower()
        if next_item in ("yes", "y"):
            break   # go back to top-level loop
        elif next_item in ("no", "n"):
            round_up(groceries)
        else:
            print("Please type in 'yes' or 'no'")
