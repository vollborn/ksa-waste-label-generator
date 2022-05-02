import json

import xmltodict

from src.helpers.DirectoryHelper import DirectoryHelper
from src.helpers.EntryHelper import EntryHelper
from src.services.DependencyInjector import DependencyInjector


def command_xmlimp():
    files = DirectoryHelper.files("xml")

    for file in files:
        with open(file) as fileobject:
            content = fileobject.read()

        data = xmltodict.parse(content)

        for entry in data['entries']['entry']:
            # needs to be converted from ordered dict to dict first
            converted = json.loads(json.dumps(entry))
            DependencyInjector.inject(EntryHelper.handle, converted)
