import requests
import discord
import json
from discord.ext import commands
from bs4 import BeautifulSoup

# YANDEREDEV MODE...
# ACTIVAAAAATE!


class HoriCommands(commands.Cog):
    @commands.command(name="hori")
    @commands.is_nsfw()
    async def hori(self, ctx, arg):
        if arg == "ass":
            response = requests.get("https://api.hori.ovh/nsfw/ass/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)
        elif arg == "ecchi":
            response = requests.get("https://api.hori.ovh/nsfw/ecchi/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)
        elif arg == "ero":
            response = requests.get("https://api.hori.ovh/nsfw/ero/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)
        elif arg == "hentai":
            response = requests.get("https://api.hori.ovh/nsfw/hentai/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)
        elif arg == "maid":
            response = requests.get("https://api.hori.ovh/nsfw/maid/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)
        elif arg == "milf":
            response = requests.get("https://api.hori.ovh/nsfw/milf/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)
        elif arg == "oppai":
            response = requests.get("https://api.hori.ovh/nsfw/oppai/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)
        elif arg == "oral":
            response = requests.get("https://api.hori.ovh/nsfw/oral/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)
        elif arg == "paizuri":
            response = requests.get("https://api.hori.ovh/nsfw/paizuri/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)
        elif arg == "selfies":
            response = requests.get("https://api.hori.ovh/nsfw/selfies/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)
        elif arg == "uniform":
            response = requests.get("https://api.hori.ovh/nsfw/uniform/")
            soup = BeautifulSoup(response.content, "html.parser")
            string = str(soup)
            result = json.loads(string)

        hori_embed = discord.Embed(
            title="Hori",
            description="Here's the image you ordered~!",
            url=result["url"]
        )
        hori_embed.set_image(url=result["url"])
        await ctx.send(embed=hori_embed)
