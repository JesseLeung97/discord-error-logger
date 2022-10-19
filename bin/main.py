import threading
import time

from bin.internal.config import Config
from bin.internal.logger import create_logger, MyClient


def initialize_logger() -> MyClient:
    config = Config()
    return create_logger(config)


def run_logger(client):
    print("Starting bot thread.")
    client.run()


def run_api(client):
    print("Starting api thread.")
    time.sleep(5)
    print("Sending api thread.")
    client.dispatch("send_message", "hello, world")


def main():
    bot = initialize_logger()

    bot_thread = threading.Thread(target=run_logger, args=(bot,))
    api_thread = threading.Thread(target=run_api, args=(bot,))

    bot_thread.start()
    api_thread.start()

    bot_thread.join()
    api_thread.join()


if __name__ == '__main__':
    main()
