tasks=[]
def addtask():
    task=input("Enter your task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
    
def viewtasks():
    if  not tasks:
        print("There is no tasks to do.")
    else:
        print("Tasks to be done:")
        for i,task in enumerate(tasks):
            print(f"{i+1}. {task}")
def removetask():
    try:
        tasktoremove= int(input("Enter a number to delete: "))
        tasktoremove=tasktoremove-1
        if tasktoremove >= 0 and tasktoremove <= len(tasks):
            print(f"Task {tasktoremove+1}. {tasks[tasktoremove]} has been removed.")
            tasks.pop(tasktoremove)
        else:
            print(f"Task number {tasktoremove} was not found.")
    except:
        print("Invalid input")
        
if __name__=="__main__":
    print("welcome to the to do list app")
    while True:
        print("\nPlease select your option")
        print("----------------------------")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Quit")
        print("----------------------------")
        choice= input("Enter your choice: ")
        if choice=="1":
            addtask()
        elif choice=="2":
            removetask()
        elif choice=="3":
            viewtasks()
        elif choice=="4":
            print("Exicted sucessfully.")
            break
        else:
            print("Invalid choice. try again")