# @rebootstr
import os

from Apps.AppI import AppI
from Apps.OSI import OSI
from Utils.Listing import Listing


DIR_NAME = "Questions"
DIR_PATH = "./"


class Questions(AppI):
    def __init__(self, system: OSI):
        super().__init__(system)
        self.filesListing = Listing(self._parseFiles())
        self.questionsListing = Listing(enabled=False)
        self.answers = None

    def _parseFiles(self):
        files = list()
        if DIR_NAME not in os.listdir(DIR_PATH):
            os.mkdir(DIR_PATH + DIR_NAME)
            return []
        for file in os.scandir(DIR_PATH + DIR_NAME):
            file: os.DirEntry
            if file.is_file():
                files.append(file.name)
        return files

    def volDown(self):
        if self.filesListing.enabled:
            if self.filesListing.search:
                self.filesListing.cancelSearch()
            else:
                self.system.exitToMainMenu()
        elif self.questionsListing.enabled:
            if self.questionsListing.search:
                self.questionsListing.cancelSearch()
            else:
                self.questionsListing.enabled = False
                self.filesListing.enabled = True

    def volUp2x(self):
        if self.filesListing.enabled:
            self.filesListing.enabled = False
            self._parseQuestions()
            self.questionsListing.start()
        elif self.questionsListing.enabled:
            self.system.print(self._formatAnswer())

    def play(self):
        if self.filesListing.enabled:
            self.system.print(self.filesListing.getList(30))
        elif self.questionsListing.enabled:
            self.system.print(self.questionsListing.getList(30))

    def play2x(self):
        if self.filesListing.enabled:
            self.filesListing.searchMode()
        elif self.questionsListing.enabled:
            self.questionsListing.searchMode()

    def previous(self):
        if self.filesListing.enabled:
            self.filesListing.prev()
        elif self.questionsListing.enabled:
            self.questionsListing.prev()

    def next(self):
        if self.filesListing.enabled:
            self.filesListing.next()
        elif self.questionsListing.enabled:
            self.questionsListing.next()

    def _parseQuestions(self):
        fileName = self.filesListing.getElement()
        file = open(DIR_PATH + DIR_NAME + f"/{fileName}", "r", encoding="utf-8")
        lines = file.readlines()

        blocks = []
        block = []
        for line in lines:
            if line == "\n":
                blocks.append(block)
                block = []
            else:
                block.append(line.replace("\n", ""))
        blocks.append(block)

        questions = []
        answers = []
        for block in blocks:
            if len(block) == 0:
                continue
            question = block[0]
            answer = ""
            for i in range(1, len(block)):
                answer += block[i] + "\n"
            answer = answer[:-1]
            questions.append(question)
            answers.append(answer)
        self.answers = answers
        self.questionsListing.elements = questions

    def _formatAnswer(self):
        ind = self.questionsListing.index
        question = self.questionsListing.getElement()
        answer = self.answers[ind].replace('\n', '\n-')
        return f"{ind}.{question}\n-{answer}"
