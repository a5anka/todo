import sqlite3

class DataAccessor:

    def __init__(self, filename):
        self.filename = filename
        conn = sqlite3.connect(filename)
        conn.execute('''CREATE TABLE IF NOT EXISTS ITEMS
        (ID INTEGER PRIMARY KEY,
        DESC           TEXT    NOT NULL);''')
        conn.close()

    def add_task(self, task):
        conn = sqlite3.connect(self.filename)
        cursor = conn.execute("INSERT INTO ITEMS (DESC) VALUES ('" + task + "')")
        conn.commit()
        conn.close()

    def delete_task(self, task_index):
        conn = sqlite3.connect(self.filename)
        cursor = conn.execute("DELETE FROM ITEMS WHERE ID=" + task_index)
        conn.commit()
        conn.close()

    def get_all_tasks(self):
        conn = sqlite3.connect(self.filename)
        cursor = conn.execute("SELECT ID, DESC FROM ITEMS")
        all_tasks = []
        for row in cursor:
            all_tasks.append((row[0], row[1]))
        conn.close()

        return all_tasks

    def clear_all_tasks(self):
        conn = sqlite3.connect(self.filename)
        cursor = conn.execute("DELETE FROM ITEMS")
        conn.commit()
        conn.close()
