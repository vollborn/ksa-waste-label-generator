import os
import sqlite3
import sys

from src.helpers.DirectoryHelper import DirectoryHelper


class Database:
    file = "ksa.sqlite"
    connection = None
    cursor = None

    def __init__(self):
        basePath = os.path.dirname(sys.argv[0])
        self.connection = sqlite3.connect(os.path.join(basePath, self.file))
        self.cursor = self.connection.cursor()
        self.migrate()

    def migrate(self):
        basePath = os.path.dirname(sys.argv[0])
        files = DirectoryHelper.files(
            "sql",
            os.path.join(basePath, "src", "migrations")
        )

        for file in files:
            with open(file) as stream:
                content = stream.read()
                self.cursor.execute(content)

    def execute(self, query, values=()):
        return self.connection.execute(query, values)

    def fetchone(self, query, values=()):
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        return cursor.fetchone()
