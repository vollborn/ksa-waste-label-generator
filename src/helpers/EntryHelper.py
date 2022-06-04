from src.services.DependencyInjector import DependencyInjector


class EntryHelper:
    def __init__(self, dictionary, database, cli):
        self.dictionary = dictionary
        self.database = database
        self.cli = cli

    @classmethod
    def handle(cls, dictionary):
        spawned = DependencyInjector.inject(cls.inject, dictionary)
        spawned.execute()

    @classmethod
    def inject(cls, dictionary, database, cli):
        return cls(dictionary, database, cli)

    def execute(self):
        obj = self.get_object()
        self.add_bins_to_object(obj)

        self.database.connection.commit()

    def add_bins_to_object(self, obj):
        bin_type = self.get_bin_type()

        for _ in range(int(self.dictionary['anzahl'])):
            query = 'INSERT INTO bins(object_id, bin_type_id) VALUES (?, ?)'
            self.database.execute(query, (obj[0], bin_type[0]))

    def get_object(self):
        number = self.dictionary['objekt_nr']
        customerNumber = self.dictionary['kunden_nr']
        query = 'SELECT id FROM objects WHERE number = ?'

        model = self.database.fetchone(query, (number,))
        if model:
            return model

        address = self.get_address()

        self.database.execute('INSERT INTO objects(number, customer_number, address_id) VALUES (?, ?, ?)',
                              (number, customerNumber, address[0]))
        return self.database.fetchone(query, (number,))

    def get_bin_type(self):
        volume = self.dictionary['volumen']
        wasteType = self.get_waste_type()

        query = 'SELECT id FROM bin_types WHERE volume = ? and waste_type_id = ?'

        model = self.database.fetchone(query, (volume, wasteType[0]))
        if model:
            return model

        self.database.execute('INSERT INTO bin_types(volume, waste_type_id) VALUES (?, ?)', (volume, wasteType[0]))
        return self.database.fetchone(query, (volume, wasteType[0]))

    def get_waste_type(self):
        name = self.dictionary['abfallart']
        query = 'SELECT id FROM waste_types WHERE name = ?'

        model = self.database.fetchone(query, (name,))
        if model:
            return model

        self.database.execute('INSERT INTO waste_types(name) VALUES (?)', (name,))
        return self.database.fetchone(query, (name,))

    def get_address(self):
        number = self.dictionary['obj_haus_nr']
        street = self.get_street()
        city = self.get_city()

        query = 'SELECT id, number FROM addresses WHERE number = ? AND city_id = ? AND street_id = ?'

        model = self.database.fetchone(query, (number, city[0], street[0]))
        if model:
            return model

        self.database.execute('INSERT INTO addresses(number, city_id, street_id) VALUES (?, ?, ?)',
                              (number, city[0], street[0]))
        return self.database.fetchone(query, (number, city[0], street[0]))

    def get_street(self):
        name = self.dictionary['obj_strasse']
        query = 'SELECT id FROM streets WHERE name = ?'

        model = self.database.fetchone(query, (name,))
        if model:
            return model

        self.database.execute('INSERT INTO streets(name) VALUES (?)', (name,))
        return self.database.fetchone(query, (name,))

    def get_city(self):
        name = self.dictionary['obj_ort']
        postcode = self.dictionary['obj_plz']
        query = 'SELECT id FROM cities WHERE name = ? AND postcode = ?'

        model = self.database.fetchone(query, (name, postcode))
        if model:
            return model

        self.database.execute('INSERT INTO cities(name, postcode) VALUES (?, ?)', (name, postcode))
        return self.database.fetchone(query, (name, postcode))
