from discord_logger.internal.config import Config
from discord_logger.internal.bot_client import BotClient


def log_error_handler(error_message: str, stack_trace: str=None):
    bot_client = _create_bot_client()
    bot_client.send_error_message(error_message, stack_trace)


def plain_message_handler(message: str):
    bot_client = _create_bot_client()
    bot_client.send_plain_message(message)


def _create_bot_client() -> BotClient:
    _config = Config()
    return BotClient(_config)
