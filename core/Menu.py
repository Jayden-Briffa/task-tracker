class Menu:
    HEADER_BUFFER = "="*10
    OPTION_BUFFER = "-"*2 + " "
    ERR_BUFFER = "*" * 2

    def __init__(self, choices: dict) -> None:
        self.menu_choices = choices
        self.options = choices.keys()
        
    # Output menu and get user's choice
    def get_user_menu_choice(self) -> str:
        print("\n", self.HEADER_BUFFER, "What would you like to do?", self.HEADER_BUFFER)

        # Dynamically output choices based on self.menu_choices
        for choice, description in self.menu_choices.items():
            print(f"{self.OPTION_BUFFER}{choice}: {description}")
                  
        return input()
    
    # Output custom error message for feedback
    def err(self, msg: str) -> None:
        print(self.ERR_BUFFER, "ERROR", msg, self.ERR_BUFFER)