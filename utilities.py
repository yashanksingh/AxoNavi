import discord
from discord import SelectOption
from discord.ui import View
from info_boss import *


class Options:
    main = ["Help", "NPCs", "Mobs and Bosses", "Items"]
    boss = ["Spider Queen", "Cuboid", "Grave Digger", "Demon", "Crypt Slasher", "Elder Slasher", "Magmatic Spirit", "Royal Gargoyle"]


async def boss_spawn_alert(boss, channel):
    main_embed = Embed(
        # title=boss,
        color=Colour.red(),
    )

    main_embed.add_field(name=f"{boss} has spawned!",
                         value=f"To know more about {boss}, use `/info`!")

    main_embed.timestamp = datetime.datetime.now()
    main_embed.set_footer(text="AxoNavi",
                          icon_url="https://cdn.discordapp.com/attachments/843077857492467742/1053664423513964615/1671283545940.png")
    main_embed.set_author(name="Boss Spawn Alert",
                          icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/crossed-swords_2694-fe0f.png")
    role = discord.utils.get(channel.guild.roles, name=boss)
    await channel.send(f"{role.mention}", embed=main_embed)


async def show_info(ctx, info_option: str, info_type: str = "none"):
    if info_option == "Help":
        await ctx.followup.send("Select an option you need info about!", view=InfoMainView())
    if info_option == "NPCs":
        await ctx.followup.send("Select which NPC you need info about!", view=NPCView())
    if info_option == "Mobs and Bosses":
        if info_type != "none":
            await select_info_boss_embed(ctx, info_type)
            return
        await ctx.followup.send("Select which mob or boss you need info about!", view=BossView())
    if info_option == "Items":
        await ctx.followup.send("I do not have info about items at the moment. Check in later!")


class InfoMainView(View):
    @discord.ui.select(
        placeholder="Choose an option!",
        options=[
            SelectOption(
                label="NPCs",
                emoji="👥",
                description="Locations, Trades, etc.",
            ),
            SelectOption(
                label="Mobs and Bosses",
                emoji="☠",
                description="Spawn-points, Drops, etc.",
            ),
            SelectOption(
                label="Items",
                emoji="🧤",
                description="Obtaining, Lore, etc.",
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        select.disabled = True
        select.placeholder = select.values[0]
        await interaction.response.edit_message(view=self)
        await show_info(interaction, select.values[0])


class NPCView(View):
    @discord.ui.select(
        placeholder="Choose an NPC!",
        options=[
            SelectOption(
                label="Shady IronSmith",
            ),
            SelectOption(
                label="Jamie",
            ),
            SelectOption(
                label="Alhena The Sentinel",
            ),
            SelectOption(
                label="Dungeon Guards",
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        select.disabled = True
        select.placeholder = select.values[0]
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(f"I do not have info about {select.values[0]} at the moment. Check in later!")


class BossView(View):
    @discord.ui.select(
        placeholder="Choose a Boss!",
        options=[
            SelectOption(
                label="Spider Queen",
            ),
            SelectOption(
                label="Cuboid",
            ),
            SelectOption(
                label="Demon",
            ),
            SelectOption(
                label="Crypt Slasher",
            ),
            SelectOption(
                label="Elder Slasher",
            ),
            SelectOption(
                label="Magmatic Spirit",
            ),
            SelectOption(
                label="Royal Gargoyle",
            ),
        ]
    )
    async def select_callback(self, select, interaction):
        select.disabled = True
        select.placeholder = select.values[0]
        await interaction.response.edit_message(view=self)
        await select_info_boss_embed(interaction, select.values[0])
