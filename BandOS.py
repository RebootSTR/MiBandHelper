# @rebootstr
import os

from Apps.MainMenu import MenuApp
from Apps.OSI import OSI


class BandOS(OSI):

    def __init__(self):
        super().__init__()
        self.systemApps = ["AppI.py", "MainMenu.py", "OSI.py"]
        self.menuApp = MenuApp(self)
        self.selectedApp = None
        self.exitToMainMenu()

    def volDown(self):
        self.selectedApp.volDown()

    def volDown2x(self):
        self.selectedApp.volDown2x()

    def volUp(self):
        self.selectedApp.volUp()

    def volUp2x(self):
        self.selectedApp.volUp2x()

    def play(self):
        self.selectedApp.play()

    def play2x(self):
        self.selectedApp.play2x()

    def previous(self):
        self.selectedApp.previous()

    def previous2x(self):
        self.selectedApp.previous2x()

    def next(self):
        self.selectedApp.next()

    def next2x(self):
        self.selectedApp.next2x()

    def exitToMainMenu(self):
        self.selectedApp = self.menuApp

    def print(self, text):
        print(text)
        try:
            os.system(self._prepareNotification("BandOS", text))
        except:
            pass

    def _prepareNotification(self, title, context):
        command = 'termux-notification -t "{}" -c "{}" -i 1337'
        return command.format(title, context)
