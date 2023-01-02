import disnake
from disnake import Embed, Option, OptionType
from disnake.ext import commands


class Maths(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='bin',
        description='Перевод из десятичной системы счисления в двоичную ',
        options=[
            Option(
                name='number',
                description='Число, которое будем переводить в двоичную СС',
                type=OptionType.integer,
                required=True
            )
        ]
    )
    async def binn(self, inter, number: int):
        number2 = bin(number)
        embed = Embed(
            title='Результат вычислений',
            description=f'**{number}**₁₀ = **{number2[2:]}**₂',
            color=disnake.Color.orange())

        await inter.send(embed=embed)

    @commands.slash_command(
        name='hex',
        description='Перевод из десятичной системы счисления в шестнадцатеричную ',
        options=[
            Option(
                name='number',
                description='Число, которое будем переводить в шестнадцатеричную СС',
                type=OptionType.integer,
                required=True
            )
        ]
    )
    async def hexx(self, inter, number: int):
        number2 = hex(number).upper()
        embed = Embed(
            title='Результат вычислений',
            description=f'**{number}**₁₀ = **{number2[2:]}**₁₆',
            color=disnake.Color.orange())

        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(Maths(bot))
