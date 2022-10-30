from os import getenv

from dotenv import find_dotenv, load_dotenv

from discord_logger.constants.environment_variables import ENV


class Config:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.bot_token = getenv(ENV.BOT_TOKEN)
        self.log_channel_id = getenv(ENV.LOG_CHANNEL_ID)
