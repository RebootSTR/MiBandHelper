# @rebootstr

from Apps.AppI import AppI
from Apps.OSI import OSI


class HelloWorld(AppI):
    def __init__(self, system: OSI):
        super().__init__(system)

    def volDown(self):
        self.system.exitToMainMenu()

    def play(self):
        self.system.print("всем ку с вами я, ваш единственный подписчек")
