import csv

from src.helpers.DirectoryHelper import DirectoryHelper
from src.helpers.EntryHelper import EntryHelper


def command_csvimp():
    files = DirectoryHelper.files("csv")

    for file in files:
        with open(file) as fileobject:
            for entry in csv.DictReader(fileobject, delimiter=";"):
                EntryHelper.handle(entry)
