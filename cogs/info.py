import asyncio
from random import choice

import disnake
from disnake import Embed, Member
from disnake.ext import commands

from tools.getseconds import getseconds

NEWS_SMILE = u'\U000025FE'


## <:greencheck:1006659369519304774>
## <:redcross:1006554004320428052>
# (<CustomActivity name=None emoji=<PartialEmoji animated=True name='advaith_anim' id=889887673425199124>>, <Activity type=<ActivityType.playing: 0> name='PyCharm' url=None details='Idling' application_id=626024502664495115 session_id=None emoji=None>)

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['пользователь', 'user', 'человек', 'member'])
    async def _user_info(self, inter, member: Member = None):
        users = ['Крутой чел!', 'Ля какой!', 'Ого какой!', 'А он мне нравится :)', 'Давай дружить)', 'Крутая аватарка!',
                 'Это мой друг!', 'А я его знаю)', 'Это мой кореш!', 'Красивое имя!', 'А ты интересный)']

        bot = ['Я крутая🧡', 'Люблю себя!', 'А я красивая такая 🥰', 'Какая красотка 😍', 'Ох какая девушка 🥵',
               'Я красотка!', 'Какая крутышка тут 🧡', '', '', '', '', '', '', '']

        if member:
            info_embed = Embed(color=0x8cc63f)

            info_embed.set_author(name=f'Информация о пользователе {member.name}')

            info_embed.add_field('Главное', f'🆔 ID пользователя: **{member.id}**'
                                            f'\n📅 Дата регистрации: <t:{int(member.created_at.timestamp())}>',
                                 inline=False)

            if member.activity:
                activity = member.activity.name
            else:
                activity = 'Никакой активности нет'

            if member.raw_status == 'dnd':
                _status = f'<:red:1011999474865942599> | Не беспокоить'
            elif inter.author.raw_status == 'idle':
                _status = f'<:yellow:1011999476363309147> | Неактивен'
            elif inter.author.raw_status == 'online':
                _status = f'<:green:1011999473511174254> | В сети'
            else:
                _status = f'<:gray:1011999472160616478>  | Не в сети'

            info_embed.add_field('Активность', f'🎭 Статус: {_status}'
                                               f'\n🎏 Активность сейчас: **{activity}**', inline=False)

            info_embed.add_field('Пользователь на сервере', f'💹 Наивысшая роль: {member.top_role.mention}'
                                                            f'\n📅 Дата вступления на сервер: '
                                                            f'<t:{int(member.joined_at.timestamp())}>', inline=False)

            if member.avatar:
                info_embed.set_thumbnail(url=member.avatar.url)

            if member.id == 986548404207366184:
                text = choice(bot)
            else:
                text = choice(users)

            info_embed.set_footer(icon_url=self.bot.user.avatar.url, text=text)

            await inter.send(embed=info_embed)

        else:
            info_embed = Embed(color=0x8cc63f)

            info_embed.set_author(name=f'Информация о пользователе {inter.author.name}')

            info_embed.add_field('Главное', f'🆔 ID пользователя: **{inter.author.id}**'
                                            f'\n📅 Дата регистрации: <t:{int(inter.author.created_at.timestamp())}>',
                                 inline=False)

            if inter.author.activity:
                activity = inter.author.activity.name
            else:
                activity = 'Никакой активности нет'

            if inter.author.raw_status == 'dnd':
                _status = f'<:red:1011999474865942599> | Не беспокоить'
            elif inter.author.raw_status == 'idle':
                _status = f'<:yellow:1011999476363309147> | Неактивен'
            elif inter.author.raw_status == 'online':
                _status = f'<:green:1011999473511174254> | В сети'
            else:
                _status = f'<:gray:1011999472160616478>  | Не в сети'

            info_embed.add_field('Активность', f'🎭 Статус: {_status}'
                                               f'\n🎏 Активность сейчас: **{activity}**', inline=False)

            info_embed.add_field('Пользователь на сервере', f'💹 Наивысшая роль: {inter.author.top_role.mention}'
                                                            f'\n📅 Дата вступления на сервер: '
                                                            f'<t:{int(inter.author.joined_at.timestamp())}>',
                                 inline=False)

            if inter.author.avatar:
                info_embed.set_thumbnail(url=inter.author.display_avatar.url)

            info_embed.set_footer(icon_url=self.bot.user.avatar.url, text=choice(users))

            await inter.send(embed=info_embed)

    @commands.command(aliases=['разраб', 'хозяин', 'владелец', 'разработчик'])
    async def developer(self, inter):
        user = await self.bot.fetch_user(712926134794453003)

        embed = Embed(
            title='Информация о разработчике бота',
            color=0x8cc63f)

        embed.add_field('Информация обо мне:', f'Имя - Костян'
                                               f'\nГород - Екатеринбург'
                                               f'\nВозраст - 17 лет', inline=False)
        embed.add_field('Любимый цвет', '#8cc63f', inline=False)
        # embed.add_field('Мой аккаунт создан:', f'<t:{int(member.created_at.timestamp())}>', inline=False)
        embed.add_field('Мой **ВК**:', f'https://vk.com/62white', inline=False)
        embed.add_field('Мой **ТГ канал**:', f'https://t.me/+6At1JdJWK3gyMTIy', inline=False)
        embed.add_field('Мой **ИНСТ**:', f'https://instagram.com/kla1mn', inline=False)
        embed.add_field('Я в дискорде:', f'{user.mention}', inline=False)
        # embed.add_field('Активность сейчас:', f'{member.desktop_status}')
        # embed.add_field('Мой статус сейчас:', member.desktop_status, inline=False)
        embed.set_image(url='https://images-ext-1.discordapp.net/external/p2fq1Lbv5O5y7DXRAffXg1mgElDyMu0Cerl'
                            'AvjHIcwE/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/712926134794453003/ddb822'
                            'f8d802a66c6deac7e34969c24b.png?width=702&height=702')

        await inter.send(embed=embed)
        return

    @commands.command(aliases=['бот', 'bot', 'bot info', 'ты'])
    async def f_bot_info_(self, inter):
        embed = Embed(color=0x8cc63f)

        user = await self.bot.fetch_user(712926134794453003)

        embed.add_field(f'Основная информация:', f'Создатель: {user.mention}'
                                                 f'\nКоличество серверов: ``{str(len(self.bot.guilds))}``'
                                                 f'\nКоличество пользователей: ``{str(len(self.bot.users))}``')

        embed.add_field(f'Техническая информация:',
                        f'Python ``3.9.1`` \nDisnake ``{disnake.__version__}`` \nPyCharm ``2020.3.5``'
                        f'\nPing: ``{str(self.bot.latency * 1000)[:5]}ms`` ', inline=False)

        embed.set_footer(text='kla1mn#1423 © 2022 Все права защищены', icon_url=user.avatar.url)
        embed.set_author(icon_url=self.bot.user.avatar.url, name=f'Информация о боте {self.bot.user}')
        embed.set_image(url=self.bot.user.avatar.url)

        await inter.send(embed=embed)

    @commands.command(
        aliases=['server', 'guild', 'guildinfo', 'serverinfo', 'guild info', 'server info', 'guild_info', 'server_info',
                 'сервер', 'гильдия'])
    async def _guild_info(self, inter):

        server = ['Мне нравится этот сервер!', 'Хороший сервер!', 'А тут уютно!', 'Крутой сервер, не так ли?',
                  'Зови друзей, будем веселиться вместе!', 'Я переезжаю на этот сервер', 'Тут так здорово!!']

        info_embed = Embed(color=0x8cc63f)

        info_embed.set_author(name=f'Информация о {inter.guild.name}')

        if inter.guild.icon:
            info_embed.set_thumbnail(url=inter.guild.icon.url)

        info_embed.add_field('📄 Описание ', f'{inter.guild.description}', inline=False)

        info_embed.add_field('Главное', f'👑 Владелец: {inter.guild.owner.mention}'
                                        f'\n👥 Количество участников: **{inter.guild.member_count}**'
                                        f'\n🆔 ID сервера: **{inter.guild.id}**'
                                        f'\n📅 Дата создания: <t:{int(inter.guild.created_at.timestamp())}>',
                             inline=False)

        info_embed.add_field(f'Каналы: **{len(inter.guild.channels) - len(inter.guild.categories)}**',
                             f'\n🎫 Категории: **{len(inter.guild.categories)}**'
                             f'\n💬 Текстовые каналы: **{len(inter.guild.text_channels)}**'
                             f'\n🎧 Голосовые каналы: **{len(inter.guild.voice_channels)}**'
                             f'\n🏟 Сцены: **{len(inter.guild.stage_channels)}**'
                             f'\n👨‍👩‍👧‍👦 Форумы: **{len(inter.guild.forum_channels)}**'
                             f'\n⚜ Ветки: **{len(inter.guild.threads)}**'
                             f'\n🛌 AFK канал: **{inter.guild.afk_channel}**'
                             f'\n🛠 Системный канал: **{inter.guild.system_channel}**', inline=False)

        info_embed.add_field('Ты на этом сервере', f'📅 Дата вступления на сервер: '
                                                   f'<t:{int(inter.author.joined_at.timestamp())}>'
                                                   f'\n👶 Дата регистрации: '
                                                   f'<t:{int(inter.author.created_at.timestamp())}>,'
                                                   f'\n💹 Наивысшая роль: {inter.author.top_role.mention}',
                             inline=False)
        info_embed.add_field('Стикеры и эмодзи', f'🎭 Количество стикеров: **{len(inter.guild.stickers)}**'
                                                 f'\n🎑 Лимит стикеров: **{inter.guild.sticker_limit}**'
                                                 f'\n🧸 Количество эмодзи: **{len(inter.guild.emojis)}**'
                                                 f'\n🎏 Лимит эмодзи: **{inter.guild.emoji_limit}**', inline=False)

        info_embed.add_field('Остальная информация', f'🎎 Всего ролей: **{len(inter.guild.roles)}**'
                                                     f'\n🔞 Уровень NSFW: **{str(inter.guild.nsfw_level)[10:]}**'
                                                     f'\n⏱ AFK тайм-аут: **{int(inter.guild.afk_timeout / 60)} минут**'
                                                     f'\n👥 Максимум участников: **{inter.guild.max_members}**',
                             inline=False)

        info_embed.set_footer(icon_url=self.bot.user.avatar.url, text=choice(server))

        await inter.send(embed=info_embed)

    @commands.command(aliases=['таймер', 'будильник', 'напоминалка'])
    async def timer(self, inter, time: str, *, value: str = None):
        embed = Embed(
            title='⏲ | Таймер установлен',
            description=f'Через ``{time}`` я напомню Вам {value}',
            color=0x8cc63f
        )
        await inter.send(embed=embed)

        await asyncio.sleep(getseconds(time))

        remind_choice = [f'{inter.author.mention}, ты хотел {value}',
                         f'{inter.author.mention}, напоминаю о {value}',
                         f'{inter.author.mention}, {time} назад ты просил напомнить о {value}']

        embed = Embed(
            title='⏲ | Сработал таймер',
            description=choice(remind_choice),
            color=0x8cc63f
        )
        await inter.send(embed=embed)

    @commands.command(aliases=['баны', 'банысервера', 'баны сервера', 'guild bans', 'guildbans'])
    async def bans(self, inter):
        embed = Embed(
            title=f'Баны на сервере {inter.guild.name}',
            color=0x8cc63f)

        bans = await inter.guild.bans(limit=1000).flatten()
        k, i = 0, 1
        for reason, user in bans:
            embed.add_field(f'{i}. Имя: {user}',
                            f'Причина: **{reason}**'
                            f'\nID: ``{user.id}``', inline=False)
            k += 1
        embed.set_footer(text=f'Всего банов: {k}')
        if inter.guild.icon:
            embed.set_thumbnail(url=inter.guild.icon.url)

        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
