import discord
from discord.ext import commands


class SystemCommands(commands.Cog):
    @commands.command(pass_context=True)
    async def help(self, ctx, arg=None):
        help_embed = discord.Embed(
            title="Help",
            description="Learn commands and how to use them here!",
            color=0xFFF8A2,
        )
        if arg == "nsfw":
            help_embed.add_field(
                name="$sauce <code>",
                value="Display information and a thumbnail about the provided saucecode.",
                inline=False,
            )
            help_embed.add_field(
                name="$randsauce",
                value="Generate a random valid saucecode and display information about it.",
                inline=False,
            )
            help_embed.add_field(
                name="$nekohavatar",
                value="Sends a NSFW profile picture.",
                inline=False,
            )
            help_embed.add_field(
                name='$nekolewd',
                value="Sends a lewd neko picture.",
                inline=False,
            )
            help_embed.set_footer(
                text="Mayuko",
                icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg",
            )
            await ctx.send(embed=help_embed)
        if arg == "hori":
            help_embed.add_field(
                name="$hori ass",
                value="Ass focused content.",
                inline=False,
            )
            help_embed.add_field(
                name="$hori ecchi",
                value="Slightly explicit sexual content. It can show full to partial nudity, including nipples. Doesn't show any genital.",
                inline=False,
            )
            help_embed.add_field(
                name="$hori ero",
                value="Any kind of erotic content, basically any nsfw image.",
                inline=False,
            )
            help_embed.add_field(
                name="$hori hentai",
                value="Explicit sexual content.",
                inline=False,
            )
            help_embed.add_field(
                name="$hori maid",
                value="A woman or girl employed to do domestic work.",
                inline=False,
            )
            help_embed.add_field(
                name="$hori milf",
                value="A sexually attractive middle-aged woman.",
                inline=False,
            )
            help_embed.add_field(
                name="$hori oppai",
                value="Boobs focused content.",
                inline=False,
            )
            help_embed.add_field(
                name="$hori oral",
                value="Oral sex content.",
                inline=False,
            )
            help_embed.add_field(
                name="$hori paizuri",
                value="A subcategory of hentai that involves breast sex, also known as titty fucking.",
                inline=False,
            )
            help_embed.add_field(
                name="$hori selfies",
                value="A girl taking a lewd picture of herself.",
                inline=False,
            )
            help_embed.add_field(
                name="$hori uniform",
                value="Girls wearing any kind of uniform.",
                inline=False,
            )
            help_embed.set_footer(
                text="Mayuko",
                icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg",
            )
            await ctx.send(embed=help_embed)
        if arg == None:
            help_embed.add_field(
                name="$waifu",
                value="Pull a random Waifu or Husbando from MyWaifuList.moe",
                inline=False,
            )

            help_embed.add_field(
                name='$anisearch <Anime name>',
                value="Search for an anime by name on Anilist.co",
                inline=False,
            )
            help_embed.add_field(
                name='$charsearch <Character name>',
                value="Search for a character by name on Anilist.co",
                inline=False,
            )
            help_embed.add_field(
                name='$nekoavatar',
                value="Sends a new profile picture.",
                inline=False,
            )
            help_embed.add_field(
                name='$info',
                value="Send a description of the bot, personified.",
                inline=False
            )
            help_embed.add_field(
                name="$changelog",
                value="View historical changes about Mayuko.",
                inline=False,
            )
            help_embed.add_field(
                name="$help hori",
                value="View hori commands",
                inline=False
            )
            help_embed.add_field(
                name="$help nsfw",
                value="View NSFW commands.",
                inline=False,
            )
            help_embed.set_footer(
                text="Mayuko",
                icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg",
            )
            await ctx.send(embed=help_embed)

    @commands.command(pass_context=True)
    async def changelog(self, ctx):
        await ctx.send("Changelog is available at https://github.com/DynamicDonkey/Mayuko/blob/master/assets/CHANGELOG.md")
        await ctx.send("Happy hacking!")

    @commands.command(name="info")
    async def info(self, ctx):
        info_embed = discord.Embed(
            title="Hi there!",
            color=0xFFF8A2
        )
        info_embed.set_thumbnail(
            url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg")
        info_embed.add_field(
            name="About me",
            value="I'm Mayuko, but you can call me Ma-chan if you'd like. I'm a huge otaku with nearly infinite knowledge of all things anime, including the magic numbers~! Since I'm not actually human, you can look at my code on [GitHub](https://github.com/DynamicDonkey/Mayuko). I've gotta get back to what I was watching now, but if you need me, just type `$help` and I'll be right over!",
            inline=False
        )
        info_embed.set_author(name="Mayuko Kirisu", url="https://github.com/DynamicDonkey/Mayuko",
                              icon_url="https://raw.githubusercontent.com/DynamicDonkey/Mayuko/master/assets/pfp.jpg")
        await ctx.send(embed=info_embed)
