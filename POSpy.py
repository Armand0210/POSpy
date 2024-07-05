items_list = []

#add items
def add_item(item):
    try:
        name, price_str = item.rsplit(' ', 1)
        price = float(price_str)
        items_list.append((name, price))
        print(f"Added {name} {price_str} to the list.")
    except ValueError:
        print(f"Invalid input format. Please enter item name and price (e.g., Cheese R50.00).")

#remove items
def remove_item(item):
    for i, (name, price) in enumerate(items_list):
        if name == item:
            del items_list[i]
            print(f"Removed {item} from the list.")
            return
    print(f"{item} is not in the list.")

def display_items_and_total():
    if not items_list:
        print("No items in the list.")
        return
    
    total = 0
    print("Items in the list:")
    for name, price in items_list:
        total += price
        print(f"{name} R{price:.2f}")
    
    print("---------------")
    print(f"Total R{total:.2f}")

#run the POS system
def run_pos_system():
    while True:
        print("\nWelcome to the POS system!")
        print("1. Add item")
        print("2. Remove item")
        print("3. Display items and total")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            item = input("Enter item name and price (e.g., Cheese R50.00): ")
            add_item(item)
        elif choice == '2':
            item = input("Enter item name to remove: ")
            remove_item(item)
        elif choice == '3':
            display_items_and_total()
        elif choice == '4':
            print("Exiting POS system. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")

#start the POS system
if __name__ == "__main__":
    run_pos_system()
