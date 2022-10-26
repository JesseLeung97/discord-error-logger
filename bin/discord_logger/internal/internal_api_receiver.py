from bin.discord_logger.internal.main import bot_client


def log_error_handler(error_message, stack_trace=None):
    bot_client.send_error_message(error_message, stack_trace)


def plain_message_handler(message):
    bot_client.send_plain_message(message)

