# Simple To-Do List Application
def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(task_list):
    task = input("Enter a new task: ")
    task_list.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks(task_list):
    if not task_list:
        print("No tasks in the list!")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def delete_task(task_list):
    view_tasks(task_list)
    if task_list:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(task_list):
                removed_task = task_list.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    task_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task(task_list)
            elif choice == 2:
                view_tasks(task_list)
            elif choice == 3:
                delete_task(task_list)
            elif choice == 4:
                print("Exiting To-Do List Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
