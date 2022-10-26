from dotenv import load_dotenv, find_dotenv
from bin.discord_logger.internal.env import ENV
from os import getenv


class Config:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.bot_token = getenv(ENV.BOT_TOKEN)
        self.log_channel_id = getenv(ENV.LOG_CHANNEL_ID)

