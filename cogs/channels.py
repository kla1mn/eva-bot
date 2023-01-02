from random import choice

import disnake
from datetime import datetime
from disnake.ext import commands
from disnake import PermissionOverwrite, Embed, TextChannel, Option, OptionType

# <:greencheck:1006659369519304774>
# <:redcross:1006554004320428052>
from tools.getseconds import getseconds


class Channels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.slash_command(
        name='create_text_channel',
        description='Создать текстовый канал',
        options=[
            Option(
                name='name',
                description='Название текстового канала',
                type=OptionType.string,
                required=True),
            Option(
                name='category',
                description='Категория, в которой создастся сцена',
                type=OptionType.channel,
                required=False),
            Option(
                name='topic',
                description='Тема канала',
                type=OptionType.string,
                required=False),
            Option(
                name='slowmode_delay',
                description='Slowmode для канала (не больше 6 часов)',
                type=OptionType.string,
                required=False),
            Option(
                name='position',
                description='Позиция канала в списке',
                type=OptionType.integer,
                required=False
            ),
            Option(
                name='reason',
                description='Причина создания канала',
                type=OptionType.string,
                required=False
            ),
            Option(
                name='nsfw',
                description='Нужно ли каналу возрастное ограничение? (Да/Нет)',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def create_text_channel(self, inter, name: str, category: TextChannel = None, topic: str = None,
                                  slowmode_delay: str = 'a', position: int = 0,
                                  reason: str = None, nsfw: bool = None):

        if category:
            if category.type != disnake.ChannelType.category:
                embed = Embed(
                    title='<:redcross:1006554004320428052> | create text channel',
                    description='Выбери категорию каналов, а не канал!',
                    color=0xde001e
                )
                await inter.send(embed=embed)
                return

        wrong_time = ['Неверное время!',
                      'Неправильное время',
                      'Такое невозможно',
                      'Введи правильное время',
                      'Я знаю точно невозможное возможно... (Неверное время)']

        nsfw_list = ['Да', 'да', 'ес', 'Ес', 'Конечно', 'конечно', 'Yes', 'yes', 'Yeah', 'yeah']

        if nsfw in nsfw_list:
            nsfw = True
        else:
            nsfw = False

        if slowmode_delay == 'a':
            slowmode_delay = 0
        elif slowmode_delay != 'a':
            if not getseconds(slowmode_delay):
                embed = Embed(
                    title='<:redcross:1006554004320428052> | create text channel',
                    description=choice(wrong_time),
                    color=0xde001e)
                await inter.send(embed=embed)
                return
            else:
                slowmode_delay = getseconds(slowmode_delay)

        await inter.guild.create_text_channel(name=name,
                                              topic=topic,
                                              slowmode_delay=slowmode_delay,
                                              position=position,
                                              reason=reason,
                                              nsfw=nsfw,
                                              category=category)

        for channel in inter.guild.channels:
            if channel.name == name:
                channel = self.bot.get_channel(int(channel.id))

        embed = Embed(
            title='<:greencheck:1006659369519304774> | create text channel',
            description=f'УРА! {inter.author.mention} только что создал текстовый канал **{channel.mention}**',
            color=0x8cc63f)
        embed.add_field('Тема канала', topic)
        embed.add_field('Причина создания', reason)
        embed.add_field('NSFW', nsfw)

        await inter.send(embed=embed)

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.slash_command(
        name='create_voice_channel',
        description='Создать канал',
        options=[
            Option(
                name='name',
                description='Название голосового канала',
                type=OptionType.string,
                required=True
            ),
            Option(
                name='category',
                description='Категория, в которой создастся сцена',
                type=OptionType.channel,
                required=False),
            Option(
                name='position',
                description='Позиция канала в списке',
                type=OptionType.integer,
                required=False
            ),
            Option(
                name='user_limit',
                description='Максимальное количество пользователей канала (макс - 99)',
                type=OptionType.integer,
                required=False
            ),
            Option(
                name='reason',
                description='Причина создания канала',
                type=OptionType.string,
                required=False
            ),
            Option(
                name='nsfw',
                description='Нужно ли каналу возрастное ограничение? (Да/Нет)',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def create_voice_channel(self, inter, name: str, category: TextChannel = None, position: int = 0,
                                   user_limit: int = 99, reason: str = None,
                                   nsfw: bool = False):

        if category:
            if category.type != disnake.ChannelType.category:
                embed = Embed(
                    title='<:redcross:1006554004320428052> | create voice channel',
                    description='Выбери категорию каналов, а не канал!',
                    color=0xde001e
                )
                await inter.send(embed=embed)
                return

        nsfw_list = ['Да', 'да', 'ес', 'Ес', 'Конечно', 'конечно', 'Yes', 'yes', 'Yeah', 'yeah']

        if nsfw in nsfw_list:
            nsfw = True
        else:
            nsfw = False

        channel = await inter.guild.create_voice_channel(name=name,
                                                         position=position,
                                                         user_limit=user_limit,
                                                         reason=reason,
                                                         nsfw=nsfw,
                                                         category=category)

        for channel in inter.guild.channels:
            if channel.name == name:
                channel = self.bot.get_channel(int(channel.id))

        embed = Embed(
            title='<:greencheck:1006659369519304774> | create voice channel',
            description=f'УРА! {inter.author.mention} только что создал голосовой канал **{channel.mention}**',
            color=0x8cc63f)
        embed.add_field('Лимит пользователей', user_limit)
        embed.add_field('Причина создания', reason)
        embed.add_field('NSFW', nsfw)

        await inter.send(embed=embed)

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.slash_command(
        name='delete_channel',
        description='Удалить канал',
        options=[
            Option(
                name='channel',
                description='Канал, который надо удалить',
                type=OptionType.channel,
                required=True
            ),
            Option(
                name='reason',
                description='Причина удаления канала',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def delete_channel(self, inter, channel: TextChannel, reason: str = None):
        await channel.delete(reason=reason)

        embed = Embed(
            title='<:greencheck:1006659369519304774> | delete channel',
            description=f'Канал **{channel}** успешно удален!',
            color=0x8cc63f)

        embed.add_field('Модератор', inter.author.mention)
        embed.add_field('Причина', reason)

        await inter.send(embed=embed)

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.slash_command(
        name='create_private_channel',
        description='Создать приватный канал',
        options=[
            Option(
                name='name',
                description='Название текстового канала',
                type=OptionType.string,
                required=True),
            Option(
                name='category',
                description='Категория, в которой создастся сцена',
                type=OptionType.channel,
                required=False),
            Option(
                name='topic',
                description='Тема канала',
                type=OptionType.string,
                required=False),
            Option(
                name='slowmode_delay',
                description='Slowmode для канала (не больше 6 часов)',
                type=OptionType.string,
                required=False),
            Option(
                name='position',
                description='Позиция канала в списке',
                type=OptionType.integer,
                required=False
            ),
            Option(
                name='reason',
                description='Причина создания канала',
                type=OptionType.string,
                required=False
            ),
            Option(
                name='nsfw',
                description='Нужно ли каналу возрастное ограничение? (Да/Нет)',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def create_private_channel(self, inter, name: str, category: TextChannel = None, topic: str = None,
                                     slowmode_delay: str = 'a',
                                     position: int = 0,
                                     reason: str = None, nsfw: bool = False):
        if category:
            if category.type != disnake.ChannelType.category:
                embed = Embed(
                    title='<:redcross:1006554004320428052> | create private channel',
                    description='Выбери категорию каналов, а не канал!',
                    color=0xde001e
                )
                await inter.send(embed=embed, ephemeral=True)
                return

        overwrites = {
            inter.guild.default_role: PermissionOverwrite(view_channel=False),
            inter.guild.me: PermissionOverwrite(view_channel=True)
        }

        wrong_time = ['Неверное время!',
                      'Неправильное время',
                      'Такое невозможно',
                      'Введи правильное время',
                      'Я знаю точно невозможное возможно... (Неверное время)']

        nsfw_list = ['Да', 'да', 'ес', 'Ес', 'Конечно', 'конечно', 'Yes', 'yes', 'Yeah', 'yeah']

        if nsfw in nsfw_list:
            nsfw = True
        else:
            nsfw = False

        if slowmode_delay == 'a':
            slowmode_delay = 0
        elif slowmode_delay != 'a':
            if not getseconds(slowmode_delay):
                embed = Embed(
                    title='<:redcross:1006554004320428052> | create text channel',
                    description=choice(wrong_time),
                    color=0xde001e)
                await inter.send(embed=embed)
                return
            else:
                slowmode_delay = getseconds(slowmode_delay)

        await inter.guild.create_text_channel(name=name,
                                              overwrites=overwrites,
                                              topic=topic,
                                              slowmode_delay=slowmode_delay,
                                              position=position,
                                              reason=reason,
                                              nsfw=nsfw,
                                              category=category)
        for channel in inter.guild.channels:
            if channel.name == name:
                channel = self.bot.get_channel(int(channel.id))

        embed = Embed(
            title='<:greencheck:1006659369519304774> | create private channel',
            description=f'УРА! {inter.author.mention} только что создал приватный текстовый канал '
                        f'**{channel.mention}**',
            color=0x8cc63f)

        embed.add_field('Тема канала', topic)
        embed.add_field('Причина создания', reason)
        embed.add_field('NSFW', nsfw)

        await inter.send(embed=embed, ephemeral=True)

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.slash_command(
        name='create_stage_channel',
        description='Создать сцену',
        options=[
            Option(
                name='name',
                description='Название текстового канала',
                type=OptionType.string,
                required=True),
            Option(
                name='category',
                description='Категория, в которой создастся сцена',
                type=OptionType.channel,
                required=False),
            Option(
                name='topic',
                description='Тема канала',
                type=OptionType.string,
                required=False),
            Option(
                name='position',
                description='Позиция канала в списке',
                type=OptionType.integer,
                required=False
            ),
            Option(
                name='reason',
                description='Причина создания канала',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def create_stage_channel(self, inter, name: str, category: TextChannel = None, topic: str = None,
                                   position: int = 0,
                                   reason: str = None):
        if category:
            if category.type != disnake.ChannelType.category:
                embed = Embed(
                    title='<:redcross:1006554004320428052> | create stage channel',
                    description='Выбери категорию каналов, а не канал!',
                    color=0xde001e
                )
                await inter.send(embed=embed)
                return

        await inter.guild.create_stage_channel(name=name,
                                               topic=topic,
                                               position=position,
                                               reason=reason,
                                               category=category)

        for channel in inter.guild.channels:
            if channel.name == name:
                channel = self.bot.get_channel(int(channel.id))

        embed = Embed(
            title='<:greencheck:1006659369519304774> | create stage channel',
            description=f'УРА! {inter.author.mention} только что создал сцену **{channel.mention}**',
            color=0x8cc63f)
        embed.add_field('Тематика', topic)
        embed.add_field('Причина создания', reason)

        await inter.send(embed=embed)

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.slash_command(
        name='create_forum_channel',
        description='Создать форум',
        options=[
            Option(
                name='name',
                description='Название форума',
                type=OptionType.string,
                required=True),
            Option(
                name='category',
                description='Категория, в которой создастся форум',
                type=OptionType.channel,
                required=False),
            Option(
                name='topic',
                description='Тематика форума',
                type=OptionType.string,
                required=False),
            Option(
                name='position',
                description='Позиция форума в списке',
                type=OptionType.integer,
                required=False
            ),
            Option(
                name='slowmode_delay',
                description='Slowmode для канала (не больше 6 часов)',
                type=OptionType.string,
                required=False),
            Option(
                name='reason',
                description='Причина создания форума',
                type=OptionType.string,
                required=False
            ),
            Option(
                name='nsfw',
                description='Нужно ли каналу возрастное ограничение? (Да/Нет)',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def create_forum_channel(self, inter, name: str, category: TextChannel = None, topic: str = None,
                                   position: int = 0, slowmode_delay: str = 'a',
                                   reason: str = None, nsfw: bool = False):
        if category:
            if category.type != disnake.ChannelType.category:
                embed = Embed(
                    title='<:redcross:1006554004320428052> | create forum channel',
                    description='Выбери категорию каналов, а не канал!',
                    color=0xde001e
                )
                await inter.send(embed=embed)
                return

        wrong_time = ['Неверное время!',
                      'Неправильное время',
                      'Такое невозможно',
                      'Введи правильное время',
                      'Я знаю точно невозможное возможно... (Неверное время)']

        nsfw_list = ['Да', 'да', 'ес', 'Ес', 'Конечно', 'конечно', 'Yes', 'yes', 'Yeah', 'yeah']

        if nsfw in nsfw_list:
            nsfw = True
        else:
            nsfw = False

        if slowmode_delay == 'a':
            slowmode_delay = 0
        elif slowmode_delay != 'a':
            if not getseconds(slowmode_delay):
                embed = Embed(
                    title='<:redcross:1006554004320428052> | create text channel',
                    description=choice(wrong_time),
                    color=0xde001e)
                await inter.send(embed=embed)
                return
            else:
                slowmode_delay = getseconds(slowmode_delay)

        await inter.guild.create_forum_channel(name=name,
                                               topic=topic,
                                               position=position,
                                               reason=reason,
                                               category=category,
                                               slowmode_delay=slowmode_delay,
                                               nsfw=nsfw)

        for ch in inter.guild.channels:
            if ch.name == name:
                channel = self.bot.get_channel(int(ch.id))

        embed = Embed(
            title='<:greencheck:1006659369519304774> | create forum channel',
            description=f'УРА! {inter.author.mention} только что создал форум **{channel.mention}**',
            color=0x8cc63f)
        embed.add_field('Тематика', topic)
        embed.add_field('Причина создания', reason)
        embed.add_field('NSFW', nsfw)

        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Channels(bot))
