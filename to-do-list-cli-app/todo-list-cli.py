tasks=[]


while True:
    print("\n To-Do list menu: ")
    print("1. Add Task: ")
    print("2. View Tasks: ")
    print("3. Remove Tasks: ")
    print("4. Exit")

    choose = input("Choose an option: ")

    if choose=="1":
        task = input("Enter new Task: ")
        tasks.append(task)
        print("New Task added!")


    elif choose=="2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour tasks")
            for i ,task in enumerate(tasks,1):
                print(f" {i}. {task}")


    elif choose=="3":
        for i,task in enumerate(tasks,1):
            print(f"{i}.{task}")
            task_num = int (input("Enter task number to remove: "))
            tasks.pop(task_num-1)
            print("Task Removed!")


    elif choose=="4":
        print("GoodBye!")
        break

    else :
        print("Invalid Option:")

