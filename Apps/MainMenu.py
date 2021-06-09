# @rebootstr
import os

import Apps.AppI
from Apps.OSI import OSI
from Utils.Searcher import Searcher


class MenuApp(Apps.AppI.AppI):

    def __init__(self, system: OSI):
        super().__init__(system)
        self.modules = list()
        self.index = 0
        self.searchMode = None
        self.apps = self._parseApps()

    def volDown(self):
        if self.searchMode:
            self._exitFromSearchMode()

    def volUp2x(self):
        self._openApp()

    def play(self):
        if self.searchMode:
            self._applySearching()
        else:
            self._printListing()

    def play2x(self):
        if not self.searchMode:
            self._enterToSearchMode()

    def previous(self):
        if self.searchMode:
            self._searchModeBigStep()
        else:
            self._indexMinus()

    def next(self):
        if self.searchMode:
            self._searchModeSmallStep()
        else:
            self._indexPlus()

    def _indexPlus(self):
        if self.index+1 < len(self.apps):
            self.index += 1
        else:
            self.index = 0

    def _indexMinus(self):
        if self.index-1 >= 0:
            self.index -= 1
        else:
            self.index = len(self.apps) - 1

    def _exitFromSearchMode(self):
        self.searchMode = None

    def _enterToSearchMode(self):
        self.searchMode = Searcher()

    def _searchModeBigStep(self):
        self.searchMode: Searcher
        self.searchMode.add(10)

    def _searchModeSmallStep(self):
        self.searchMode: Searcher
        self.searchMode.add(1)

    def _applySearching(self):
        self.searchMode: Searcher
        self.index = self.searchMode.get(len(self.apps) - 1)
        self._exitFromSearchMode()

    def _printListing(self):
        toPrint = ""
        for i in range(len(self.apps)):
            prefix = "#" if i == self.index else "-"
            toPrint += f"{i}.{prefix}{self.apps[i]['name']}\n"
        self.system.print(toPrint)

    def _parseApps(self):
        files = list()
        for file in os.scandir("Apps/"):
            file: os.DirEntry
            if file.is_file() and file.name[-3:] == ".py" and file.name not in self.system.systemApps:
                files.append(file.name[:-3])
        apps = list()
        for name in files:
            app = {
                "name": name,
                "module": __import__("Apps."+name)
            }
            apps.append(app)
        return apps

    def _openApp(self):
        appModule = self.apps[self.index]
        name = appModule["name"]
        newApp = eval(f'appModule["module"].{name}.{name}(self.system)')
        self.system.selectedApp = newApp
