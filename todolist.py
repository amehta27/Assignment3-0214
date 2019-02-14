tasks_array = []
def show_menu():
    print("Press 1 to add a new task:")
    print("Press 2 to delete a task:")
    print("Press 3 to view all the tasks:")
    print("Press q to quit:")

def add_new_task():
    task_name = input("Enter name of task: ")
    task_priority = input("Enter priority:")

    tasks_dictionary = {"title": task_name, "priority": task_priority}

    tasks_array.append(tasks_dictionary)


def view_all_tasks():
    for index in range(0,len(tasks_array)):
        task = tasks_array[index]
        print (f"{index + 1}-{task['title']}-{task['priority']}")

def delete_task():
    for index in range(0,len(tasks_array)):
        task = tasks_array[index]
        print (f"{index + 1}-{task['title']}-{task['priority']}")

    delete_task = int(input("enter the task number to delete it:"))
    del tasks_array[delete_task-1]


user_input = ""

while user_input != "q":
    show_menu()
    user_input = input("Enter your choice: ")

    if user_input == "1":
        add_new_task()
    elif user_input == "2":
          delete_task()
    elif user_input == "3":
         view_all_tasks()
