# @rebootstr
import os
import time

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
        if len(text) > 200:
            parts = []
            part = ""
            lines = text.split("\n")
            for line in lines:
                if len(part + "\n" + line) < 200:
                    part += "\n" + line
                else:
                    parts.append(part)
                    part = ""
            parts.append(part)
            i = 1

            kostyl = os.system(self._prepareNotification(f"BandOS 0/{len(parts)}", "wait, please"))
            time.sleep(1)

            for part in reversed(parts):
                os.system(self._prepareNotification(f"BandOS {i}/{len(parts)}", part))
                i += 1
        else:
            os.system(self._prepareNotification("BandOS", text))

    def _prepareNotification(self, title, context):
        command = 'termux-notification -t "{}" -c "{}"'
        return command.format(title, context)
