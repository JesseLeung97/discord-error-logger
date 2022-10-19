from enum import Enum, unique


class BCOLORS:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


@unique
class ERRORS(str, Enum):
    NO_DOTENV = 'The dotenv file could not be found.'
    NO_ENV_VARS = 'The dotenv file contained no environment variables.'
    CLIENT_CLOSED = "The client is not running."
    NO_CHANNEL = "The given channel ID did not match a channel in this server."


def throw_error(error_code):
    print(f"{BCOLORS.FAIL}{error_code}{BCOLORS.ENDC}")
    raise SystemExit(1)

