from discord_logger.internal.bot_client import BotClient
from discord_logger.internal.config import Config
from discord_logger.external.api import (log_error, plain_message)

if __name__ == "__main__":
    print("Starting up the bot client")
    _config = Config()
    bot_client = BotClient(config=_config)