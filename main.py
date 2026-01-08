from core.Menu import Menu
from core.Tasks_Model import Tasks_Model
from core.Validator import Validator

# Choices are passed dynamically in case other menus are needed in future
MENU_CHOICES = {
    "1": "Add a new task",
    "2": "Retrieve next task",
    "3": "Retrieve task by ID",
    "4": "Mark a task as complete",
    "quit": "Exit the program (you will lose all your tasks)"
}

client = Tasks_Model()
main_menu = Menu(MENU_CHOICES)

user_choice = None
while True:
    user_choice = main_menu.get_user_menu_choice()
    flag = False

    match user_choice:

        # Add a new task
        case "1":
            description = input("Enter a description for the new task: ")
            priority = input("Enter a priority for the new task: ")
        
            if (not Validator.isInt(priority)):
                flag = True
                main_menu.err("Field 'priority' must be an integer")
        
            if (Validator.isEmpty(priority)):
                flag = True
                main_menu.err("Field 'priority' must be given")
        
            if (Validator.isEmpty(description)):
                flag = True
                main_menu.err("Field 'description' must be given")
            
            if (not flag):
                priority = int(priority)
                new_task = client.add_task(description, priority)

                print("\nTask successfully created!\n", new_task, sep="")

        # Get next task
        case "2":
            if (client.empty()):
                main_menu.err("The task queue is empty")
                flag = True

            if (not flag):
                next_task = client.get_task_by_priority()
                print(next_task)

        # Get task by ID
        case "3":
            id = input("Enter the task's id: ")

            if (not Validator.isInt(id)):
                main_menu.err("Field 'id' must be an integer")
                flag = True

            if (Validator.isEmpty(id)):
                main_menu.err("Field 'id' must be included")
                flag = True

            if (not flag):
                id = int(id)
                task = client.get_task_by_id(id)
                print(task)

        # Mark task as complete
        case "4":
            id = input("Enter the task's id: ")

            if (not Validator.isInt(id)):
                main_menu.err("Field 'id' must be an integer")
                flag = True

            if (Validator.isEmpty(id)):
                main_menu.err("Field 'id' must be included")
                flag = True

            if (not flag):
                id = int(id)
                task = client.complete_task(id)
                print(task)

        case "quit":
            exit()

        # Tell the user what they can enter if they enter an invalid option
        case _:
            main_menu.err(f"Your choice '{user_choice}' is invalid. You can only choose: '{",".join(main_menu.options)}'")