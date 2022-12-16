import os
import logging
from abc import ABC

import discord
from discord.commands import option
from dotenv import load_dotenv

from utilities import select_info_view, Options


logging.basicConfig(filename='logs/axonavi.log',
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                    level=logging.INFO,
                    filemode='w',
                    encoding='utf-8')
logging_handler = logging.StreamHandler()
logger = logging.getLogger('discord')
logger.addHandler(logging_handler)

logger.info("Loaded Logger")


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TEST_TOKEN = os.getenv('BOXLOTL_TOKEN')
MY_GUILD_ID = os.getenv('MY_GUILD_ID')
PRIV_GUILD_ID = os.getenv('PRIV_GUILD_ID')
BOXLOTL_GUILD_ID = os.getenv('BOXLOTL_GUILD_ID')

MY_GUILD = discord.Object(MY_GUILD_ID)
PRIV_GUILD = discord.Object(PRIV_GUILD_ID)

logger.info("Loaded environment variables")


class MyBot(discord.Bot, ABC):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix='?', intents=intents)

    async def on_ready(self):
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        activity = discord.Activity(type=3, name="you poop... always!")
        await self.change_presence(status=discord.Status.dnd, activity=activity)


bot = MyBot()


@bot.slash_command(name="status", description="Set status of bot!", guild_ids=[PRIV_GUILD_ID])
@option("status", discord.Status)
async def set_status(ctx: discord.ApplicationContext, status: discord.Status):
    logger.info(f"{ctx.user} used /status {status}")
    if ctx.user.id != 520923251367608322:
        return
    if status == "offline" or status == "streaming":
        await ctx.respond(f"Cannot change status to: **{status}**",
                          ephemeral=True)
        return
    prev_activity = bot.guilds[0].get_member(bot.user.id).activity

    await bot.change_presence(status=status, activity=prev_activity)
    await ctx.respond(f"Changed status to: **{status}**",
                      ephemeral=True)
    logger.info(f"{ctx.user} changed bot status to {status}")


@bot.slash_command(name="activity", description="Set activity of bot!", guild_ids=[PRIV_GUILD_ID])
@option("activity_type", str, choices=["playing", "listening", "watching"])
async def set_activity(ctx: discord.ApplicationContext, activity_type: str, *, activity_message: str):
    logger.info(f"{ctx.user} used /activity {activity_type} {activity_message}")
    if ctx.user.id != 520923251367608322:
        return
    if activity_message == "streaming":
        await ctx.respond(f"Cannot change activity to: **{activity_message}**",
                          ephemeral=True)
        return
    prev_status = bot.guilds[0].get_member(bot.user.id).status

    num_type = 0  # playing
    if activity_type == 'listening':
        num_type = 2
        if activity_message.lower().startswith("to "):
            activity_message = activity_message[3:].strip()
    elif activity_type == 'watching':
        num_type = 3

    await bot.change_presence(activity=discord.Activity(type=num_type, name=activity_message),
                              status=prev_status)
    await ctx.respond(f"Changed activity to: **{activity_type}** {activity_message}",
                      ephemeral=True)
    logger.info(f"{ctx.user} changed bot activity to {activity_type} {activity_message}")


async def get_choices(ctx: discord.AutocompleteContext):
    picked_option = ctx.options["info_option"]
    if picked_option == "Mobs and Bosses":
        return Options.boss


@bot.command(name="info", description="Get info about things in-game!")
@option("info_option", str, description="Select an option you need info about!", choices=Options.main)
@option("info_type", str, description="Select what you need info about!", autocomplete=get_choices)
async def game_info(ctx: discord.ApplicationContext, info_option: str = "Help", info_type: str = "none"):
    logger.info(f"{ctx.user} used /info {info_option} {info_type}")
    await ctx.respond(f"Hey {ctx.user}!")
    await select_info_view(ctx, info_option, info_type)


@bot.command(name="idkwtnt", guild_ids=[PRIV_GUILD_ID, BOXLOTL_GUILD_ID])
async def poop(ctx: discord.ApplicationContext, anything: str):
    logger.info(f"{ctx.user} used /idkwtnt {anything}")
    if ctx.user.id not in [520923251367608322, 801290250881335296]:
        await ctx.respond("You cannot use this you little sh*t",
                          ephemeral=True)
        return
    await ctx.send(anything)
    await ctx.respond("Message sent", ephemeral=True)
    logger.info(f"{ctx.user} sent \"{anything}\" in {ctx.channel}")


@bot.listen('on_message')
async def dont_ping(message):
    if message.author.id == bot.user.id:
        return
    allowed_pings_users = []  # 520923251367608322 users who can ping anyone
    dont_ping_roles = []  # roles on which bot notifies you not to ping
    dont_ping_exceptions_users = []  # people from the above roles who want to be pinged
    if message.author.id in allowed_pings_users:
        return
    for user in message.mentions:
        if user.id in dont_ping_exceptions_users:
            continue
        for role_id in dont_ping_roles:
            role = message.guild.get_role(role_id)
            if role in user.roles:
                await message.reply("ay boy im a higher up than you your not allowed to ping me",
                                    mention_author=True)


bot.run(TOKEN)
