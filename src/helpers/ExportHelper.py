import os

from barcode.writer import ImageWriter
from barcode import Code128

from src.services.DependencyInjector import DependencyInjector
from fpdf import FPDF


class ExportHelper:
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
        query = 'SELECT ' \
                'objects.id, ' \
                'objects.number, ' \
                'objects.customer_number, ' \
                'cities.name, ' \
                'cities.postcode,' \
                'streets.name,' \
                'addresses.number ' \
                'FROM objects ' \
                'JOIN addresses ON addresses.id = objects.address_id ' \
                'JOIN streets ON addresses.street_id = streets.id ' \
                'JOIN cities ON addresses.city_id = cities.id ' \
                'WHERE objects.id = ?'

        model = self.database.fetchone(query, (self.dictionary[0],))
        bins = self.get_bins(model[0])

        self.export(model, bins)

    def get_bins(self, object_id):
        query = 'SELECT ' \
                'bins.id, ' \
                'waste_types.name, ' \
                'bin_types.volume ' \
                'FROM bins ' \
                'JOIN bin_types ON bins.bin_type_id = bin_types.id ' \
                'JOIN waste_types ON bin_types.waste_type_id = waste_types.id ' \
                'WHERE object_id = ?'

        return self.database.fetchall(query, (object_id,))

    def export(self, model, bins):
        self.cli.println("Exporting " + model[1] + "...")

        pdf = FPDF()
        pdf.set_font('Arial', 'B', 8)

        for bin_model in bins:
            pdf.add_page()
            pdf.cell(0, 4, 'Objekt-Nr: ' + model[1], 0, True)
            pdf.cell(0, 4, 'Straße: ' + model[5], 0, True)
            pdf.cell(0, 4, 'Nr: ' + str(model[6]), 0, True)
            pdf.cell(0, 4, 'PLZ: ' + model[4], 0, True)
            pdf.cell(0, 4, 'Ort: ' + model[3], 0, True)

            pdf.ln()
            pdf.cell(0, 4, 'Tonnen-Nr: ' + str(bin_model[0]), 0, True)
            pdf.cell(0, 4, 'Abfallsorte: ' + bin_model[1], 0, True)
            pdf.cell(0, 4, 'Volumen: ' + str(bin_model[2]), 0, True)

            barcode = self.get_barcode(bin_model)
            pdf.image(barcode, 120, 10, 40, 20)

            if os.path.exists(barcode):
                os.remove(barcode)

        file = model[1] + '.pdf'
        pdf.output(file)

    @staticmethod
    def get_barcode(bin_model):
        number = str(bin_model[0])
        filename = 'etikett-' + number

        codeNumber = "000000" + number
        codeNumber = codeNumber[-6:]

        code = Code128(codeNumber, writer=ImageWriter())
        code.save(filename)

        return filename + '.png'
