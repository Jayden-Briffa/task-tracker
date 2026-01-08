from Menu import Menu
from Tasks_Model import Tasks_Model
from Validator import Validator

MENU_CHOICES = {
    "1": "Add a new task",
    "2": "Retrieve next task",
    "3": "Retrieve task by ID",
    "4": "Mark a task as complete"
}

client = Tasks_Model()
main_menu = Menu(MENU_CHOICES)

client.add_task("kiwi", 3)
client.add_task("apple", 2)
client.add_task("orange", 3)
client.add_task("banana", 1)

user_choice = None
while user_choice != "quit":
    user_choice = main_menu.get_user_menu_choice()
    flag = False

    match user_choice:

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

                print(new_task)


        case "2":
            if (client.empty()):
                main_menu.err("The task queue is empty")
                flag = True

            if (not flag):
                next_task = client.get_task_by_priority()
                print(next_task)

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


        case _:
            main_menu.err(f"Your choice '{user_choice}' is invalid. You can only choose: '{main_menu.choices}'")

exit()