import disnake
from disnake.ext import commands


class Context(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.user_command(name='Аватар')
    async def avatar(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User):
        embed = disnake.Embed(color=0x8cc63f)
        embed.set_image(url=user.display_avatar.url)
        embed.set_footer(text=f'Аватар пользователя {user.name}', icon_url=self.bot.user.avatar.url)
        await inter.send(embed=embed)

    @commands.message_command(name='Перевернуть')
    async def reverse(self, inter: disnake.ApplicationCommandInteraction, message: disnake.Message):
        await inter.send(message.content[::-1])

    @commands.user_command(name='Дата регистрации')
    async def registration(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User):
        await inter.send(f'Пользователь **{user.name}** был зарегестрирован <t:{int(user.created_at.timestamp())}>')

    '''@commands.user_command(name='Kick')
    async def _kick_(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        await member.kick(reason='kick')
        await inter.send(f'{member.mention} был кикнут')

    @commands.user_command(name='Ban')
    async def _ban_(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        await member.ban(reason='ban')
        await inter.send(f'{member.mention} был забанен')
   
    @commands.user_command(name='Unmute')
    async def _unmute_(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        await inter.guild.timeout(user=member, duration=None, reason='unmute')
        await inter.send(f'{member.mention} был размучен')

    @commands.user_command(name='Mute')
    async def _mute_(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member):
        await inter.guild.timeout(user=member, duration=999999, reason='mute')
        await inter.send(f'{member.mention} был замучен')'''


def setup(bot):
    bot.add_cog(Context(bot))
