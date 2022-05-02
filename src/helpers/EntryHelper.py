import sqlite3


class EntryHelper:
    @staticmethod
    def handle(dictionary, cli, database):
        obj = EntryHelper.get_object(database, dictionary)
        if not obj:
            obj = EntryHelper.create_object(database, dictionary)

        EntryHelper.add_bins_to_object(database, obj, dictionary)

    @staticmethod
    def add_bins_to_object(database, obj, dictionary):
        query = "INSERT INTO bins VALUES ("
        bin_type = EntryHelper.get_bin_type(database, dictionary)

        for _ in dictionary['anzahl']:
            query += ""

        query += ")"
        database.connection.execute(query, dictionary["objekt_nr"])

    @staticmethod
    def get_object(database, dictionary):
        query = "SELECT * FROM objects WHERE number = ?"
        cursor: sqlite3.Cursor = database.connection.execute(query, dictionary["objekt_nr"])

        result = cursor.fetchone()
        return result

    @staticmethod
    def create_object(database, dictionary):
        return 0

    @staticmethod
    def get_bin_type(database, dictionary):
        return 0

    @staticmethod
    def create_bin_type(database, dictionary):
        return 0

    @staticmethod
    def get_waste_type(database, dictionary):
        return 0

    @staticmethod
    def create_waste_type(database, dictionary):
        return 0

    @staticmethod
    def get_address(database, dictionary):
        return 0

    @staticmethod
    def create_address(database, dictionary):
        return 0

    @staticmethod
    def get_street(database, dictionary):
        return 0

    @staticmethod
    def create_street(database, dictionary):
        return 0

    @staticmethod
    def get_city(database, dictionary):
        return 0

    @staticmethod
    def create_city(database, dictionary):
        return 0
