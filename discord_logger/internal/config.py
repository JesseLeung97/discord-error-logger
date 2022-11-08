import sys
from os import getenv

from dotenv import find_dotenv, load_dotenv

from discord_logger.constants.environment_variables import ENV


def _get_parent_module_name() -> str:
    return sys.modules['.'.join(__name__.split('.')[:-1]) or '__init__']


class Config:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.bot_token = getenv(ENV.BOT_TOKEN)
        self.log_channel_id = getenv(ENV.LOG_CHANNEL_ID)
        self.parent_module_name = _get_parent_module_name()
