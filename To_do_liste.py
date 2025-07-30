my_list = []

def add_item():
    item = input("Enter item to add: ")
    my_list.append({"task": item, "done": False})
    print(f"'{item}' has been added to the list.")

def show_list():
    if my_list:
        print("\nCurrent List:")
        for i, entry in enumerate(my_list, start=1):
            status = "[✔]" if entry["done"] else "[ ]"
            print(f"{i}. {status} {entry['task']}")
    else:
        print("The list is empty.")

def mark_done():
    show_list()
    if not my_list:
        return
    try:
        index = int(input("Enter task number to mark as done: "))
        if 1 <= index <= len(my_list):
            my_list[index - 1]["done"] = True
            print(f"Task {index} marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_list()
    if not my_list:
        return
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(my_list):
            removed = my_list.pop(index - 1)
            print(f"'{removed['task']}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("\n===== LIST MENU =====")
    print("1. Add item to list")
    print("2. Show list")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            show_list()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1 to 5.")

if __name__ == "__main__":
    main()
