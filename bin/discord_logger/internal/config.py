from dotenv import load_dotenv, find_dotenv
from bin.discord_logger.internal.internal_error_handler import _throw_error, ERRORS
from bin.discord_logger.internal.env import ENV
from os import getenv


class Config:
    def __init__(self):
        env = find_dotenv()
        if env == '':
            _throw_error(ERRORS.no_dotenv)

        if not load_dotenv(env):
            _throw_error(ERRORS.no_env_vars)

        self.bot_token = getenv(ENV.BOT_TOKEN)
        self.log_channel_id = getenv(ENV.LOG_CHANNEL_ID)

