from asyncio import sleep
from random import choice, randint

import disnake
# import datetime
import asyncio
from disnake.ext import commands
from datetime import timedelta
from disnake import Option, OptionType, Member, Embed, Intents, Message

# <:greencheck:1006659369519304774> #
# <:redcross:1006554004320428052> #

bad_words = ['anal', 'anus', 'arse', 'ass', 'ballsack', 'bastard', 'bitch', 'biatch', 'bloody', 'blowjob', 'blow job',
             'bollock', 'bollok', 'boner', 'boob', 'bugger', 'bum', 'butt', 'buttplug', 'clitoris', 'cock', 'coon',
             'crap', 'cunt', 'dick', 'dildo', 'dyke', 'fag', 'feck', 'fellate', 'fellatio',
             'felching', 'fuck', 'f u c k', 'fudgepacker', 'fudge packer', 'flange', 'Goddamn', 'God damn', 'homo',
             'jerk', 'jizz', 'knobend', 'knob end', 'labia', 'lmfao', 'muff', 'nigger', 'nigga', 'penis', 'piss',
             'poop', 'prick', 'pube', 'pussy', 'queer', 'scrotum',
             'shit', 's hit', 'sh1t', 'slut', 'smegma', 'spunk', 'tit', 'tosser', 'turd', 'twat', 'vagina', 'wank',
             'whore', 'пидор', 'ниггер', 'нига', 'нигер', 'нага', 'пидор', 'пидорас', 'педик', 'гомик', 'хач', 'даун',
             'дебил', 'retard', 'virgin', 'simp', 'incel', 'cunt', 'бля',
             'блять', 'сука', 'долбоеб', 'уебан', 'гнида', 'мразь', 'мразота', 'уебище', 'уебок', 'хуесос', 'хуй',
             'нахуй', 'хуевина', 'хуевина', 'манда', 'мандахуевина', 'пиздоблятский', 'пиздоблятская', 'юлять', 'дурак',
             'дура', 'хрень', 'хер', 'нахер', 'гандон', 'гондон', 'лох', 'лошара', 'пизда', 'пиздец', 'пиздабол',
             'негр', 'ебать', 'piдорас', 'пидорас', 'piдoрaс', 'рidoras', 'суки', 'блят']


class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        dm = ['Балбес?', 'Такие слова хорошие ребята не говорят..', 'Такие слова хорошие ребята не используют..',
              'Это что за слово такое?', 'Мы не любим такие слова!', 'Не надо использовать такой жаргон..',
              'Ну что за слова такие! Особенно при девушке(', 'Хоть бы постеснялся кто-нибудь..',
              'При девушке некрасиво так говорить!', 'Не используй такие слова, пожалуйста)',
              'Ради меня, не используй такие слова..', 'Вот я уйду с этого сервера, вот тогда и ругайся так!',
              'Я тебя вижу!', 'С первого раза не понятно?', 'Я вижу всех!', 'Я все слышу!',
              'Такие слова хорошие ребята не говорят..', 'Такие слова хорошие ребята не используют..',
              'Это что за слово такое?', 'Мы не любим такие слова!', 'Не надо использовать такой жаргон..',
              'Ну что за слова такие! Особенно при девушке(', 'Хоть бы постеснялся кто-нибудь..',
              'При девушке некрасиво так говорить!', 'Не используй такие слова, пожалуйста)',
              'Ради меня, не используй такие слова..', 'Вот я уйду с этого сервера, вот тогда и ругайся так!',
              'Я тебя вижу!', 'С первого раза не понятно?', 'Я вижу всех!', 'Я все слышу!',
              'Такие слова хорошие ребята не говорят..', 'Такие слова хорошие ребята не используют..',
              'Это что за слово такое?', 'Мы не любим такие слова!', 'Не надо использовать такой жаргон..',
              'Ну что за слова такие! Особенно при девушке(', 'Хоть бы постеснялся кто-нибудь..',
              'При девушке некрасиво так говорить!', 'Не используй такие слова, пожалуйста)',
              'Ради меня, не используй такие слова..', 'Вот я уйду с этого сервера, вот тогда и ругайся так!',
              'Я тебя вижу!', 'С первого раза не понятно?', 'Я вижу всех!', 'Я все слышу!',
              'Такие слова хорошие ребята не говорят..', 'Такие слова хорошие ребята не используют..',
              'Это что за слово такое?', 'Мы не любим такие слова!', 'Не надо использовать такой жаргон..',
              'Ну что за слова такие! Особенно при девушке(', 'Хоть бы постеснялся кто-нибудь..',
              'При девушке некрасиво так говорить!', 'Не используй такие слова, пожалуйста)',
              'Ради меня, не используй такие слова..', 'Вот я уйду с этого сервера, вот тогда и ругайся так!',
              'Я тебя вижу!', 'С первого раза не понятно?', 'Я вижу всех!', 'Я все слышу!',
              'Такие слова хорошие ребята не говорят..', 'Такие слова хорошие ребята не используют..',
              'Это что за слово такое?', 'Мы не любим такие слова!', 'Не надо использовать такой жаргон..',
              'Ну что за слова такие! Особенно при девушке(', 'Хоть бы постеснялся кто-нибудь..',
              'При девушке некрасиво так говорить!', 'Не используй такие слова, пожалуйста)',
              'Ради меня, не используй такие слова..', 'Вот я уйду с этого сервера, вот тогда и ругайся так!',
              'Я тебя вижу!', 'С первого раза не понятно?', 'Я вижу всех!', 'Я все слышу!',
              'Такие слова хорошие ребята не говорят..', 'Такие слова хорошие ребята не используют..',
              'Это что за слово такое?', 'Мы не любим такие слова!', 'Не надо использовать такой жаргон..',
              'Ну что за слова такие! Особенно при девушке(', 'Хоть бы постеснялся кто-нибудь..',
              'При девушке некрасиво так говорить!', 'Не используй такие слова, пожалуйста)',
              'Ради меня, не используй такие слова..', 'Вот я уйду с этого сервера, вот тогда и ругайся так!',
              'Я тебя вижу!', 'С первого раза не понятно?', 'Я вижу всех!', 'Я все слышу!']

        images = [
            'https://cdn.discordapp.com/attachments/1009866989105324155/1009867571065012315/IMG_8537.PNG?size=4096',
            'https://cdn.discordapp.com/attachments/1009866989105324155/1009867532733268068/IMG_8535.PNG?size=4096',
            'https://cdn.discordapp.com/attachments/1009866989105324155/1009867532016029767/IMG_8533.PNG?size=4096',
            'https://cdn.discordapp.com/attachments/1009866989105324155/1009867409718517880/IMG_8526.PNG?size=4096',
            'https://cdn.discordapp.com/attachments/1009866989105324155/1009867406719598732/IMG_8520.PNG?size=4096',
            'https://cdn.discordapp.com/attachments/1009866989105324155/1009867341116477479/IMG_8516.PNG?size=4096',
            'https://cdn.discordapp.com/attachments/1009866989105324155/1009867337572302949/IMG_8510.PNG?size=4096',
            'https://cdn.discordapp.com/attachments/1009866989105324155/1009867215253811230/IMG_8491.PNG?size=4096']

        caps = ['Отключи caps!', 'CAPS!', 'Капсом мы не пользуемся(', 'CAPS LOCK', 'Давай без капса!']

        msg = message.content.lower()
        for i in msg.split():
            if i in bad_words:
                await message.delete()
                await message.author.send(choice(dm))
                image = randint(0, 1)
                if image == 1:
                    await message.author.send(choice(images))
                    return
                else:
                    return

        """if msg.upper() == message.content:
            await message.delete()
            await message.author.send(choice(caps))
            image = randint(0, 1)
            if image == 1:
                await message.author.send(choice(images))
                return
            else:
                pass"""


def setup(bot):
    bot.add_cog(AutoMod(bot))
