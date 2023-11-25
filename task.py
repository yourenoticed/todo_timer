class Task():
    def __init__(self, name: str, description: str, completion: bool, deadline=None, total_time=0, id=0):
        self.id = id
        self.name = name
        self.description = description
        self.completion = completion
        self.deadline = deadline
        self.total_time = total_time
    
    def __str__(self):
        return self.name
    
    def change_description(self, final: str):
        self.description = final
    
    def change_completion(self):
        self.completion = self.completion == False
