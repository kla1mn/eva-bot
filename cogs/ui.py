from disnake.ext import commands
import disnake


class Buttons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label='Нельзя нажимать!',
                       style=disnake.ButtonStyle.red,
                       disabled=False,
                       emoji='💥')
    async def tap_me_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.send('Просто кнопка, зачем ты нажал(а)?', ephemeral=False)
        

class Ui(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='red_button',
                            description='Сюда нельзя нажимать!')
    async def button(self, inter):
        await inter.send('Не нажимай на кнопку!', view=Buttons())


def setup(bot):
    bot.add_cog(Ui(bot))
