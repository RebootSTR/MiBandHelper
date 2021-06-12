# @rebootstr

from Utils.Searcher import Searcher


class Listing:

    def __init__(self, elements=None, enabled=True):
        if elements is None:
            elements = []
        self.index = 0
        self.enabled = enabled
        self.elements = elements
        self.search = None

    def start(self):
        self.enabled = True
        self.index = 0

    def next(self):
        if self.search:
            self.search: Searcher
            self.search.add(1)
        else:
            self._indexPlus()

    def searchMode(self):
        self.search: Searcher
        if self.search:
            self.index = self.search.get(len(self.elements))
            self.search = None
        else:
            self.search = Searcher()

    def prev(self):
        if self.search:
            self.search: Searcher
            self.search.add(10)
        else:
            self._indexMinus()

    def _indexPlus(self):
        if self.index+1 < len(self.elements):
            self.index += 1
        else:
            self.index = 0

    def _indexMinus(self):
        if self.index-1 >= 0:
            self.index -= 1
        else:
            self.index = len(self.elements) - 1

    def getList(self):
        toPrint = ""
        for i in range(len(self.elements)):
            prefix = "#" if i == self.index else "-"
            toPrint += f"{i}.{prefix}{self.elements[i]}\n"
        if toPrint == "":
            toPrint = "NOTHING"
        return toPrint

    def getElement(self):
        return self.elements[self.index]
