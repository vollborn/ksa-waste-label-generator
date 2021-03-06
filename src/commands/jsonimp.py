import json

from src.helpers.DirectoryHelper import DirectoryHelper
from src.helpers.EntryHelper import EntryHelper
from src.services.DependencyInjector import DependencyInjector


def command_jsonimp():
    files = DirectoryHelper.files("json")

    for file in files:
        with open(file) as fileobject:
            data = json.load(fileobject)

            for entry in data:
                DependencyInjector.inject(EntryHelper.handle, entry)
