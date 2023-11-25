class Task():
    def __init__(self, name: str, description: str, completion: bool, id=0):
        self.id = id
        self.name = name
        self.description = description
        self.completion = completion
    
    def __str__(self):
        pass
    