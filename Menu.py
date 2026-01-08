class Menu:
    MENU_BUFFER = 10
    def get_user_input(self, menu_choices):
        print("="*Menu.MENU_BUFFER, "What would you like to do?", "="*MENU_BUFFER)
        return