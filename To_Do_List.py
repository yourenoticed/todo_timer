class To_Do_List():
	def __init__(self, todo_list):
		self.todo_list = todo_list

	def add_task(self, task):
		self.todo_list.append(task)

	def get_by_id(self, id):
		for task in self.todo_list:
			if task.id == id:
				return task
		return None