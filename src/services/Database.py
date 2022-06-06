import os
import sqlite3
import sys


class Database:
    file = "ksa.sqlite"
    connection = None
    cursor = None
    config = None

    def __init__(self, config):
        basePath = os.path.dirname(sys.argv[0])
        self.connection = sqlite3.connect(os.path.join(basePath, self.file))
        self.cursor = self.connection.cursor()
        self.config = config
        self.migrate()

    def migrate(self):
        self.cursor.executescript(self.config.get("migrations.queries"))

    def execute(self, query, values=()):
        return self.connection.execute(query, values)

    def fetchone(self, query, values=()):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        return cursor.fetchone()

    def fetchall(self, query, values=()):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        return cursor.fetchall()
