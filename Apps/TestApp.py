# @rebootstr

from Apps.AppI import AppI
from Apps.OSI import OSI


class TestApp(AppI):
    def __init__(self, system: OSI):
        super().__init__(system)

    def volDown(self):
        self.system.exitToMainMenu()

    def play(self):
        self.system.print("Уведа с текстом)))")
