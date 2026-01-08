class Task:
    new_id = 0

    def __init__(self, description: str, priority: str):
        self.id = Task.gen_id()
        self.description = description
        self.priority = priority
        self.status = False

    def __str__(self):
        return "\n--".join([
            f"--id: {self.id}", 
            f"description: {self.description}", 
            f"priority: {self.priority}", 
            f"status: {'Complete' if self.status else 'Incomplete' }"]) # Map True to "Complete" and False to "Incomplete"
    
    @staticmethod
    def gen_id():
        Task.new_id = Task.new_id + 1
        return Task.new_id