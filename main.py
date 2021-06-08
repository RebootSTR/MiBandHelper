# rebootstr
import time
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

'''Music Play/Pause event use com.mc.miband.buttonMusicPlay action **

    Music Next event use com.mc.miband.buttonMusicNext action **
    
    Music Previous event use com.mc.miband.buttonMusicPrevious action **
    
    Music Volume up event use com.mc.miband.buttonMusicVolumeUp action **
    
    Music Volume down event use com.mc.miband.buttonMusicVolumeDown action **
    
    Music 2x Play/Pause event use com.mc.miband.buttonMusicPlay2 action **
    
    Music 2x Next event use com.mc.miband.buttonMusicNext2 action **
    
    Music 2x Previous event use com.mc.miband.buttonMusicPrevious2 action **
    
    Music 2x Volume up event use com.mc.miband.buttonMusicVolumeUp2 action **
    
    Music 2x Volume down event use com.mc.miband.buttonMusicVolumeDown2 action **'''


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


if __name__ == '__main__':
    run()
