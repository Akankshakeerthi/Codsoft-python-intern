class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks[task] = False  # False indicates task is not completed
            print(f'Task "{task}" added successfully.')
        else:
            print(f'Task "{task}" already exists.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for task, completed in self.tasks.items():
                status = 'Completed' if completed else 'Not Completed'
                print(f'- {task} ({status})')

    def mark_as_completed(self, task):
        if task in self.tasks:
            self.tasks[task] = True
            print(f'Task "{task}" marked as completed.')
        else:
            print(f'Task "{task}" not found.')

def main():
    todo_list = ToDoList()

    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
        elif choice == '3':
            task = input("Enter the task to mark as completed: ")
            todo_list.mark_as_completed(task)
        elif choice == '4':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
