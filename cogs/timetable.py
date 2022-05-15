from discord.ext import commands, tasks
from datetime import datetime as dt
import asyncio
import json
from pathlib import Path

json_file = Path(__file__).resolve().parent.joinpath("data.json")


class TimeTable(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.send_time_table.start()
        with json_file.open(encoding="uft8") as f:
            self.data = json.load(f)
        self.coll_time = [
            [f'{x[0][:3]}{int(x[0][3:]) - 5}' for i, x in enumerate(self.data["times"])]
        ]

    async def cog_unload(self) -> None:
        self.send_time_table.cancel()

    @tasks.loop()
    async def send_time_table(self) -> None:
        now = dt.now()
        next_class = 0
        if now.weekday() == 6:
            timedeff = dt(now.year, now.month, now.day+1, hour=9, minute=0) - now
            asyncio.sleep(int(timedeff.total_seconds()))

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TimeTable(bot))


async def start_up() -> None:
    import os
    import discord
    from dotenv import load_dotenv
    from pathlib import Path

    prefix = Path(__file__).resolve().parent

    load_dotenv(prefix.joinpath('.env'))
    load_dotenv(prefix.joinpath('../.env'))
    load_dotenv(prefix.joinpath('../../.env'))

    try:
        token = os.environ['TOKEN']
    except KeyError:
        token = os.environ['DIS_TEST_TOKEN']

    intents = discord.Intents.all()

    bot = commands.Bot('t!', intents=intents)
    await bot.load_extension(Path(__file__).stem)

    @bot.event
    async def on_ready() -> None:
        print('ready')
    await bot.start(token)

if __name__ == '__main__':
    asyncio.run(start_up())
