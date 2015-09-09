class DataAccessor:

    def __init__(self, filename):
        self.filename = filename

    def add_task(self, task):
        with open(self.filename, "a") as todo_storage_file:
            todo_storage_file.write(task + '\n')
            todo_storage_file.close()

    def delete_task(self, task_index):
        with open(self.filename, "r") as todo_storage_file:
            items = enumerate(todo_storage_file.readlines(), start=1)
            todo_storage_file.close()

            with open(self.filename, "w") as todo_storage_file:
                for i, line in items:
                    if i != int(task_index):
                        todo_storage_file.write(line)
                todo_storage_file.close()

    def get_all_tasks(self):
        with open(self.filename, "r") as todo_storage_file:
            all_tasks = enumerate(todo_storage_file.readlines(), start=1)
            todo_storage_file.close()

        return all_tasks

    def clear_all_tasks(self):
        with open(self.filename, "w") as todo_storage_file:
            todo_storage_file.close()

