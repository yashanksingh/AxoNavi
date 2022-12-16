from discord import Embed
from discord import Colour


async def select_info_boss_embed(ctx, boss_type: str):
    if boss_type == "Spider Queen":
        main_embed = Embed(
            title="Spider Queen",
            color=Colour.orange(),
        )

        main_embed.add_field(name="Type", value="Boss", inline=True)
        main_embed.add_field(name="Location", value="Caves", inline=True)
        main_embed.add_field(name="Nearest Warp", value="spawn", inline=True)

        main_embed.add_field(name="Spawning",
                             value="Every `5` minutes.\nCapped at `1`",
                             inline=False)
        main_embed.add_field(name="Skills",
                             value="  Can confuse players every `10` seconds."
                                   "\nCan spawn `10` minions every `20` seconds."
                                   "\nCan steal `20%` of player's health every `30` seconds.",
                             inline=False)
        main_embed.add_field(name="Player-Based Drops",
                             value="  #1 Damager Drops:\n`100%` - 3 Spider Queen's Eye"
                                   "\n#2 Damager Drops:\n`100%` - 2 Spider Queen's Eye"
                                   "\n#3 Damager Drops:\n`100%` - 1 Spider Queen's Eye",
                             inline=False)

        main_embed.set_footer(text="AxoNavigator",
                              icon_url="https://cdn.discordapp.com/emojis/981320857672618045.webp?size=128&quality=lossless")
        main_embed.set_author(name="Mobs and Bosses",
                              icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/skull-and-crossbones_2620-fe0f.png")
        main_embed.set_thumbnail(
            url="https://mc-heads.net/avatar/35e248da2e108f09813a6b848a0fcef111300978180eda41d3d1a7a8e4dba3c3")

        image_embed = Embed(color=Colour.orange())
        image_embed.set_image(
            url="https://cdn.discordapp.com/attachments/965142041623429162/1053194641006145556/image.png")

        await ctx.followup.send(embeds=[main_embed, image_embed])
        return

    if boss_type == "Cuboid":
        main_embed = Embed(
            title="Cuboid",
            color=Colour.orange(),
        )

        main_embed.add_field(name="Type", value="Boss", inline=True)
        main_embed.add_field(name="Location", value="Nether", inline=True)
        main_embed.add_field(name="Nearest Warp", value="nether", inline=True)

        main_embed.add_field(name="Spawning",
                             value="Every `5` minutes.\nCapped at `1`",
                             inline=False)
        main_embed.add_field(name="Skills",
                             value="  Can ignite players on fire every `2` seconds."
                                   "\nCan shoot a fireball at player every `5` seconds.",
                             inline=False)
        main_embed.add_field(name="General Drops",
                             value="  `  3%` - 64 Forged Magma"
                                   "\n`  5%` - 32 Forged Magma"
                                   "\n` 10%` - 16 Forged Magma"
                                   "\n` 20%` - 8 Forged Magma"
                                   "\n` 60%` - 4 Forged Magma"
                                   "\n` 80%` - 2 Forged Magma"
                                   "\n`100%` - 1 Forged Magma",
                             inline=False)
        main_embed.add_field(name="Player-Based Drops",
                             value="  #1 Damager Drops:\n` 5%` - Charred Magma Pants"
                                   "\n#2 Damager Drops:\n` 2%` - Charred Magma Pants"
                                   "\n#3 Damager Drops:\n` 1%` - Charred Magma Pants",
                             inline=False)

        main_embed.set_footer(text="AxoNavigator",
                              icon_url="https://cdn.discordapp.com/emojis/981320857672618045.webp?size=128&quality=lossless")
        main_embed.set_author(name="Mobs and Bosses",
                              icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/skull-and-crossbones_2620-fe0f.png")
        main_embed.set_thumbnail(
            url="https://mc-heads.net/avatar/38957d5023c937c4c41aa2412d43410bda23cf79a9f6ab36b76fef2d7c429")

        image_embed = Embed(color=Colour.orange())
        image_embed.set_image(
            url="https://cdn.discordapp.com/attachments/965142041623429162/1053189646420541490/image.png")

        await ctx.followup.send(embeds=[main_embed, image_embed])
        return

    if boss_type == "Demon":
        main_embed = Embed(
            title="Demon",
            color=Colour.orange(),
        )

        main_embed.add_field(name="Type", value="Basic Enemy", inline=True)
        main_embed.add_field(name="Location", value="Nether", inline=True)
        main_embed.add_field(name="Nearest Warp", value="demonnest", inline=True)

        main_embed.add_field(name="Spawning",
                             value="`10%` chance every `30` seconds\nCapped at `5`",
                             inline=False)
        main_embed.add_field(name="General Drops",
                             value="  `  1%` - 1 Compressed Demon Scales"
                                   "\n`  3%` - 32 Demon Scales"
                                   "\n` 10%` - 16 Demon Scales"
                                   "\n` 20%` - 8 Demon Scales"
                                   "\n` 60%` - 4 Demon Scales"
                                   "\n` 80%` - 2 Demon Scales"
                                   "\n`100%` - 1 Demon Scales",
                             inline=False)

        main_embed.set_footer(text="AxoNavigator",
                              icon_url="https://cdn.discordapp.com/emojis/981320857672618045.webp?size=128&quality=lossless")
        main_embed.set_author(name="Mobs and Bosses",
                              icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/skull-and-crossbones_2620-fe0f.png")
        main_embed.set_thumbnail(
            url="https://mc-heads.net/avatar/f421b3a2d68a79053c8bee3c3bb3f665d51469fc1e3d35a8c5ea2f1b73337")

        image_embed = Embed(color=Colour.orange())
        image_embed.set_image(
            url="https://cdn.discordapp.com/attachments/965142041623429162/1053179854297763940/image.png")

        await ctx.followup.send(embeds=[main_embed, image_embed])
        return

    if boss_type == "Crypt Slasher":
        main_embed = Embed(
            title="Crypt Slasher",
            color=Colour.orange(),
        )

        main_embed.add_field(name="Type", value="Basic Enemy", inline=True)
        main_embed.add_field(name="Location", value="Graveyard", inline=True)
        main_embed.add_field(name="Nearest Warp", value="graveyard", inline=True)

        main_embed.add_field(name="Spawning",
                             value="`6.9%` chance every `42` seconds\nCapped at `30`",
                             inline=False)
        main_embed.add_field(name="General Drops",
                             value="  `0.3%` - Slasher's Knife"
                                   "\n`0.1%` - 16 Crimson Blood"
                                   "\n`  2%` - 1 Crimson Blood"
                                   "\n`  5%` - 64 Rotten Flesh"
                                   "\n` 10%` - 32 Rotten Flesh"
                                   "\n` 20%` - 16 Rotten Flesh"
                                   "\n` 30%` - 8 Rotten Flesh"
                                   "\n` 50%` - 4 Rotten Flesh",
                             inline=False)

        main_embed.set_footer(text="AxoNavigator",
                              icon_url="https://cdn.discordapp.com/emojis/981320857672618045.webp?size=128&quality=lossless")
        main_embed.set_author(name="Mobs and Bosses",
                              icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/skull-and-crossbones_2620-fe0f.png")
        main_embed.set_thumbnail(
            url="https://mc-heads.net/avatar/862ad44182f4b4ae5c815a19e39837639668642a545888d138732ab4f8c5c")

        image_embed = Embed(color=Colour.orange())
        image_embed.set_image(
            url="https://cdn.discordapp.com/attachments/965142041623429162/1044602658050297916/image.png")

        await ctx.followup.send(embeds=[main_embed, image_embed])
        return

    if boss_type == "Elder Slasher":
        main_embed = Embed(
            title="Elder Slasher",
            color=Colour.orange(),
        )

        main_embed.add_field(name="Type", value="Mini Boss", inline=True)
        main_embed.add_field(name="Location", value="Graveyard", inline=True)
        main_embed.add_field(name="Nearest Warp", value="graveyard", inline=True)

        main_embed.add_field(name="Spawning",
                             value="Every `2` minutes\nCapped at `2`",
                             inline=False)
        main_embed.add_field(name="General Drops",
                             value="  `0.5%` - Jagged Katana"
                                   "\n`  4%` - Forged Crimson",
                             inline=False)

        main_embed.set_footer(text="AxoNavigator",
                              icon_url="https://cdn.discordapp.com/emojis/981320857672618045.webp?size=128&quality=lossless")
        main_embed.set_author(name="Mobs and Bosses",
                              icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/skull-and-crossbones_2620-fe0f.png")
        main_embed.set_thumbnail(
            url="https://mc-heads.net/avatar/36aae86da0cd317a47fa6668fd4785b5a7a7e4ed9e7bc68652bae27984b84c")

        image_embed = Embed(color=Colour.orange())
        image_embed.set_image(
            url="https://cdn.discordapp.com/attachments/965142041623429162/1044604854347251722/image.png")

        await ctx.followup.send(embeds=[main_embed, image_embed])
        return

    if boss_type == "Magmatic Spirit":
        main_embed = Embed(
            title="Magmatic Spirit",
            color=Colour.orange(),
        )

        main_embed.add_field(name="Type", value="Basic Enemy", inline=True)
        main_embed.add_field(name="Location", value="Graveyard", inline=True)
        main_embed.add_field(name="Nearest Warp", value="deepercrypts", inline=True)

        main_embed.add_field(name="Spawning",
                             value="`15%` chance every `40` seconds.\nCapped at `20`",
                             inline=False)
        main_embed.add_field(name="Skills",
                             value="Can push players away in `3` block radius every `1` minute.",
                             inline=False)
        main_embed.add_field(name="General Drops",
                             value="  `0.1%` - Spirit's Axe"
                                   "\n`0.3%` - Spirit Axe's Head"
                                   "\n`0.5%` - Spirit Axe's Handle"
                                   "\n`0.8%` - Forged Crimson",
                             inline=False)

        main_embed.set_footer(text="AxoNavigator",
                              icon_url="https://cdn.discordapp.com/emojis/981320857672618045.webp?size=128&quality=lossless")
        main_embed.set_author(name="Mobs and Bosses",
                              icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/skull-and-crossbones_2620-fe0f.png")
        main_embed.set_thumbnail(
            url="https://mc-heads.net/avatar/9241fee68717a4ccb5830debd8a145a7b3401e5ef545871eafff836150214e53")

        image_embed = Embed(color=Colour.orange())
        image_embed.set_image(
            url="https://cdn.discordapp.com/attachments/965142041623429162/1044607760471445524/image.png")

        await ctx.followup.send(embeds=[main_embed, image_embed])
        return

    if boss_type == "Royal Gargoyle":
        main_embed = Embed(
            title="Royal Gargoyle",
            color=Colour.orange(),
        )

        main_embed.add_field(name="Type", value="Boss", inline=True)
        main_embed.add_field(name="Location", value="Graveyard", inline=True)
        main_embed.add_field(name="Nearest Warp", value="deepercrypts", inline=True)

        main_embed.add_field(name="Spawning",
                             value="Every `6` minutes.\nCapped at `1`",
                             inline=False)
        main_embed.add_field(name="Skills",
                             value="  Can shoot a fireball at player every `4` seconds."
                                   "\nCan push players away in `3` block radius every `30` seconds."
                                   "\nCan teleport players to itself in `4` block radius every `100` seconds.",
                             inline=False)
        main_embed.add_field(name="General Drops",
                             value="  ` 3%` - Infernal Cleaver"
                                   "\n`10%` - Forged Crimson"
                                   "\n`20%` - Gilded Dust",
                             inline=False)
        main_embed.add_field(name="Player-Based Drops",
                             value="  #1 Damager Drops:\n` 5%` - Forged Crimson\n`10%` - Gilded Dust"
                                   "\n#2 Damager Drops:\n` 2%` - Forged Crimson\n` 5%` - Gilded Dust"
                                   "\n#3 Damager Drops:\n` 3%` - Gilded Dust",
                             inline=False)

        main_embed.set_footer(text="AxoNavigator",
                              icon_url="https://cdn.discordapp.com/emojis/981320857672618045.webp?size=128&quality=lossless")
        main_embed.set_author(name="Mobs and Bosses",
                              icon_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/322/skull-and-crossbones_2620-fe0f.png")
        main_embed.set_thumbnail(
            url="https://mc-heads.net/avatar/a89f6303af85877610912dc04b8b1e89724752f0a7eea05ab6547e228179c06f")

        image_embed = Embed(color=Colour.orange())
        image_embed.set_image(
            url="https://cdn.discordapp.com/attachments/965142041623429162/1043916155171115038/image.png")

        await ctx.followup.send(embeds=[main_embed, image_embed])
        return

    await ctx.followup.send(f"I do not have any info about {boss_type} at the moment. Check in later!")
