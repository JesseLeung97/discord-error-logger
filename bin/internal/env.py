from enum import Enum, unique


@unique
class ENV(str, Enum):
    PUBLIC_KEY = 'PUBLIC_KEY'
    CLIENT_ID = 'CLIENT_ID'
    BOT_TOKEN = 'BOT_TOKEN'
    INTENTS = 'INTENTS'
    LOG_CHANNEL_ID = 'LOG_CHANNEL_ID'

