from src.discord_logger.internal.internal_api_receiver import (
    log_error_handler, plain_message_handler)


def log_error(error_message: str, stack_trace: str=None):
    log_error_handler(error_message, stack_trace)


def plain_message(message: str):
    plain_message_handler(message)
