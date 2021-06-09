# rebootstr

from queue import Queue
from threading import Thread
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

    search_mode = False
    search_value = 0
    index = 0
    while True:
        button = queue.get()
        # print(button)

        if button == "buttonMusicPlay":
            if search_mode:
                search_mode = False
                index = search_value
                print("index set to", index)
            else:
                print("Print list. index =", index)
        elif button == "buttonMusicNext":
            index += 1
            print("down, index =", index)
        elif button == "buttonMusicPrevious":
            index -= 1
            print("up, index =", index)
        elif button == "buttonMusicVolumeUp":
            if search_mode:
                search_value += 1
                print(search_value)
            else:
                print("open with index", index)
                index = 0
        elif button == "buttonMusicVolumeDown":
            if search_mode:
                search_value += 10
                print(search_value)
            else:
                print("return")
                index = 0
        elif button == "buttonMusicPlay2":
            print("search")
            search_mode = True
            search_value = 0
        else:
            print("iv got a unknown message", button)


if __name__ == '__main__':
    run()
