import os

class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.save_tasks()

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                status = "1" if task["completed"] else "0"
                file.write(f"{status},{task['task']}\n")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    status, task = line.strip().split(",", 1)
                    self.tasks.append({"task": task, "completed": status == "1"})
