import discord
from discord import SelectOption
from discord.ui import View
from info_boss import *


class Options:
    main = ["Help", "NPCs", "Mobs and Bosses", "Items"]
    boss = ["Crypt Slasher", "Elder Slasher", "Magmatic Spirit", "Royal Gargoyle"]


async def select_info_view(ctx, info_option: str, info_type: str = "none"):
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
        await select_info_view(interaction, select.values[0])


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
                label="Axolotl-Infused Zombie",
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
