# @rebootstr

import argparse
from HTTPClient import HTTPClient
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('event', type=str)

    args = parser.parse_args()
    send(args.event.split(".")[-1])


def send(message):
    try:
        client = HTTPClient()
        client.send(message)
    except:
        logging.error("ServerNotFound")


if __name__ == '__main__':
    run()
