tasks = []

while True:
    print("\n------ TO-DO LIST MENU ------")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done ✔")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter a choice between 1 to 5: ")

    # Add task
    if choice == "1":
        task_name = input("Enter task name: ")
        tasks.append({"name": task_name, "done": False})
        print("Task is added!")

    # View task
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                status = "✔" if tasks[i]["done"] else "❌"
                print(i + 1, ".", tasks[i]["name"], status)

    # Mark task as completed
    elif choice == "3":
        if len(tasks) == 0:
            print("No task to mark.")
        else:
            for i in range(len(tasks)):
                status = "✔" if tasks[i]["done"] else "❌"
                print(i + 1, ".", tasks[i]["name"], status)

            num = int(input("Enter task number to mark as done: "))
            if num > 0 and num <= len(tasks):
                tasks[num - 1]["done"] = True
                print("Task marked as done ✔")
            else:
                print("Invalid task number.")

    # Delete task
    elif choice == "4":
        if len(tasks) == 0:
            print("No task to delete.")
        else:
            for i in range(len(tasks)):
                status = "✔" if tasks[i]["done"] else "❌"
                print(i + 1, ".", tasks[i]["name"], status)

            num = int(input("Enter task number to delete: "))
            if num > 0 and num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Deleted task:", removed["name"])
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":
        print("Good Bye!")
        break

    else:
        print("Invalid choice. Enter 1 to 5.")
