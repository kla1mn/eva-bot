import aiohttp
import disnake

from random import choice, randint, random, sample

from disnake.ext import commands
from disnake import Embed, Option, OptionType, Member


class Nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='neko',
        description='ничего особенного',
        options=[],
        # guild_ids=[986549993676632136]
    )
    async def neko(self, inter):
        if inter.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/nsfw/neko')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])

                await inter.send(embed=embed)
        else:
            embed = Embed(
                title='Тихо тихо..',
                description='**Здесь** такое смотреть нельзя!'
                            '\nПопробуй в **другом** канале...',
                color=disnake.Color.red()
            )
            await inter.author.send(embed=embed)

    @commands.command(
        name='waifu',
        description='Вай!! Фуууууу...',
        options=[]
    )
    async def waifu(self, inter):
        if inter.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/nsfw/waifu')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])

                await inter.send(embed=embed)
        else:
            embed = Embed(
                title='Тихо тихо..',
                description='**Здесь** такое смотреть нельзя!'
                            '\nПопробуй в **другом** канале...',
                color=disnake.Color.red()
            )
            await inter.author.send(embed=embed)

    @commands.command(
        name='bjob',
        description='какая-то скользкая работа..',
        options=[]
    )
    async def bjob(self, inter):
        if inter.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/nsfw/blowjob')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])

                await inter.send(embed=embed)
        else:
            embed = Embed(
                title='Тихо тихо..',
                description='**Здесь** такое смотреть нельзя!'
                            '\nПопробуй в **другом** канале...',
                color=disnake.Color.red()
            )
            await inter.author.send(embed=embed)


def setup(bot):
    bot.add_cog(Nsfw(bot))
