import os
import json

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['description']} - {'Done' if task['completed'] else 'Not Done'}")

def add_task(tasks, description):
    task = {"description": description, "completed": False}
    tasks.append(task)
    print(f"Task added: {description}")
    save_tasks(tasks)

def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task deleted: {deleted_task['description']}")
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def mark_completed(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["completed"] = True
        print(f"Task marked as completed: {tasks[index - 1]['description']}")
        save_tasks(tasks)
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == "3":
            index = int(input("Enter the task index to delete: "))
            delete_task(tasks, index)
        elif choice == "4":
            index = int(input("Enter the task index to mark as completed: "))
            mark_completed(tasks, index)
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
