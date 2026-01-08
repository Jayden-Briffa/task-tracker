from queue import PriorityQueue as Priority_Queue
from Task import Task

class Tasks_Model:
    def __init__(self):
        self.current = {}
        self.priority_queue = Priority_Queue()

    def empty(self):
        return self.priority_queue.empty()

    def add_task(self, description: str, priority: int) -> Task:
        new_task = Task(description, priority)
        self.current[new_task.id] = new_task
        self.priority_queue.put_nowait((new_task.priority, new_task.id))

        return self.current[new_task.id]
    
    def get_task_by_priority(self) -> Task:
        priority_task = self.priority_queue.get_nowait()
        found_task = self.current[priority_task[1]]

        return found_task

    def get_task_by_id(self, id: int) -> Task:
        found_task = self.current[id]
        return found_task
    
    def complete_task(self, id: int) -> Task:
        self.current[id].status = True
    
        return self.current[id]
