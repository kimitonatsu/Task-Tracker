from task import Task
from datetime import datetime
import json

class TaskManager:
    def __init__(self):
        self.next_id = 1
        self.tasks = []
        self.load_from_file()

    def save_to_file(self, filename = "tasks.json"):
        data = [task.to_dict() for task in self.tasks]
        with open(filename, "w") as f:
            json.dump(data, f, indent = 2)
    def load_from_file(self, filename = "tasks.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.tasks = [Task.from_dict(task_json) for task_json in data]

            if self.tasks:
                self.next_id = max(task.id for task in self.tasks) + 1

        except FileNotFoundError:
            self.tasks = []
            self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        print(f"Task added successfully (ID: {self.next_id})")
        self.next_id += 1
        self.save_to_file()

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Task with ID {task_id} deleted successfully")
                self.save_to_file()
                return
    def list_tasks(self, status = ""):
        if status == "" or status is None:
            for task in self.tasks:
                print(task.to_dict())
            return
        for task in self.tasks:
            if task.status == status:
                print(task.to_dict())
    def update_task(self, task_id, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                task.updatedAt = datetime.now()
                print(f"Task with ID {task_id} updated successfully")
                self.save_to_file()
                return
    def mark_in_progress(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "in_progress"
                print(f"Task with ID {task_id} marked as in progress")
                self.save_to_file()
                return
    def mark_done(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "done"
                print(f"Task with ID {task_id} marked as done")
                self.save_to_file()
                return