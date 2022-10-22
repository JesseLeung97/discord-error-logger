from enum import Enum, unique


@unique
class ENV(str, Enum):
    BOT_TOKEN = "BOT_TOKEN"
    LOG_CHANNEL_ID = 'LOG_CHANNEL_ID'

