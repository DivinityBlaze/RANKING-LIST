rank_list = []

while True:
    print("\nMenu:")
    print("1. Print List")
    print("2. Add Item to End")
    print("3. Remove Last Item")
    print("4. Insert at Position")
    print("5. Remove at Position")
    print("6. Move to Position")
    print("7. Edit Item")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        if rank_list:
            for i in range(len(rank_list)):
                print(str(i + 1) + ". " + rank_list[i])
        else:
            print("The ranking list is empty.")

    elif choice == '2':
        item = input("Enter an item to add: ")
        rank_list.append(item)
        print("Item added.")

    elif choice == '3':
        if rank_list:
            removed_item = rank_list.pop()
            print("Removed:", removed_item)
        else:
            print("The ranking list is already empty.")

    elif choice == '4':
        position = int(input("Enter the position to insert: "))
        item = input("Enter the item to insert: ")
        rank_list.insert(position - 1, item)
        print("Item inserted.")

    elif choice == '5':
        position = int(input("Enter the position to remove: "))
        if 1 <= position <= len(rank_list):
            removed_item = rank_list[position - 1]
            rank_list.remove(removed_item)
            print("Removed:", removed_item)
        else:
            print("Invalid position.")

    elif choice == '6':
        from_position = int(input("Enter the position to move from: "))
        to_position = int(input("Enter the position to move to: "))
        if 1 <= from_position <= len(rank_list) and 1 <= to_position <= len(rank_list):
            item = rank_list.pop(from_position - 1)
            rank_list.insert(to_position - 1, item)
            print("Item moved.")
        else:
            print("Invalid positions.")

    elif choice == '7':
        position = int(input("Enter the position to edit: "))
        if 1 <= position <= len(rank_list):
            new_item = input("Enter the new item: ")
            rank_list[position - 1] = new_item
            print("Item edited.")
        else:
            print("Invalid position.")

    elif choice == '8':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")