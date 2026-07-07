doneTasks = []
unDoneTasks = []

def addTask(input):
    unDoneTasks.append(input)
    print("Task added! ")
def removeTask(input):
    if (input in unDoneTasks):
        unDoneTasks.remove(input)
        print("Task removed! ")
    else:
        print("Not a task currently! ")
def viewTask():
    print(unDoneTasks)
def viewDoneTask():
    print(doneTasks)
def markTask(input):
    unDoneTasks.remove(input)
    doneTasks.append(input)
    print("Task marked completed! ")
inp = input("Would you like to add a task(a), remove a task(r), view your tasks(v), mark a task done(m), view done tasks (d) or finish (done)? ").lower()
while (inp!="done"):
    if inp=="a":
        inpA = input("What is the name of your task you add? ").lower()
        addTask(inpA)
    elif inp=="r":
        inpR = input("What is the name of your task would like to remove? ").lower()
        removeTask(inpR)
    elif inp=="v":
        viewTask()
    elif inp=="d":
        viewDoneTask()
    elif inp=="m":
        print(unDoneTasks)
        inpM = input("What is the name of your task would like to have completed? ").lower()
        markTask(inpM)
    else:
        print("Invalid choice!")
    inp = input("Would you like to add a task(a), remove a task(r), view your tasks(v), mark a task done(m), view done tasks (d) or finish (done)? ").lower()
print("Thanks for using this program! ")
