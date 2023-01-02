from random import choice, randint, sample

import aiohttp
import disnake
from disnake import Embed, Option, OptionType
from disnake.ext import commands


## <:greencheck:1006659369519304774>
## <:redcross:1006554004320428052>


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """@commands.slash_command(
        name='user_ping',
        description='Красиво пингует пользователя (за это можно получить мут/бан)',
        options=[
            Option(
                name='member',
                description='Кого пингануть',
                type=OptionType.user,
                required=True
            )
        ]
    )
    async def user_ping(self, inter, member: Member):
        pingvariations = ['Вас пинганули!',
                          'Подойти уже к телефону!',
                          'Возьми трубку!',
                          'Ответь уже!',
                          'Тебя зовут!',
                          'Нужна твоя помощь!',
                          'Нам нужно твое внимание!',
                          'Ты нам нужен!',
                          'Ай да сюда, беляши стынут!']

        embed = Embed(
            title=choice(pingvariations),
            description=f'{member.mention}, тебя зовет **{inter.author.name}**',
            color=0x8cc63f)

        # embed.set_footer(text=inter.author)
        await inter.send(embed=embed)"""

    """@commands.slash_command(
        name='prediction',
        description='Предсказание на день',
        options=[])
    async def prediction(self, inter):
        predictions = ['Даря своей любимой букет из ромашек, пересчитайте все лепестки. Должно быть: любит!',
                       'Ожидая плохого события, не крутите пуговицу: она обязательно оторвется.',
                       'Вы счастливчик! Поэтому будьте скромней и не хватайте больше счастливых билетов.',
                       'Переходя дорогу, посмотрите по сторонам — есть вероятность встретить свою судьбу.',
                       'Заходите к начальнику с левой ноги — и вас ждет повышение по службе.',
                       'Улыбайтесь всегда! И никто не назовет вас мрачным человеком. '
                       'Молчите! И никто не назовет занудой.',
                       'Жизнь ваша — бесконечная дорога, поэтому выберите надежное средство для передвижения '
                       'по ней — автомобиль.',
                       'Сегодня для вас самый лучший день! Как и все остальные!',
                       'Купите книгу, которая вам совершенно не нравится, — и вы найдете ответы на все вопросы.',
                       'В течение первой недели после встречи Нового Года тебя ждёт приятный сюрприз.',
                       'Выйдя из подъезда из своего дома, поверни голову направо. '
                       'Марка стоящей там машины — скоро появится и у тебя.',
                       'Если 1 июня вы оденете наизнанку одежду, то на вас обратят внимание много людей '
                       'противоположного пола. Может быть, вы встретите любовь!',
                       'Если в хлебе вам попадется инородное тело, знайте — это на счастье!',
                       'Звезды благосклонны к вам. Однако не стоит вылавливать их в миске с салатом, '
                       'иначе мощное влияние Марса может способствовать вещим сновидениям под столом.',
                       'Венера во втором доме предвещает плотный ужин с излишествами и умеренной '
                       'физической нагрузкой на танцполе.',
                       'Для вашего знака Зодиака противопоказаны ритуальные танцы на столе, '
                       'в противном случае возможна нелицеприятная встреча в казенном доме.',
                       'Люди вашего знака улыбчивы, веселы, разговорчивы, смешливы… эй, милейший, не слишком ли вы '
                       'налегли на шампанское?',
                       'Звезды расположены не лучшим образом: наиболее подверженными ритмичным подергиваниям '
                       'будут коленные, кистевые, локтевые и тазобедренный суставы.',
                       'Ваша планета–покровительница Меркурий предвещает вам неожиданный поворот событий '
                       'после вашего тоста за любовь.',
                       'С сегодняшнего дня вы находитесь под покровительством планеты Венера, '
                       'которая преподнесет вам новую неожиданную любовь.',
                       'Этой ночью звезды расположились на небе так, что вам светит все, '
                       'что вы так давно мечтали получить.']
        embed = Embed(
            title='Ваше предсказание:',
            description=choice(predictions),
            color=0x8cc63f)

        await inter.send(embed=embed)"""

    @commands.slash_command(
        name='dog',
        description='Шабака',
        options=[])
    async def dog(self, inter):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()

        dogs = ['Шабака!', 'Песель!', 'Собакен!',
                'Пес!', 'Барбос!', 'Пушистик!', 'Милаха!']

        embed = Embed(
            title=choice(dogs),
            color=disnake.Color.light_grey()
        )
        embed.set_image(url=dogjson['link'])
        await inter.send(embed=embed)

    @commands.slash_command(
        name='cat',
        description='Владелец мира',
        options=[])
    async def cat(self, inter):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            catjson = await request.json()

        cats = ['Пушистик!', 'Кошак!', 'Котик!', 'Мурлыка!',
                'Лапочка!', 'Милаха!', 'Котофей!', 'Мохнатик!', 'Мяу!']

        embed = Embed(
            title=choice(cats),
            color=disnake.Color.light_grey()
        )
        embed.set_image(url=catjson['link'])
        await inter.send(embed=embed)

    @commands.slash_command(
        name='panda',
        description='Папапанда',
        options=[])
    async def panda(self, inter):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/panda')
            pandajson = await request.json()

        pandas = ['Панда!', 'Пандочка!', 'Кунг-Фу мастер!',
                  'Лапочка!', 'Милаха!', 'Мохнатик!']

        embed = Embed(
            title=choice(pandas),
            color=0xffffff
        )
        embed.set_image(url=pandajson['link'])
        await inter.send(embed=embed)

    @commands.slash_command(
        name='raccoon',
        description='янот',
        options=[])
    async def raccoon(self, inter):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/racoon')
            racoonjson = await request.json()

        pandas = ['Енот!', 'Енотик!!', 'Пушистик!',
                  'Лапочка!', 'Милаха!', 'Мохнатик!']

        embed = Embed(
            title=choice(pandas),
            color=disnake.Color.darker_gray()
        )
        embed.set_image(url=racoonjson['link'])
        await inter.send(embed=embed)

    @commands.slash_command(
        name='red_panda',
        description='красная папапанда',
        options=[])
    async def red_panda(self, inter):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/red_panda')
            red_pandajson = await request.json()

        pandas = ['Панда!', 'Пандочка!', 'Кунг-Фу мастер!',
                  'Лапочка!', 'Милаха!', 'Мохнатик!']

        embed = Embed(
            title=choice(pandas),
            color=disnake.Color.dark_orange()
        )
        embed.set_image(url=red_pandajson['link'])
        await inter.send(embed=embed)

    @commands.slash_command(
        name='try',
        description='Попытать свою удачу',
        options=[
            Option(
                name='value',
                description='Что будем пробовать?',
                type=OptionType.string,
                required=True
            )
        ]
    )
    async def tryy(self, inter, value: str):
        a = randint(0, 1)
        if a == 0:
            embed = Embed(
                title='<:redcross:1006554004320428052> | Неудачно!',
                description=f'**{inter.author.name}** неудачно {value}',
                color=disnake.Color.red()
            )
            await inter.send(embed=embed)
        else:
            embed = Embed(
                title='<:greencheck:1006659369519304774> | Успешно!',
                description=f'**{inter.author.name}** успешно {value}',
                color=disnake.Color.green()
            )
            await inter.send(embed=embed)

    @commands.slash_command(
        name='rickroll',
        description='Зарикроль друга',
        options=[]
    )
    async def rickroll(self, inter):
        rick = ['Never gonna give u up..',
                'Попался..', 'Да, опять!', 'Нэвэр гона гив ю ап..',
                'Beluga has rickrolled u((', 'Привет от Rick Astley!',
                'Вот и рикролл..', 'Снова он..']
        rick_gif = ['https://c.tenor.com/_4YgA77ExHEAAAAd/rick-roll.gif',
                    'https://c.tenor.com/VFFJ8Ei3C2IAAAAM/rickroll-rick.gif',
                    'https://i.pinimg.com/originals/56/06/9c/56069caf073a95badaa1734e0b569229.gif',
                    'https://www.gifcen.com/wp-content/uploads/2022/03/rickroll-gif.gif',
                    'https://www.gifcen.com/wp-content/uploads/2022/03/rickroll-gif-5.gif',
                    'https://thumbs.gfycat.com/FlawlessThirdCurlew-size_restricted.gif',
                    'https://thumbs.gfycat.com/AdmirableFearfulKangaroo-max-1mb.gif',
                    'https://cs.pikabu.ru/images/big_size_comm/2011-11_2/13205301988881.gif',
                    'https://64.media.tumblr.com/ad123e3a538194e29fdda4d2ec3f84a0/e21028f37a15dd08-4f/'
                    's500x750/44cbdea7280a21ab618d87c95301b54ca2ab32de.gifv']

        embed = Embed(
            title=choice(rick),
            color=disnake.Color.light_grey()
        )
        embed.set_image(url=choice(rick_gif))

        await inter.send(embed=embed)

    @commands.slash_command(
        name='skala',
        description='Хмм..',
        options=[]
    )
    async def skala(self, inter):
        skala_gif = ['https://c.tenor.com/k1wbOgEPazIAAAAM/the-rock-sus-meme-the-rock-sus.gif',
                     'https://c.tenor.com/25FN1Vr-YlEAAAAd/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0.gif',
                     'https://c.tenor.com/qwR44XG-f5kAAAAM/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0.gif',
                     'https://c.tenor.com/m-A0IoleYTkAAAAC/%D1%81%D0%BA%D0%B0%D0%BB%D0%B0-skala.gif',
                     'https://i.gifer.com/origin/e1/e1a0362291858704234da89172062e65_w200.gif',
                     'https://i.gifer.com/origin/6a/6a67d44d843c6ffbc5c5b459611ae98c_w200.gif',
                     'https://c.tenor.com/gHBcYHRee1QAAAAM/dwayne-the-rock-johnson-rock.gif',
                     'https://static.life.ru/publications/2020/8/3/816306494625.1201.gif',
                     'https://i.gifer.com/G05K.gif',
                     'https://i.gifer.com/origin/4c/4c5093a2559fa2db7ea477566b7e3723_w200.gif',
                     'https://i.gifer.com/origin/57/57257374676fe35674e38da0bc010919_w200.gif',
                     'https://i.gifer.com/origin/dc/dc05fbc02db1cf5af55fce2b588cde48_w200.gif']

        embed = Embed(
            color=disnake.Color.dark_grey()
        )
        embed.set_image(url=choice(skala_gif))

        await inter.send(embed=embed)

    @commands.slash_command(
        name='password',
        description='Генерация пароля',
        options=[
            Option(
                name='length',
                description='Длина пароля',
                type=OptionType.integer,
                required=True
            )
        ]
    )
    async def password(self, inter, length: int):
        lower_case = 'abcdefghijklmnopqrstuvwxyz'
        upper_case = lower_case.upper()
        numbers = '1234567890'
        symbols = '!?/._'
        use_for = lower_case + upper_case + numbers + symbols
        length_for_pass = length

        if length > 67:
            await inter.send(embed=Embed(
                title='<:redcross:1006554004320428052> | password',
                description='Слишком много символов!',
                color=disnake.Color.red()
            ))
        else:
            password = ''.join(sample(use_for, length_for_pass))
            embed = Embed(
                title=f'Ваш пароль - {password}',
                description='Внимание! Скоро данное сообщение исчезнет!',
                color=disnake.Color.red()
            )

            await inter.send(embed=embed, ephemeral=True)

    @commands.slash_command(
        name='magic_ball',
        description='Магический шар на все случаи жизни',
        options=[
            Option(
                name='value',
                description='В чем Вы сомневаетесь?',
                type=OptionType.string,
                required=True
            )
        ]
    )
    async def magic_ball(self, inter, value: str):
        variety = ['Да', 'Нет', 'Возможно', 'Наверное нет..', 'Скоро', 'Не смогла сосредоточиться, давай еще раз',
                   'Лучше не надо', 'Я не знаю', 'Подумай самостоятельно']
        embed = Embed(
            title='🔮 | Магический шар',
            description=f'{value} {choice(variety)}',
            color=0x8cc63f,
        )
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))


'''@bot.command()
async def SendPepe(ctx):
    emb = discord.Embed(title = "Pepe", colour=discord.Colour.dark_green())
    emb.set_image(url = "https://i.imgur.com/Hab3RJO.jpg")
    await ctx.send(embed = emb'''

''', icon_url=inter.author.avatar'''

'''0xe38a76'''

'''0x03f4fc'''

'''request2 = await session.get('https://some-random-api.ml/facts/racoon')
            racoonfactjson = await request2.json()
            
    ,
            description=racoonfactjson['fact'],'''

'''https://some-random-api.ml/animu/hug'''
