from dotenv import load_dotenv, find_dotenv
from bin.internal.internal_error_handler import throw_error, ERRORS
from bin.internal.env import ENV
from os import getenv


class Config:
    def __init__(self):
        env = find_dotenv()
        if env == '':
            throw_error(ERRORS.no_dotenv)

        if not load_dotenv(env):
            throw_error(ERRORS.no_env_vars)

        self.bot_token = getenv(ENV.BOT_TOKEN)
        self.log_channel_id = getenv(ENV.LOG_CHANNEL_ID)