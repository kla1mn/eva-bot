from datetime import datetime

from disnake.ext import commands
import disnake


class ModalWindow(disnake.ui.Modal):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super(ModalWindow, self).__init__(title='Ого, ошибка!', components=[
            disnake.ui.TextInput(
                label='Опиши все максимально подробно 🤗',
                placeholder='У меня не работает команда бана, бла бла бла..',
                custom_id='Описание ошибки от пользователя:',
                max_length=2000,
                min_length=10,
                style=disnake.TextInputStyle.paragraph
            )
        ])

    async def callback(self, interaction: disnake.ModalInteraction):
        bug_report_channel = self.bot.get_channel(1013850420025770045)
        embed = disnake.Embed(
            title='Разработчики подъем! К нам прилетела **ошибка/баг**!',
            timestamp=datetime.now(),
            color=disnake.Color.brand_red())
        for key, value in interaction.text_values.items():
            embed.add_field(name=key, value=value)
        embed.set_author(icon_url=interaction.author.display_avatar.url,
                         name=f'{interaction.author} | {interaction.author.id}')
        embed.set_footer(text=interaction.guild.name)

        await bug_report_channel.send(embed=embed)
        await interaction.send(embed=disnake.Embed(
            title='<:greencheck:1006659369519304774> | Спасибо! Ваша заявка будет расмотренна администрацией!',
            color=0x8cc63f),
            ephemeral=True)


class Modal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        name='bug',
        description='Нашел баг? Сообщи скорее разработчику!!',
        options=[]
    )
    async def bug(self, inter: disnake.ApplicationCommandInteraction):
        """
        Вызвать модальное окно
        """
        await inter.response.send_modal(modal=ModalWindow(self.bot))


def setup(bot):
    bot.add_cog(Modal(bot))
