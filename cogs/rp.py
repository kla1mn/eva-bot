from random import choice

import aiohttp
import disnake
from disnake import Embed, Option, OptionType, Member
from disnake.ext import commands


## <:greencheck:1006659369519304774>
## <:redcross:1006554004320428052>


class RolePlay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['обнять', 'обнимаемся', 'обнимахи', 'обняться', 'обнимаю'])
    async def hug(self, inter, member: Member = None):
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

    @commands.command(aliases=['погладить', 'гладить', 'поглажу', 'глажу'])
    async def pat(self, inter, member: Member = None):
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

    @commands.command(aliases=['подмигнуть', 'мигнуть', 'подмигиваю'])
    async def wink(self, inter, member: Member = None):
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

    @commands.command(aliases=['целовать', 'поцеловать', 'целую'])
    async def kiss(self, inter, member: Member = None):
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

    @commands.command(aliases=['укусить', 'кусать', 'кусить', 'кусаю'])
    async def bite(self, inter, member: Member = None):
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

    @commands.command(aliases=['смущаться', 'засмущаться', 'смущаюсь', 'засмущался'])
    async def blush(self, inter, member: Member = None):
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

    @commands.command(aliases=['кринж', 'криндж'])
    async def cringe(self, inter, member: Member = None):
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

    @commands.command(aliases=['плакать', 'заплакать', 'плак', 'плачу'])
    async def cry(self, inter, member: Member = None, *, reason: str = None):
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

    @commands.command(aliases=['танцевать', 'танцую', 'потанцевать'])
    async def dance(self, inter, *, reason: str = None):
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

    @commands.command(aliases=['лизнуть', 'лизать', 'лижу', 'лизну'])
    async def lick(self, inter, member: Member = None):
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

    @commands.command(aliaese=['ручки', 'касание'])
    async def handhold(self, inter, member: Member = None, *, reason: str = None):
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

    @commands.command(aliases=['улыбаться', 'улыбаюсь', 'улыбнуться'])
    async def smile(self, inter, member: Member = None, *, reason: str = None):
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

    @commands.command(aliases=['махать', 'помахать', 'машу', 'помашу'])
    async def wave(self, inter, member: Member = None, *, reason: str = None):
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

    @commands.command(aliases=['дай пять', 'даю пять'])
    async def highfive(self, inter, member: Member = None, *, reason: str = None):
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

    @commands.command(aliases=['счастье', 'счастлив', 'счастлива'])
    async def happy(self, inter, *, reason: str = None):
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
                description=f'**{inter.author} счастлив(а), потому что {reason}**',
                color=0x8cc63f)

            embed.set_image(url=blush_json['url'])

            await inter.send(embed=embed)

    @commands.command(aliases=['пощечина', 'лещ', 'даю пощечину', 'даю леща'])
    async def slap(self, inter, member: Member = None, *, reason: str = None):
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
    bot.add_cog(RolePlay(bot))
