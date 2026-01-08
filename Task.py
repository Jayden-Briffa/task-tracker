class Task:
    new_id = 0

    def __init__(self, description: str, priority: str):
        self.id = Task.gen_id()
        self.description = description
        self.priority = priority
        self.status = False

    def __str__(self):
        return "\n--".join([f"--id: {self.id}", f"description: {self.description}", f"priority: {self.priority}", f"status: { 'Complete' if self.status else 'Incomplete' }"])

    @staticmethod
    def gen_id():
        Task.new_id = Task.new_id + 1
        return Task.new_id

# jobs = [Task("banana", 2), Task("apple", 3), Task("orange", 1)]

# for job in jobs:
#   prior_queue.put(job)

# while 1:
#     try:
#       popped_item = prior_queue.get_nowait()
#       print(popped_item.description)
#     except Empty:
#       break