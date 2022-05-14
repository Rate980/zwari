import discord
from discord.ext import commands


class MyBot(commands.Bot):
    async def on_ready(self) -> None:
        print('ready')


if __name__ == '__main__':
    import os
    from pathlib import Path

    from dotenv import load_dotenv

    file_prefix = Path(__file__).resolve().parent
    load_dotenv(file_prefix.joinpath('.env'))

    token = os.environ['TOKEN']
    prefix = os.environ['PREFIX']
    intents = discord.Intents.all()
    intents.typing = False

    bot = MyBot(prefix, intents=intents)

    bot.run(token)
