import json
import random

import requests

from src.discord_logger.constants.global_constants import GlobalConstants
from src.discord_logger.internal.config import Config


def _gen_random_nonce():
    return random.randint(1000000000000000000, 9999999999999999999)


class BotClient:
    def __init__(self, config: Config):
        self.config = config

    def _send_message(self, message: str):
        url = (
            f"https://discord.com/api/v9/channels/{self.config.log_channel_id}/messages"
        )

        headers = {
            "authorization": self.config.bot_token
        }

        data = {
            "content": message,
            "nonce": f"{_gen_random_nonce()}",
            "tts": "false"
        }

        response = requests.post(url=url, headers=headers, data=data)
        if response.status_code != GlobalConstants.HTTP_RESPONSE_OK:
            err = json.dumps(response.json(), indent=4)
            raise Exception(
                f"The server responded with a {response.status_code}\n{err}"
            )

    def send_error_message(self, error_message: str, stack_trace: str = None):
        if stack_trace:
            error_message = f"{error_message}\n```\n{stack_trace}\n```"
        self._send_message(error_message)

    def send_plain_message(self, message: str):
        self._send_message(message)
