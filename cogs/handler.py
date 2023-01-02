import datetime

from disnake.ext import commands
from disnake import Embed


# <:checkmark:905943731067305996>
# <:deletesign:905943741775368272>

# <:tick:1006284280240025671>
# <:redcross:1006285060888076289>

## <:greencheck:1006659369519304774>
## <:redcross:1006554004320428052>


class Handler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter, error):
        if isinstance(error, commands.MissingPermissions):
            embed = Embed(
                title='<:redcross:1006554004320428052> | missing permissions',
                description='Ого! Кажется, у тебя недостаточно прав, чтобы использовать эту команду('
                            '\nПопроси роль покруче или дождись карьерного роста (лучше попроси)',
                color=0xde001e
            )
            await inter.send(embed=embed)

        elif isinstance(error, commands.BotMissingPermissions):

            embed = Embed(
                title='<:redcross:1006554004320428052> | bot missing permissions',
                description='Боту не хватает прав! Быстро дай боту нужные права! Шевелись!',
                color=0xde001e
            )
            await inter.send(embed=embed)

        elif isinstance(error, commands.CommandInvokeError):
            print(f'ERROR: {error.original}')

            embed = Embed(
                title='<:redcross:1006554004320428052> | error',
                description='Упс..'
                            '\nВыглядит так, будто возникла ошибка в работе бота!'
                            '\nОбязательно сообщи об этом разработчикам! (используй **/bug**)',
                color=0xde001e
            )
            await inter.send(embed=embed)

        elif isinstance(error, commands.CommandOnCooldown):

            embed = Embed(
                title='<:redcross:1006554004320428052> | Ошибка!',
                description=f"Команда {inter.command.name} на перезарядке. Она доступна только 1 раз за "
                            f"'{datetime.datetime.fromtimestamp(error.cooldown.per).strftime('%H:%M:%S')}'. "
                            f"Попробуйте через "
                            f"'{datetime.datetime.fromtimestamp(error.retry_after).strftime('%H:%M:%S')}'.",
                color=0xde001e
            )
            await inter.send(embed=embed)

        elif isinstance(error, commands.BadArgument):

            embed = Embed(
                title='<:redcross:1006554004320428052> | bad argument',
                description='Кажется, ты ввел какой-то аргумент неверно! '
                            '\nНе отчаивайся и попробуй заново!!',
                color=0xde001e
            )
            await inter.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, inter, error):
        if isinstance(error, commands.MissingPermissions):
            embed = Embed(
                title='<:redcross:1006554004320428052> | missing permissions',
                description='Ого! Кажется, у тебя недостаточно прав, чтобы использовать эту команду('
                            '\nПопроси роль покруче или дождись карьерного роста (лучше попроси)',
                color=0xde001e
            )
            await inter.send(embed=embed)

        elif isinstance(error, commands.BotMissingPermissions):

            embed = Embed(
                title='<:redcross:1006554004320428052> | bot missing permissions',
                description='Боту не хватает прав! Быстро дай боту нужные права! Шевелись!',
                color=0xde001e
            )
            await inter.send(embed=embed)

        elif isinstance(error, commands.CommandInvokeError):
            print(f'ERROR: {error.original}')

            embed = Embed(
                title='<:redcross:1006554004320428052> | error',
                description='Упс..'
                            '\nВыглядит так, будто возникла ошибка в работе бота!'
                            '\nОбязательно сообщи об этом разработчикам! (используй **/bug**)',
                color=0xde001e
            )
            await inter.send(embed=embed)

        elif isinstance(error, commands.CommandOnCooldown):

            embed = Embed(
                title='<:redcross:1006554004320428052> | Ошибка!',
                description=f"Команда {inter.command.name} на перезарядке. Она доступна только 1 раз за "
                            f"'{datetime.datetime.fromtimestamp(error.cooldown.per).strftime('%H:%M:%S')}'. "
                            f"Попробуйте через "
                            f"'{datetime.datetime.fromtimestamp(error.retry_after).strftime('%H:%M:%S')}'.",
                color=0xde001e
            )
            await inter.send(embed=embed)

        elif isinstance(error, commands.BadArgument):

            embed = Embed(
                title='<:redcross:1006554004320428052> | bad argument',
                description='Кажется, ты ввел какой-то аргумент неверно! '
                            '\nНе отчаивайся и попробуй заново!!',
                color=0xde001e
            )
            await inter.send(embed=embed)

        '''elif isinstance(error, commands.errors.CommandNotFound):

            embed = Embed(
                title='<:redcross:1006554004320428052> | Ошибка!',
                description='Такой команды не существует! Проверь правильность написания (либо подбери синоним :))!',
                color=0xde001e
            )
            await inter.send(embed=embed)'''


def setup(bot):
    bot.add_cog(Handler(bot))
