from src.discord_logger.internal.bot_client import BotClient
from src.discord_logger.internal.config import Config

if __name__ == "__main__":
    print("Starting up the bot client")
    _config = Config()
    bot_client = BotClient(config=_config)
