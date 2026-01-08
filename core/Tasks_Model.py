from queue import PriorityQueue as Priority_Queue
from core.Task import Task

class Tasks_Model:
    def __init__(self):
        self.current = {}
        self.priority_idx = Priority_Queue()

    # Return True if there are no more tasks in priority_idx
    def empty(self) -> bool:
        return self.priority_idx.empty()

    # Add a new key:value pair to current and a corresponding index to priority_idx
    def add_task(self, description: str, priority: int) -> Task:
        new_task = Task(description, priority)
        self.current[new_task.id] = new_task
        self.priority_idx.put_nowait((new_task.priority, new_task.id))

        return self.current[new_task.id]
    
    # Pop and return the task with the lowest priority value
    def get_task_by_priority(self) -> Task:
        priority_task = self.priority_idx.get_nowait()
        found_task = self.current[priority_task[1]]

        return found_task

    def get_task_by_id(self, id: int) -> Task:
        found_task = self.current[id]
        return found_task
    
    def complete_task(self, id: int) -> Task:
        self.current[id].status = True
    
        return self.current[id]
