from discord import Client, Intents
from bin.internal.internal_error_handler import throw_error, ERRORS


class MyClient(Client):
    def __init__(self, config):
        self.config = config

        intents = Intents.default()
        intents.message_content = True
        intents.messages = True

        super(MyClient, self).__init__(intents=intents)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    async def on_send_message(self, message):
        if self.is_closed():
            throw_error(ERRORS.CLIENT_CLOSED)
        print(f"sending message: {message}")
        channel = self.get_channel(int(self.config.log_channel_id))
        if channel is None:
            throw_error(ERRORS.NO_CHANNEL)

        await channel.send("Hello, World!")

    def run(self):
        super(MyClient, self).run(self.config.bot_token)


def create_logger(config) -> MyClient:
    return MyClient(config)



