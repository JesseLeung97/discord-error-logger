import inspect
from os import getenv

from dotenv import find_dotenv, load_dotenv

from discord_logger.constants.environment_variables import ENV


def _get_parent_module_name() -> str:
    stack = inspect.stack(0)
    stack_len = len(stack)
    stack_frame = stack[stack_len - 1]
    end_idx = stack_frame.filename.index("/__init__.py")
    start_idx = stack_frame.filename.rindex("/", 0, end_idx)

    return stack_frame.filename[start_idx + 1:end_idx]


class Config:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.bot_token = getenv(ENV.BOT_TOKEN)
        self.log_channel_id = getenv(ENV.LOG_CHANNEL_ID)
        self.parent_module_name = _get_parent_module_name()
