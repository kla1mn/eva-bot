from random import choice

import disnake
import datetime
import asyncio
from disnake.ext import commands
from datetime import timedelta
from disnake import Option, OptionType, Member, Embed
import disnake_paginator

from tools.getseconds import getseconds


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''@commands.slash_command(name='aboba')
    async def test(self, inter):
        if 'цветные-роли' in str(inter.guild.channels):
            await inter.send('+')
        elif 'цветные-роли' not in str(inter.guild.channels):
            await inter.send('-')'''

    """@commands.slash_command(
        name='123',
        description='Наполни свою жизнь красками!',
        options=[]
    )
    async def test(self, inter):
        embed = Embed(
            title='<:redcross:1006554004320428052> | colorful roles',
            description='Вы уже создали канал для выбора цвета!',
            color=0xde001e
        )
        test = await inter.channel.send(embed=embed)
        await test.add_reaction(emoji='<:bot:1015958240057638942>')"""


    """@commands.slash_command(name='123')
    async def ping_command(self, inter):
        paginator = disnake_paginator.ButtonPaginator(title="Pong", segments=["Hello", "World"], color=0x00ff00)
        await paginator.start(inter)"""

    '''@commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.slash_command(
        name='ban',
        description='Банит участника',
        options=[
            Option(
                name='member',
                description='Участник, которого надо забанить',
                type=OptionType.user,
                required=True
            ),
            Option(
                name='reason',
                description='Причина бана',
                type=OptionType.string,
                required=False
            ),
            Option(
                name='time',
                description='Время, на которое участник будет забанен',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def tban(self, inter, member: Member, reason: str = None, time: str = None):
        wrongtime = ['Неверное время!',
                     'Неправильное время',
                     'Такое невозможно',
                     'Введи правильное время',
                     'Я знаю точно невозможное возможно...']

        banitself2 = [
            f'Участник **{member.name}** был забанен по причине "**{reason}**" на время - **{time}**',
            f'Участник **{member.name}** не сможет **{time}** находиться на нашем сервере '
            f'по причине "**{reason}**"',
            f'Участник **{member.name}** остается без сладкого на **{time}** по причине "**{reason}**"',
            f'Участник **{member.name}** не сможет играть в майнкрафт **{time}** по причине "**{reason}**"']

        afterban2 = [f'Участник **{member.name}** наконец-то был разбанен',
                     f'Участник **{member.name}** может вернуться к нам на сервер',
                     f'Участник **{member.name}** получает билет в новую жизнь',
                     f'Участник **{member.name}** покушал и теперь готов к новым приключениям',
                     f'Участник **{member.name}** выспался и теперь имеет светлый и ясный ум']

        selfban = ['Ты пытаешься забанить самого себя!',
                   'Ты что творишь?! Себя нельзя банить!',
                   'Даже не думай об этом! Себя нельзя банить!',
                   'Ещё что захотел, нельзя себя банить!',
                   'Давай ты не будешь меня дергать по пустякам, себя нельзя банить!',
                   'Придумай что-нибудь получше, себя нельзя банить!',
                   'Фантазии не хватает? Себя нельзя банить!',
                   '👉🆔<:deletesign:905943741775368272>',
                   'Пошутил и хватит, себя нельзя банить!',
                   'Очень смешно, себя нельзя банить!',
                   'Dino "смееясь во весь голос": себя нельзя банить!',
                   'Подожди, ты только что пытался себя забанить..?']

        banitself = [
            f'Участник **{member.name}** был забанен по причине "**{reason}**" навсегда',
            f'Участник **{member.name}** не сможет больше находиться на нашем сервере '
            f'по причине "**{reason}**"',
            f'Участник **{member.name}** остается без сладкого по причине "**{reason}**"',
            f'Участник **{member.name}** не сможет играть в майнкрафт по причине "**{reason}**"',
            f'Участник **{member.name}** был забанен по причине **{reason}**']

        if time:
            if not getseconds(time):
                embed = Embed(
                    title='<:deletesign:905943741775368272> | ban',
                    description=choice(wrongtime),
                    color=disnake.Color.red())

                await inter.send(embed=embed)
                return

            if member.id == inter.author.id:
                embed = Embed(
                    title='<:deletesign:905943741775368272> | ban',
                    description=choice(selfban),
                    color=disnake.Color.red())

                await inter.send(embed=embed)
                return

            await member.ban(reason=reason)

            embed = Embed(
                title=f'<:checkmark:905943731067305996> | ban',
                description=choice(banitself2),
                color=0x8cc63f)

            await inter.send(embed=embed)

            await asyncio.sleep(getseconds(time))

            embed = Embed(
                title=f'<:checkmark:905943731067305996> | unban',
                description=choice(afterban2),
                color=0x8cc63f)

            await inter.send(embed=embed)

            await member.unban(reason='Истекло время бана.')

        if not time:
            if member.id == inter.author.id:
                embed = Embed(
                    title='<:deletesign:905943741775368272> | ban',
                    description=choice(selfban),
                    color=disnake.Color.red())

                await inter.send(embed=embed)
                return

            await member.ban(reason=reason)

            embed = Embed(
                title=f'<:checkmark:905943731067305996> | ban',
                description=choice(banitself),
                color=0x8cc63f)

            await inter.send(embed=embed)'''

    '''@commands.slash_command(name='embed')
    async def embed(self, inter):
        if not inter.channel.is_nsfw():
            embed = Embed(
                title='title',
                description='description',
                color=0x8cc63f,
                timestamp=datetime.datetime.now()
            )
            embed.add_field('1 field', '1 description// inline=True', inline=True)
            embed.add_field('2 field', '2 description// inline=True', inline=True)
            embed.add_field('3 field', '3 description// inline=False', inline=False)

            embed.set_footer(text='this is footer', icon_url=self.bot.user.avatar.url)
            embed.set_author(name='this is author',
                             icon_url='https://asset.msi.com/global/picture/news/2017/nb/GT75VR20171107-1.jpg')
            embed.set_thumbnail(
                url='https://yt3.ggpht.com/ytc/AMLnZu-idSWIq6y0NCTYADUrzN9bH0gZYFbf0ELiVUKWng=s900-c-k-c0x00ffffff-no-rj')
            embed.set_image(
                url='https://storage-asset.msi.com/global/picture/news/2021/desktop/intel-12th-20211101-1.jpg')

            await inter.send(embed=embed)
        else:
            await inter.send('-')'''

    '''@commands.command(name='test')
    async def test(self, inter, member: Member = None):
        pass'''


def setup(bot):
    bot.add_cog(Test(bot))
