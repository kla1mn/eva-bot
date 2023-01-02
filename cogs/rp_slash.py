import aiohttp
import disnake

import datetime
from datetime import datetime

from translate import Translator
from random import choice, randint, random, sample

from disnake.ext import commands
from disnake import Embed, Option, OptionType, Member

## <:greencheck:1006659369519304774>
## <:redcross:1006554004320428052>


class RolePlaySlash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='hug',
        description='Обними другого пользователя',
        options=[
            Option(
                name='member',
                description='Кого обнять',
                type=OptionType.user,
                required=False
            )
        ]
    )
    async def _hug(self, inter, member: Member = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | hug',
                description='Ты попытался обнять себя, так делать не надо!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/hug')
                hug_json = await request.json()
            embed = Embed(color=0x8cc63f)
            embed.set_image(url=hug_json['url'])
            await inter.send(embed=embed)
            return
        else:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/hug')
                hug_json = await request.json()

            hugs = ['Обнимашки!', 'Иди обниму!', 'Мило!', 'Обнимахи!',
                    'Пора няшиться!', 'Ня!', '╰(*°▽°*)╯', '༼ つ ◕_◕ ༽つ']

            embed = Embed(
                title=choice(hugs),
                description=f'**{inter.author.mention} обнимает {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=hug_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='pat',
        description='Погладить другого пользователя',
        options=[
            Option(
                name='member',
                description='Кого погладить',
                type=OptionType.user,
                required=False
            )
        ]
    )
    async def _pat(self, inter, member: Member = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | pat',
                description='Ты попытался погладить себя, так делать не надо!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/pat')
                pat_json = await request.json()
            embed = Embed(color=0x8cc63f)
            embed.set_image(url=pat_json['url'])
            await inter.send(embed=embed)
            return
        else:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/pat')
                pat_json = await request.json()

            pats = ['Иди поглажу!', 'Мило!', 'ᓚᘏᗢ', '^_^',
                    'Можно тебя погладить?', '╰(*°▽°*)╯', '༼ つ ◕_◕ ༽つ']

            embed = Embed(
                title=choice(pats),
                description=f'**{inter.author.mention} гладит {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=pat_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='wink',
        description='Подмигнуть другому пользователя',
        options=[
            Option(
                name='member',
                description='Кому подмигнуть',
                type=OptionType.user,
                required=False
            )
        ]
    )
    async def _wink(self, inter, member: Member = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | wink',
                description='Ты попытался подмигнуть самому себе, так делать не надо!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/wink')
                wink_json = await request.json()

                embed = Embed(color=0x8cc63f)
                embed.set_image(url=wink_json['url'])
                await inter.send(embed=embed)
                return
        else:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/wink')
                wink_json = await request.json()

            winks = ['Чпуньк!', 'Мило!', 'ᓚᘏᗢ',
                     'НЯ!', '╰(*°▽°*)╯', '༼ つ ◕_◕ ༽つ']

            embed = Embed(
                title=choice(winks),
                description=f'**{inter.author.mention} подмигивает {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=wink_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='kiss',
        description='Поцеловать пользователя',
        options=[
            Option(
                name='member',
                description='Кого поцеловать',
                type=OptionType.user,
                required=False
            )
        ]
    )
    async def _kiss(self, inter, member: Member = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | kiss',
                description='Ты попытался поцеловать себя, так делать не надо!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/kiss')
                kiss_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=kiss_json['url'])
                await inter.send(embed=embed)
        else:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/kiss')
                kiss_json = await request.json()

            kisses = ['Целую тебя!', 'Дай расцелую тебя!', 'Мило!', 'Целовашки!',
                      'Пора целоваться!', 'Чмок!', '╰(*°▽°*)╯', '༼ つ ◕_◕ ༽つ']

            embed = Embed(
                title=choice(kisses),
                description=f'**{inter.author.mention} целует {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=kiss_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='bite',
        description='Укусить пользователя',
        options=[
            Option(
                name='member',
                description='Кого укусить',
                type=OptionType.user,
                required=False
            )
        ]
    )
    async def _bite(self, inter, member: Member = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | bite',
                description='Ты попытался укусить себя, так делать не надо!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/bite')
                bite_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=bite_json['url'])
                await inter.send(embed=embed)
        else:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/bite')
                bite_json = await request.json()

            bites = ['Кусь тебя!', 'Ррррр..', 'Кусаюсь!', 'Кусяю!',
                     'Пора кусаться..', 'Кусь!']

            embed = Embed(
                title=choice(bites),
                description=f'**{inter.author.mention} кусает {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=bite_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='blush',
        description='Покраснеть и засмущаться',
        options=[
            Option(
                name='member',
                description='Из-за кого смущаться',
                type=OptionType.user,
                required=False
            )
        ]
    )
    async def _blush(self, inter, member: Member = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | blush',
                description='Ты попытался смутить самого себя, так делать не надо!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/blush')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
        else:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/blush')
                blush_json = await request.json()

            bites = ['Uwu', 'НЯ!', '╰(*°▽°*)╯', '(*/ω＼*)',
                     'Засмущали', 'Ну не смущайте меня..']

            embed = Embed(
                title=choice(bites),
                description=f'**{inter.author.mention} засмущался и покраснел из-за {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='cringe',
        description='Крииииииинж',
        options=[
            Option(
                name='member',
                description='Кто источник кринжа',
                type=OptionType.user,
                required=False
            )
        ]
    )
    async def _cringe(self, inter, member: Member = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | cringe',
                description='Ты кринжанул себя, так делать не надо!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/cringe')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
        else:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/cringe')
                blush_json = await request.json()

            bites = ['Мда..', 'Фейспам..', 'Вот это прикол..',
                     'Да уж..', 'Крииииинж']

            embed = Embed(
                title=choice(bites),
                description=f'**{member.mention} источник безумного криииииинжа**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='cry',
        description='Поплакать((',
        options=[
            Option(
                name='member',
                description='Из-за кого плачем',
                type=OptionType.user,
                required=False
            ),
            Option(
                name='reason',
                description='Из-за чего плачем',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def _cry(self, inter, member: Member = None, reason: str = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | cry',
                description='Не надо плакать из-за себя!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/cry')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
        elif member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/cry')
                blush_json = await request.json()

            bites = ['Грустно(', 'Грустно и невкусно', 'Плак плак',
                     ':((', 'ಥ_ಥ']

            embed = Embed(
                title=choice(bites),
                description=f'**Плачу из-за {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)
        elif not member and reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/cry')
                blush_json = await request.json()

            bites = ['Грустно(', 'Грустно и невкусно', 'Плак плак',
                     ':((', 'ಥ_ಥ']

            embed = Embed(
                title=choice(bites),
                description=f'**Плачу, потому что {reason}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)
        elif member and reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/cry')
                blush_json = await request.json()

            bites = ['Грустно(', 'Грустно и невкусно', 'Плак плак',
                     ':((', 'ಥ_ಥ']

            embed = Embed(
                title=choice(bites),
                description=f'**Плачу из-за {member.mention}, потому что {reason}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='dance',
        description='Танцуют все!',
        options=[
            Option(
                name='reason',
                description='Повод танцевать',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def _dance(self, inter, reason: str = None):
        if not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/dance')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
                return
        if reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/dance')
                blush_json = await request.json()

            bites = ['Танцуем!', 'Танцуют все!', 'тыц тыц тыц',
                     'Пляшем!', ]

            embed = Embed(
                title=choice(bites),
                description=f'**Танцую потому, что **{reason}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)
            return

    @commands.slash_command(
        name='lick',
        description='Ну давай, лизни',
        options=[
            Option(
                name='member',
                description='Кого лизнем?',
                type=OptionType.user,
                required=False
            )
        ]
    )
    async def _lick(self, inter, member: Member = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | lick',
                description='Ты попытался облизать себя, так делать не надо!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/lick')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
        else:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/lick')
                blush_json = await request.json()

            bites = ['Лизь', 'Ну лизни давай', 'Lick',
                     'Лизну!', ]

            embed = Embed(
                title=choice(bites),
                description=f'**{inter.author.mention}** лизнул **{member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='handhold',
        description='Возьмемся за ручки?)',
        options=[
            Option(
                name='member',
                description='Кого берем за ручку?',
                type=OptionType.user,
                required=False
            ),
            Option(
                name='reason',
                description='Зачем берем за ручку?',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def _handhold(self, inter, member: Member = None, reason: str = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | handhold',
                description='Не надо брать себя за ручки!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/handhold')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
        elif member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/handhold')
                blush_json = await request.json()

            bites = ['#жмурукукаждому', 'Жмяк!', 'Возьмемся за ручки?',
                     ':)', '(❁´◡`❁)']

            embed = Embed(
                title=choice(bites),
                description=f'**Беру за руку {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)
        elif member and reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/handhold')
                blush_json = await request.json()

            bites = ['#жмурукукаждому', 'Жмяк!', 'Возьмемся за ручки?',
                     ':)', '(❁´◡`❁)']

            embed = Embed(
                title=choice(bites),
                description=f'**Беру за руку {member.mention}, потому что {reason}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='smile',
        description='Улыбнись!',
        options=[
            Option(
                name='member',
                description='Кому улыбаемся?',
                type=OptionType.user,
                required=False
            ),
            Option(
                name='reason',
                description='А почему улыбаемся?',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def _smile(self, inter, member: Member = None, reason: str = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | smile',
                description='Не надо улыбаться себе!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/smile')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
        elif member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/smile')
                blush_json = await request.json()

            bites = ['Хы)', 'Улыбаки!', 'Улыбаюсь)',
                     '☺', '(*/ω＼*)']

            embed = Embed(
                title=choice(bites),
                description=f'**Улыбаюсь {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)
        elif member and reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/smile')
                blush_json = await request.json()

            bites = ['Хы)', 'Улыбаки!', 'Улыбаюсь)',
                     '☺', '(*/ω＼*)']

            embed = Embed(
                title=choice(bites),
                description=f'**Улыбаюсь {member.mention}, потому что {reason}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='wave',
        description='Машем ручкой!',
        options=[
            Option(
                name='member',
                description='Кому машем?',
                type=OptionType.user,
                required=False
            ),
            Option(
                name='reason',
                description='А зачем машем?',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def _wave(self, inter, member: Member = None, reason: str = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | wave',
                description='Не надо махать себе!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/wave')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
        elif member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/wave')
                blush_json = await request.json()

            bites = ['Привет!', 'Машем рукой!', '✋🙂',
                     '🤗', '🖐']

            embed = Embed(
                title=choice(bites),
                description=f'**Машу рукой {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)
        elif member and reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/wave')
                blush_json = await request.json()

            bites = ['Привет!', 'Машем рукой!', '✋🙂',
                     '🤗', '🖐']

            embed = Embed(
                title=choice(bites),
                description=f'**Машу рукой {member.mention}, потому что {reason}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='highfive',
        description='Дай пять!',
        options=[
            Option(
                name='member',
                description='Кому даем пять!',
                type=OptionType.user,
                required=False
            ),
            Option(
                name='reason',
                description='Почему даем пять?',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def _highfive(self, inter, member: Member = None, reason: str = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | highfive',
                description='Не надо давать пять себе!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/highfive')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
        elif member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/highfive')
                blush_json = await request.json()

            bites = ['Дай пятюню!', 'Лови пять!', '🤜🤛',
                     '👊', '🤚']

            embed = Embed(
                title=choice(bites),
                description=f'**Даю пять {member.mention}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)
        elif member and reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/highfive')
                blush_json = await request.json()

            bites = ['Дай пятюню!', 'Лови пять!', '🤜🤛',
                     '👊', '🤚']

            embed = Embed(
                title=choice(bites),
                description=f'**Даю пять {member.mention}, потому что {reason}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='happy',
        description='Просто счастье',
        options=[Option(
                name='reason',
                description='Почему ты счастлив?',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def _happy(self, inter, reason: str = None):

        if not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/happy')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
        elif reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/happy')
                blush_json = await request.json()

            embed = Embed(
                description=f'**Счастлив(а), потому что {reason}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)

    @commands.slash_command(
        name='slap',
        description='Дай ему пощечину!',
        options=[
            Option(
                name='member',
                description='Кому пощечину даем?',
                type=OptionType.user,
                required=False
            ),
            Option(
                name='reason',
                description='За что пощечину?',
                type=OptionType.string,
                required=False
            )
        ]
    )
    async def _slap(self, inter, member: Member = None, reason: str = None):
        if member == inter.author:
            embed = Embed(
                title='<:redcross:1006554004320428052> | slap',
                description='Не надо бить себя!',
                color=disnake.Color.red())
            await inter.send(embed=embed, ephemeral=True)
            return
        if not member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/slap')
                blush_json = await request.json()
                embed = Embed(color=0x8cc63f)
                embed.set_image(url=blush_json['url'])
                await inter.send(embed=embed)
        elif member and not reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/slap')
                blush_json = await request.json()

            bites = ['Лови пощечину!', 'Лови леща!', 'Уххх..',
                     'Смачно..', 'Жестко..']

            embed = Embed(
                title=choice(bites),
                description=f'**Даю пощечину {member.mention}!**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)
        elif member and reason:
            async with aiohttp.ClientSession() as session:
                request = await session.get('https://api.waifu.pics/sfw/slap')
                blush_json = await request.json()

            bites = ['Лови пощечину!', 'Лови леща!', 'Уххх..',
                     'Смачно..', 'Жестко..']

            embed = Embed(
                title=choice(bites),
                description=f'**Даю пощечину {member.mention}, потому что {reason}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(RolePlaySlash(bot))
