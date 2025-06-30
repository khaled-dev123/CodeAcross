# Simple To-Do List Program
my_list = []


def add_item():
    item = input("Enter item to add: ")
    my_list.append(item)
    print(f"'{item}' has been added to the list.")


def show_list():
    if my_list:
        print("\nCurrent List:")
        for i, item in enumerate(my_list, start=1):
            print(f"{i}. {item}")
    else:
        print("The list is empty.")


def show_menu():
    print("\n===== LIST MENU =====")
    print("1. Add item to list")
    print("2. Show list")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            show_list()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
