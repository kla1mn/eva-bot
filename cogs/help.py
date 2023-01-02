import disnake
import disnake_paginator
from disnake.ext import commands
# 0x2F3136


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['помощь', 'помоги', 'помогите'])
    async def help(self, inter):
        user = await self.bot.fetch_user(712926134794453003)
        main_embed = disnake.Embed(
            title='Команды бота **eva**',
            description='**Помощь**'
                        '\n**/help** - все команды'
                        f'\n"**bot **" - префикс бота (с пробелом)'
                        f'\n`[]` - обязательный аргумент'
                        f'\n`()` - необязательный аргумент'
                        f'\nВсе команды **БУДУТ** иметь non-slash альтернативу'
                        f'\nВсего команд: `62`',
            color=0x8cc63f)
        main_embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar.url)
        main_embed.set_footer(text='kla1mn#1423 © 2022 Все права защищены', icon_url=user.display_avatar.url)

        moder_embed = disnake.Embed(
            title='⚙ | **Модерация** '
                  '\n*команды доступны если ты владеешь соответствующими правами*',
            description='**kick** - кик пользователя [пользователь] (причина)'
                        '\n**ban** - бан пользователя [пользователь] (время) (причина)'
                        '\n**unban** - разбан пользователя [ID пользователя] (причина)'
                        '\n**clear** - очистка определенного количества сообщений в чате [количество]'
                        '\n**mute** - мут пользователя на определенное время [пользователь] [время] (причина)'
                        '\n**unmute** - размут пользователя [пользователь] (причина)'
                        '\n**lock** - закрывает данный текстовый канал для default-role'
                        '\n**unlock** - открывает данный текстовый канал для default-role'
                        '\n**slowmode** - установка медленного режима (для отключения указать "0") [время] (канал)',
            color=0x8cc63f)
        moder_embed.set_footer(text='Здесь могла быть Ваша реклама')

        fun_embed = disnake.Embed(
            title='🎲 | **Развлечения** ',
            description='**echo** - повтор твоего сообщения [сообщение]'
                        '\n**dog** - фотография собаки'
                        '\n**cat** - фоттография кота'
                        '\n**panda** - фотография панды'
                        '\n**raccoon** - фотография енота'
                        '\n**red_panda** - фотография красной панды'
                        '\n**rickroll** - просто рикролл..'
                        '\n**skala** -  Хммм.. Это что, Скала Джонсон?!'
                        '\n**magic_ball** - магический шар поможет сделать правильный выбор [вопрос]'
                        '\n**red_button** - просто кнопка',
            color=0x8cc63f)
        fun_embed.set_footer(text='Здесь тоже могла быть Ваша реклама')

        rp_embed = disnake.Embed(
            title='🎭 | **Role play**',
            description='**hug** - обнять пользователя [пользователь]'
                        '\n**pat** - погладить пользователя [пользователь]'
                        '\n**wink** - подмигнуть пользователю [пользователь]'
                        '\n**kiss** - поцеловать пользователя [пользователь]'
                        '\n**bite** - укусить пользователя [пользователь]'
                        '\n**blush** - засмущаться из-за пользователя [пользователь]'
                        '\n**cringe** - кринжануть из-за пользователя [пользователь]'
                        '\n**cry** - заплакать из-за пользователя [пользователь] [причина]'
                        '\n**dance** - потанцевать [причина]'
                        '\n**lick** - облизать пользователя [пользователь]'
                        '\n**handhold** - взять за ручку пользователя [пользователь] [причина]'
                        '\n**smile** - улыбнуться пользователю [пользователь] [причина]'
                        '\n**wave** - помахать пользователю [пользователь] [причина]'
                        '\n**highfive** - дать пять пользователю [пользователь] [причина]'
                        '\n**happy** - побыть счастливым [причина]'
                        '\n**slap** - дать пощечину пользователю [пользователь] [причина]'
                        '\n**try** - попробовать что-нибудь сделать [значение]',
            color=0x8cc63f)
        rp_embed.set_footer(text='Рекламы много не бывает!!')

        """embed4 = disnake.Embed(
            title='💹 **Экономика:** ',
            description='**start_economic** - начать экономику'
                        '\n**delete_economic** - удалить экономику'
                        '\n**work** - "условно" поработать и получить некоторое количество монеток'
                        '\n**balance** - проверка баланса любого пользователя [пользователь]'
                        '\n**pay** - перевод монеток другому пользователю [пользователь] [сумма]'
                        '\n**coin** - случайный выбор "Орёл | Решка" *(в разработке)*',
            color=0x8cc63f)"""

        users_embed = disnake.Embed(
            title='🗣 | **Управление пользователями**'
                  '\n*доступно администраторам*',
            description='**add_role** - добавление роли пользователю [роль] [пользователь]'
                        '\n**remove_role** - удаление роли пользователя [роль] [пользователь]'
                        '\n**edit_nick** - изменение никнейма пользователя [новый ник] [пользователь]'
                        '\n**colorful_roles** - цветные роли для твоего сервер (использовать один раз)'
                        '\n**delete_role** - удаление роли [роль]',
            color=0x8cc63f)
        users_embed.set_footer(text='Да, здесь тоже могла быть Ваша реклама')

        info_embed = disnake.Embed(
            title='ℹ | **Информация** ',
            description='**user_info** - получение информации о любом пользователе (пользователь)'
                        '\n**guild_info** - получение информации о сервере'
                        '\n**bot_info** - получение информации о боте **eva**'
                        '\n**bans** - информация о банах на данном сервере'
                        '\n**developer** - информация о разработчике бота',
            color=0x8cc63f)
        info_embed.set_footer(text='И даже тут могла быть Ваша реклама')

        channels_embed = disnake.Embed(
            title='👥 | **Каналы** '
                  '\n*доступно администраторам*',
            description='**create_text_channel** - создание нового текстового канала [название]'
                        '\n**create_voice_channel** - создание нового голосового канала [название]'
                        '\n**create_private_channel** - создание секретного текстового канала [название]'
                        '\n**delete_channel** - удаление текстового канала [название]',
            color=0x8cc63f)
        channels_embed.set_footer(text='Оказывается, тут тоже могла быть Ваша реклама')

        maths_embed = disnake.Embed(
            title='🔢 | **Математика** ',
            description='**bin** - перевод десятичного числа в двоичное [число]'
                        '\n**hex** - перевод десятичного числа в шестнадцатеричное [число]'
                        '\n*раздел в разработке*',
            color=0x8cc63f)
        maths_embed.set_footer(text='Это что, свободное место для рекламы??')

        context_embed = disnake.Embed(
            title='🛠 | **Приложения** ',
            description='**Аватар** - бот пришлет аватар любого участника сервера [пкм по пользователю]'
                        '\n**Дата регистрации** - бот пришлет дату регистрации любого участника сервера '
                        '[пкм по пользователю]'
                        '\n**Перевернуть** - бот перевернет любое сообщение [пкм по сообщению]',
            color=0x8cc63f)
        context_embed.set_footer(text='Больше места для рекламы нет!')

        other_embed = disnake.Embed(
            title='🔧 | **Другое** ',
            description='**password** - генерация сложного пароля [длина пароля (до 67 символов)]'
                        '\n**timer** - пинг пользователя через определенное время [время] (действие)'
                        '\n**weather** - погода в данный момент в любой точке мира [город] [страна]'
                        '\n**news** - последние новости в мире *(фукнция в разработке)*'
                        '\n**bug** - сообщи разработчикам об ошибках!'
                        '\n**prefix** - смена старого префикса на новый [новый префикс]',
            color=0x8cc63f)
        other_embed.set_footer(text='Ладно шучу, здесь есть место для рекламы)')

        paginator = disnake_paginator.ButtonPaginator(

            segments=[main_embed, moder_embed, info_embed, users_embed, channels_embed, fun_embed, rp_embed,
                      context_embed, maths_embed, other_embed],
            color=0x8cc63f,
            timeout=600,
            button_style=disnake.ButtonStyle.blurple,
            invalid_user_function='Извини, но ты не можешь пролистать этот список( Его вызвал не ты!')
        await paginator.start(inter)

        """await inter.send(embed=embed1, components=[
            Select(
                placeholder="Выберите Ваш сервер",
                options=[
                    SelectOption(label='Модерация', value=f'{embed211}', emoji='⚙',
                                 description='Полная информация о командах модерации'),
                    SelectOption(label='Развлечения', value=f'{embed3}', emoji='⚙',
                                 description='Полная информация о командах модерации'),
                    SelectOption(label='Экономика', value=f'{embed4}', emoji='⚙',
                                 description='Полная информация о командах модерации'),
                    SelectOption(label='Музыка', value='1235467', emoji='⚙',
                                 description='Полная информация о командах модерации'),
                    SelectOption(label='Управление пользователями', value=f'{embed5}', emoji='⚙',
                                 description='Полная информация о командах модерации'),
                    SelectOption(label='Информация', value=f'{embed6}', emoji='⚙',
                                 description='Полная информация о командах модерации'),
                    SelectOption(label='Управление каналми', value=f'{embed7}', emoji='⚙',
                                 description='Полная информация о командах модерации'),
                    SelectOption(label='Математика', value=f'{embed8}', emoji='⚙',
                                 description='Полная информация о командах модерации'),
                    SelectOption(label='Приложения', value=f'{embed9}', emoji='⚙',
                                 description='Полная информация о командах модерации'),
                    SelectOption(label='Другое', value=f'{embed10}', emoji='⚙',
                                 description='Полная информация о командах модерации')

                ]
            )
        ])"""

        """interaction = await self.bot.wait_for("select_option")
        if interaction['label'] == 'Модерация':
            embed2 = disnake.Embed(
                title='📊 **Модерация:** '
                      '\n*доступно модераторам*',
                description='**kick** - кик пользователя [пользователь] [причина]'
                            '\n**ban** - бан пользователя [пользователь] [время] [причина]'
                            '\n**clear** - очистка определенного количества сообщений в чате [количество]'
                            '\n**mute** - заглушает пользователя на определенное время [пользователь] [время] [причина]',
                color=0x8cc63f
            )
            await inter.send(embed=embed2)"""

        # embed10.set_author(name=self.bot.user, icon_url=self.bot.user.avatar.url)
        # embed10.set_footer(text='kla1mn#1423 © 2022 Все права защищены')

        # embed.set_footer(text=inter.author)
        # embed.set_author(name=self.bot.user, icon_url=self.bot.user.avatar.url)
        # embed.set_footer(text='kla1mn#1423 © 2022 Все права защищены')


def setup(bot):
    bot.add_cog(Help(bot))
