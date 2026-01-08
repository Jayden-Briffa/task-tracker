class Menu:
    MENU_BUFFER = 10
    ERR_BUFFER = 3

    def __init__(self, choices: dict) -> None:
        self.menu_choices = choices
        self.choices = choices.keys()
                
    def get_user_menu_choice(self) -> str:
        print("="*Menu.MENU_BUFFER, "What would you like to do?", "="*Menu.MENU_BUFFER)
        return input()
    
    def err(self, msg: str) -> None:
        return msg
