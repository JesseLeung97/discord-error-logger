from bin.discord_logger.internal.config import Config
from bin.discord_logger.internal.bot_client import _bot_client


def main():
    print("Starting bot client")
    _bot_client.send_plain_message("This is just a test.  I'm a bot.")


if __name__ == '__main__':
    main()
