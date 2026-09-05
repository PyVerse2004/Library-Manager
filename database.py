import sqlite3

class Database:
    def connector(self):
        self.connection = sqlite3.connect("library.db")

    def cursoring(self):
        self.cursor = self.connection.cursor()

    def create_table(self):
        pass