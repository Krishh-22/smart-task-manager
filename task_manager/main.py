from task import Task
from storage import save_tasks, load_tasks

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return
    for i, task in enumerate(tasks):
        status = "✓" if task.completed else "✗"
        overdue = " (OVERDUE)" if task.is_overdue() else " "
        print(f"{i+1}. [{status}] {task.title} | Priority: {task.priority} | Deadline: {task.deadline}")

def search_tasks(tasks):
    keyword = input("Enter keyword to search: ").lower()
    found = []

    for task in tasks:
        if keyword in task.title.lower():
            found.append(task)

    display_tasks(found)

def show_overdue(tasks):
    overdue_tasks = [task for task in tasks if task.is_overdue()]
    print("\nOverdue Tasks:")
    display_tasks(overdue_tasks)

def show_statistics(tasks):
    total = len(tasks)
    completed = len([task for task in tasks if task.completed])
    pending = total - completed

    if total > 0:
        completion_rate = (completed / total) * 100
    else:
        completion_rate = 0

    print("\nTask Statistics")
    print("Total tasks:", total)
    print("Completed tasks:", completed)
    print("Pending tasks:", pending)
    print("Completion rate:", round(completion_rate, 2), "%")

def main():
    tasks = load_tasks()

    while True:
        print("\n====== SMART TASK MANAGER ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Show Overdue Tasks")
        print("7. Show Statistics")
        print("8. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Task title: ")
            priority = input("Priority (Low/Medium/High): ")
            deadline = input("Deadline (YYYY-MM-DD): ")

            task = Task(title, priority, deadline)
            tasks.append(task)

            save_tasks(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            num = int(input("Task number to mark complete: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num].mark_complete()
                save_tasks(tasks)

        elif choice == "4":
            display_tasks(tasks)
            num = int(input("Task number to delete: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
                save_tasks(tasks)

        elif choice == "5":
            search_tasks(tasks)

        elif choice == "6":
            show_overdue(tasks)

        elif choice == "7":
            show_statistics(tasks)

        elif choice == "8":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()