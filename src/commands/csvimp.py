import csv

from src.helpers.DirectoryHelper import DirectoryHelper
from src.helpers.EntryHelper import EntryHelper
from src.services.DependencyInjector import DependencyInjector


def command_csvimp():
    files = DirectoryHelper.files("csv")

    for file in files:
        with open(file) as fileobject:
            for entry in csv.DictReader(fileobject, delimiter=";"):
                DependencyInjector.inject(EntryHelper.handle, entry)
