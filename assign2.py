tasks = []
def menu():
    print("Welcome!")
    print("1. Add Task:")
    print("2. View Task:")
    print("3 .Delete Task:")
    print("4. Close Task:")

def add_task():
        task = input("add task:")
        tasks.append(task)
        print("task added")

def view_tasks():
    if not tasks:
        print("No tasks!")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks,):
            print(f"{index}. {task}")

def delete_task():
    if not tasks:
        print("No tasks!")
    else:
        view_tasks()
        try:
            task_index = int(input("Enter the task to delete:"))
            if task_index < 1 :
                print("Invalid number. Try again.")
            else:
                deleted_task = tasks.pop(task_index - 1)
                print(f"Task '{deleted_task}' deleted!")
        except (ZeroDivisionError , ValueError):
            print("Error!")

def main_menu():
    while True:
        menu()
        choice= input("enter 1-4 : ")

        if choice == '1':add_task()
        elif choice == '2':view_tasks()
        elif choice == '3':delete_task()
        elif choice == '4':
            print("Closing!")
            break
        else:
            print("Not an option!")
main_menu()