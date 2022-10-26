import json
import requests
import random
from bin.discord_logger.internal.config import Config


def _gen_random_nonce():
    return random.randint(1000000000000000000, 9999999999999999999)


class BotClient:
    def __init__(self, config: Config):
        self.config = config

    def __send_message(self, message: str):
        url = f"https://discord.com/api/v9/channels/{self.config.log_channel_id}/messages"
        headers = {
            "authorization": self.config.bot_token
        }
        data = {
            "content": message,
            "nonce": f"{_gen_random_nonce()}",
            "tts": "false"
        }
        res = requests.post(url=url, headers=headers, data=data)
        if res.status_code == 200:
            err = json.dumps(res.json(), indent=4)
            raise Exception(f"The server responded with a {res.status_code}\n{err}")

    def send_error_message(self, error_message: str, stack_trace: str = None):
        if stack_trace:
            error_message = f"{error_message}\n```\n{stack_trace}\n```"
        self.__send_message(error_message)

    def send_plain_message(self, message: str):
        self.__send_message(message)
