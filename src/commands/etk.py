from src.helpers.ExportHelper import ExportHelper


def command_etk(database):
    objects = database.fetchall('SELECT id FROM objects')

    for obj in objects:
        ExportHelper.handle(obj)
