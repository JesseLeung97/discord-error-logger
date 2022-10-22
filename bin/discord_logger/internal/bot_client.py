import requests
import random
from bin.discord_logger.internal.config import Config


def _gen_random_nonce():
    return random.randint(1000000000000000000, 9999999999999999999)


class BotClient:
    def __init__(self, config):
        self.config = config

    def __send_message(self, message):
        url = f"https://discord.com/api/v9/channels/{self.config.log_channel_id}/messages"
        headers = {
            "authorization": self.config.bot_token
        }
        data = {
            "content": message,
            "nonce": f"{_gen_random_nonce()}",
            "tts": "false"
        }
        requests.post(url=url, headers=headers, data=data)

    def send_error_message(self, error_message, stack_trace=None):
        if stack_trace:
            error_message = f"{error_message}\n```\n{stack_trace}\n```"
        self.__send_message(error_message)

    def send_plain_message(self, message):
        self.__send_message(message)


_config = Config()
_bot_client = BotClient(config=_config)

