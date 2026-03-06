from datetime import datetime

class Task:
    def __init__(self, title, priority="Medium", deadline=None):
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "deadline": self.deadline,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(
            data["title"],
            data["priority"],
            data["deadline"]
        )
        task.completed = data["completed"]
        return task