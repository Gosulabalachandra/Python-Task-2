# Python-Task-2
#This is my Second Task in this Internship
TASKS_FILE = "tasks.txt"
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📋 No tasks found.")
    else:
        print("\n📜 To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
def remove_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"❌ Task removed: {removed}")
    else:
        print("⚠ Invalid task number.")
def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("⚠ Please enter a valid number.")
        elif choice == "4":
            print("👋 Exiting To-Do App. Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please select between 1-4.")

if __name__ == "__main__":
    main()
