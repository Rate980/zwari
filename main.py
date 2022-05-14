import os

import discord
from discord.ext import commands


class MyBot(commands.Bot):
    async def on_ready(self) -> None:
        print('ready')


if __name__ == '__main__':
    from pydotenv import load_dotenv
    from pathlib import Path
    prefix = Path(__file__).resolve().parent
    load_dotenv(prefix.joinpath('.env'))

    intents = discord.Intents.all()
    intents.typing = False
