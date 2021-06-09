# @rebootstr
from HTTPClient import HTTPClient
from main import buttons


def parse_buttons(enter: str):
    i = 0
    result = list()
    while i < len(enter):
        if enter[i] == "2":
            i += 1
            result.append(buttons["2"+enter[i]])
        else:
            result.append(buttons[enter[i]])
        i += 1
    return result


def run():
    print("7 9")
    print(" 5")
    print("1 3")
    print("--- if you want a press 2x: enter 27 or 29 or 25 etc")
    while True:
        enter = input("Enter a buttons: ")
        to_send = parse_buttons(enter)
        for send in to_send:
            HTTPClient().send(send)


if __name__ == '__main__':
    run()
