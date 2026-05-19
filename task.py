from datetime import datetime

class Task:
    def __init__(self, task_id, description, status ="todo"):
        self.id = task_id
        self.description = description
        self.status = status
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat(),
        }
    @classmethod
    def from_dict(cls, data):
        task = cls(data["id"], data["description"], data["status"])
        return task