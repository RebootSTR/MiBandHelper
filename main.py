# rebootstr

from queue import Queue
from threading import Thread

from BandOS import BandOS
from HTTPServer import HTTPServer


def start_server(queue: Queue):
    server = HTTPServer()

    def listener():
        while True:
            queue.put(server.get())

    serverThread = Thread(target=listener, daemon=True)
    serverThread.start()


buttons = \
    {
        "5": "buttonMusicPlay",
        "3": "buttonMusicNext",
        "1": "buttonMusicPrevious",
        "9": "buttonMusicVolumeUp",
        "7": "buttonMusicVolumeDown",
        "25": "buttonMusicPlay2",
        "23": "buttonMusicNext2",
        "21": "buttonMusicPrevious2",
        "29": "buttonMusicVolumeUp2",
        "27": "buttonMusicVolumeDown2"
    }


def run():
    queue = Queue()
    start_server(queue)
    system = BandOS()
    while True:
        button = queue.get()
        # print(button)

        if button == "buttonMusicPlay":
            system.play()
        elif button == "buttonMusicPlay2":
            system.play2x()
        elif button == "buttonMusicNext":
            system.next()
        elif button == "buttonMusicPrevious":
            system.previous()
        elif button == "buttonMusicVolumeUp":
            system.volUp()
        elif button == "buttonMusicVolumeUp2":
            system.volUp2x()
        elif button == "buttonMusicVolumeDown":
            system.volDown()
        elif button == "buttonMusicVolumeDown2":
            system.volDown2x()
        else:
            print("iv got a unknown message", button)


if __name__ == '__main__':
    run()
