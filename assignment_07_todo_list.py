# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# =============================================================================

def display_menu():
    """Prints the menu options."""
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    """Prompts for a task description and adds it to the list."""
    description = input("Enter task: ")
    tasks.append(description)
    print(f'Task added: "{description}"')


def view_tasks(tasks):
    """Displays all tasks, numbered from 1. Shows a message if empty."""
    if len(tasks) == 0:
        print("Your to-do list is empty. Add a task to get started!")
        return

    print("Your Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks):
    """Shows the list, asks which task number to remove, and removes it."""
    if len(tasks) == 0:
        print("Your to-do list is empty. There's nothing to delete.")
        return

    view_tasks(tasks)
    task_number = int(input("Enter task number to delete: "))

    # Validate the task number is within range
    if task_number < 1 or task_number > len(tasks):
        print("Error: Invalid task number.")
        return

    # Convert to 0-based index and remove
    removed_task = tasks.pop(task_number - 1)
    print(f'Task "{removed_task}" has been removed.')


def main():
    tasks = []

    while True:
        print()
        display_menu()
        choice = input("Enter your choice (1-4): ")
        print()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
