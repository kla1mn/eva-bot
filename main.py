import datetime
import json
import os
from asyncio import sleep

import disnake
from disnake.ext import commands
from disnake.flags import Intents

import config


'''def get_prefix(bot, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]'''


if config.debug:
    bot = commands.Bot(command_prefix='bot ', test_guilds=config.test_guilds, intents=Intents.all())
else:
    bot = commands.Bot(command_prefix='bot ', sync_commands_debug=True, intents=Intents.all())

bot.remove_command("help")


'''@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "bot "
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)'''


'''@bot.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)'''


'''@commands.has_permissions(administrator=True)
@bot.slash_command(
    name='prefix',
    description='Смена префикса бота eva',
    options=[
        disnake.Option(
            name='new_prefix',
            description='Новый префикс',
            type=disnake.OptionType.string,
            required=False
        )
    ]
)
async def _setprefix(inter, new_prefix: str = 'bot '):
    with open("prefixes.json", 'r') as f:
        prefix = json.load(f)
    prefix[str(inter.guild.id)] = new_prefix
    with open("prefixes.json", 'w') as f:
        json.dump(prefix, f, indent=4)
        embed = disnake.Embed(
            title='<:greencheck:1006659369519304774> | set prefix',
            description=f'Успешно установлен новый префикс `{new_prefix}`'
                        f'\nМодератор - {inter.author.mention}',
            color=0x8cc63f,
            timestamp=datetime.datetime.now()
        )
    await inter.send(embed=embed)


@commands.has_permissions(administrator=True)
@bot.command(aliases=['смена префикса', 'set prefix', 'set_prefix', 'смени префикс '])
async def setprefix(inter, *, new_prefix: str = 'bot '):
    with open("prefixes.json", 'r') as f:
        prefix = json.load(f)
    prefix[str(inter.guild.id)] = new_prefix
    with open("prefixes.json", 'w') as f:
        json.dump(prefix, f, indent=4)
        embed = disnake.Embed(
            title='<:greencheck:1006659369519304774> | set prefix',
            description=f'Успешно установлен новый префикс `{new_prefix}`'
                        f'\nМодератор - {inter.author.mention}',
            color=0x8cc63f,
            timestamp=datetime.datetime.now()
        )
    await inter.send(embed=embed)'''


@bot.event
async def on_ready():
    print('Бот готов Вам помочь!')
    print('Загружаю коги...')
    print('------------------------------------------------')

    for name in os.listdir('./cogs'):
        if name.endswith('.py'):
            bot.load_extension(f'cogs.{name[:-3]}')
            print(f'Ког {name} был успешно загружен.')

    bot.load_extension('jishaku')
    print('------------------------------------------------')
    print('Загрузил все коги!')

    if config.debug:
        while True:
            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('Бот в разработке.'))
            await sleep(1)
            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('Бот в разработке..'))
            await sleep(1)
            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('Бот в разработке...'))
            await sleep(1)
            '''await bot.change_presence(status=disnake.Status.streaming,
                activity=disnake.Streaming(name=f'на {len(bot.guilds)} серверах', url='https://www.twitch.tv'))
            await sleep(10)'''
    else:
        while True:
            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('/help'))
            await sleep(5)

            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('Добро пожаловать!'))
            await sleep(5)

            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('!музыка недоступна!'))
            await sleep(5)

            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('#evaforever'))
            await sleep(5)

            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('!музыка недоступна!'))
            await sleep(5)

            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('developer: kla1mn#1423   '))
            await sleep(10)

            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('!музыка недоступна!'))
            await sleep(5)

            await bot.change_presence(status=disnake.Status.dnd,
                                      activity=disnake.Game('developer: kla1mn#1423   '))
            await sleep(10)


@bot.command(aliases=['скажи', 'повтори', 'repeat'])
async def say(ctx, *, echo_value: str):
    await ctx.send(echo_value)


@bot.command()
async def l(ctx, extension):
    if ctx.author.id in config.devs:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Загружаю ког: {extension}')


@bot.command()
async def u(ctx, extension):
    if ctx.author.id in config.devs:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Выгружаю ког: {extension}')


@bot.command()
async def r(ctx, extension):
    if ctx.author.id in config.devs:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'Перезагружаю ког: {extension}')


bot.run(config.token)

# <:deletesign:905943741775368272>
# <:checkmark:905943731067305996>

'''@bot.command(pass_context=True)
async def servers(ctx):
    await ctx.send(f"Количество серверов, на которых я есть: {str(len(bot.guilds))}")'''

"""    welcome_channel = bot.get_channel(986549994326724630)
    embed = Embed(
        title='Добро пожаловать!',
        color=0x8cc63f,
        timestamp=datetime.now(),
        description=f'Рады тебя видеть, {member.mention}! '
                    f'\nТы попал на сервер **"{member.guild.name}"**'
                    f'\nЧтобы узнать команды бота **eva** пропиши **/help**'
    )
    await welcome_channel.send(embed=embed)
"""

'''@bot.command()   
async def baka(ctx, member: disnake.Member):
    r = requests.get(f"https://tenor.com/search/hug-anime-gifs")
    soup = BeautifulSoup(r.content, 'html.parser')
    div = soup.findAll("div", class_="Sticker")
    gif = []
    for link in div[0:15]:
        links = link.find("img").get('src')
        gif.append(links)
    embed = Embed(color=0xff9900, title=f"{member.name} ты Baka")
    embed.set_image(url=choice(gif))
    await ctx.send(embed=embed)'''

''' покупка рекламы   '''
'   продажа рекламы лс   '
'''await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                        '))
        await sleep(0.5)
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('с                       '))
        await sleep(0.5)
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' с                      '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  с                     '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   с                    '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    с                   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     с                  '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      с                 '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       с                '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        с               '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('         с              '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('          с             '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('           с            '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('            с           '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('             с          '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('              с         '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('               с        '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                с       '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                 с      '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                  с     '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                   с    '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                    с   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('л                   c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' л                  c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  л                 c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   л                c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    л               c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     л              c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      л             c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       л            c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        л           c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('         л          c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('          л         c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('           л        c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('            л       c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('             л      c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('              л     c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('               л    c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                л   c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                 л  c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                  л c   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                   лc   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('ы                  лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' ы                 лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  ы                лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   ы               лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    ы              лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     ы             лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      ы            лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       ы           лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        ы          лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('         ы         лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('          ы        лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('           ы       лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('            ы      лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('             ы     лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('              ы    лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('               ы   лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                ы  лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                 ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('м                ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' м               ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  м              ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   м             ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    м            ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     м           ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      м          ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       м         ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        м        ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('         м       ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('          м      ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('           м     ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('            м    ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('             м   ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('              м  ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('               м ы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('                мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('а               мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' а              мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  а             мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   а            мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    а           мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     а          мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      а         мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       а        мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        а       мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('         а      мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('          а     мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('           а    мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('            а   мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('             а  мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('              а мы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('               амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('л              амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' л             амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  л            амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   л           амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    л          амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     л         амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      л        амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       л       амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        л      амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('         л     амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('          л    амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('           л   амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('            л  амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('             л амы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('              ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('к             ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' к            ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  к           ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   к          ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    к         ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     к        ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      к       ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       к      ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        к     ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('         к    ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('          к   ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('           к  ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('            к ламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('             кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('е            кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' е           кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  е          кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   е         кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    е        кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     е       кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      е      кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       е     кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        е    кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('         е   кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('          е  кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('           е кламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('            екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('р           екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' р          екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  р         екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   р        екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    р       екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     р      екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      р     екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       р    екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        р   екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('         р  екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('          р екламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('           рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('а          рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' а         рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  а        рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   а       рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    а      рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     а     рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      а    рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       а   рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        а  рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('         а рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('ж        а рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' ж       а рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  ж      а рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   ж     а рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    ж    а рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     ж   а рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      ж  а рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       ж а рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('        жа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('а       жа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' а      жа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  а     жа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   а    жа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    а   жа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     а  жа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      а жа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('       ажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('д      ажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' д     ажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  д    ажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   д   ажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    д  ажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     д ажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('      дажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('о     дажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' о    дажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  о   дажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   о  дажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    о дажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('     одажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('р    одажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' р   одажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  р  одажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('   р одажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('    родажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('п   родажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game(' п  родажа рекламы лс   '))
        await bot.change_presence(status=disnake.Status.do_not_disturb,
                                  activity=disnake.Game('  п родажа рекламы лс   '))'''
