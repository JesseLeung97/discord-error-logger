from discord_logger import BotClient


def log_error_handler(error_message: str, stack_trace: str=None):
    BotClient.send_error_message(error_message, stack_trace)


def plain_message_handler(message: str):
    BotClient.send_plain_message(message)
