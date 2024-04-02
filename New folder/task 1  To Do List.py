class Task:
    def __init__(self, name, description, due_date, priority):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.done = False
def add_task(tasks):
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    tasks.append(Task(name, description, due_date, priority))
    print("Task added successfully!")
def display_tasks(tasks):
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task.name} - {task.description} - Due: {task.due_date} - Priority: {task.priority} - {'Done' if task.done else 'Not Done'}")
def main():
    tasks = []
    while True:
        print("\nTODO LIST")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
