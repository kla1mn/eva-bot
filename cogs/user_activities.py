import datetime

import disnake
from disnake import Member, Role, Option, OptionType, Embed, Message, RawReactionActionEvent
from disnake.ext import commands

# <:greencheck:1006659369519304774>
# <:redcross:1006554004320428052>

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
             'дура', 'хрень', 'хер', 'нахер']


class UserActivities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.slash_command(
        name='delete_role',
        description='Удалить роль',
        options=[
            Option(
                name='role',
                description='Роль, которую требуется выдать',
                type=OptionType.role,
                required=True
            )
        ]
    )
    async def delete_role(self, inter, role: Role):
        name_role = role.name
        await role.delete()
        embed = Embed(
            title='<:greencheck:1006659369519304774> | delete role',
            description=f'Роль **{name_role}** была удалена модератором {inter.author.mention}',
            color=0x8cc63f
        )
        await inter.send(embed=embed)

    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.slash_command(
        name='add_role',
        description='Добавить участнику роль',
        options=[
            Option(
                name='role',
                description='Роль, которую требуется выдать',
                type=OptionType.role,
                required=True
            ),
            Option(
                name='member',
                description='Участник, которому будет выдана роль',
                type=OptionType.user,
                required=False
            )
        ]
    )
    async def add_role(self, inter, role: Role, member: Member = None):
        if not member:
            member = inter.author

        if role in member.roles:
            embed = Embed(
                title='<:redcross:1006554004320428052> | add role',
                description='Данная роль уже на пользователе',
                color=disnake.Color.red())

            # embed.set_footer(text=inter.author)
            await inter.send(embed=embed)
        else:
            await member.add_roles(role, reason=f'Command used by {inter.author}')

            embed = Embed(
                title='<:greencheck:1006659369519304774> | add role',
                description=f'Роль {role.mention} была выдана пользователю {member.mention}',
                color=0x8cc63f)

            # embed.set_footer(text=inter.author)
            await inter.send(embed=embed)

    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.slash_command(
        name='remove_role',
        description='Убрать роль участника',
        options=[
            Option(
                name='role',
                description='Роль, которую требуется убрать',
                type=OptionType.role,
                required=True
            ),
            Option(
                name='member',
                description='Участник, чья роль будет убрана',
                type=OptionType.user,
                required=False
            )
        ]
    )
    async def remove_role(self, inter, role: Role, member: Member = None):
        if not member:
            member = inter.author

        if role not in member.roles:
            embed = Embed(
                title='<:redcross:1006554004320428052> | remove role',
                description='Данная роль, итак, не на пользователе',
                color=disnake.Color.red())

            # embed.set_footer(text=inter.author)
            await inter.send(embed=embed)
        else:
            await member.remove_roles(role, reason=f'Command used by {inter.author}')

            embed = Embed(
                title='<:greencheck:1006659369519304774> | remove role',
                description=f'Роль {role.mention} была снята с пользователя {member.mention}',
                color=0x8cc63f)

            # embed.set_footer(text=inter.author)
            await inter.send(embed=embed)

    @commands.has_permissions(manage_nicknames=True)
    @commands.has_permissions(manage_nicknames=True)
    @commands.slash_command(
        name='edit_nickname',
        description='Изменяет НИК пользователя',
        options=[
            Option(
                name='new_nick',
                description='Новый НИК',
                type=OptionType.string,
                required=True
            ),
            Option(
                name='member',
                description='Участник, чей НИК будет изменен',
                type=OptionType.user,
                required=True
            )
        ]
    )
    async def edit_nick(self, inter, new_nick: str, member: Member = None):
        if not member:
            member = inter.author

        await member.edit(nick=new_nick)

        embed = Embed(
            title='<:greencheck:1006659369519304774> | edit nick',
            description=f'Новый никнейм - "**{new_nick}**"',
            color=disnake.Color.green())

        await inter.send(embed=embed)

    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.slash_command(
        name='colorful_roles',
        description='Наполни свою жизнь красками!',
        options=[]
    )
    async def colorful_roles(self, inter):
        if '🧮-цветные-роли' in str(inter.guild.channels) or 'цветные-роли' in str(inter.guild.channels):
            await inter.send('У Вас уже есть такой канал на этом сервере!')
            return

        overwrites = {
            inter.guild.default_role: disnake.PermissionOverwrite(send_messages=False)
        }

        await inter.guild.create_text_channel(name='🧮-Цветные роли', position=0, overwrites=overwrites)
        embed = Embed(
            title='<:greencheck:1006659369519304774> | colorful roles',
            description='Вы создали канал для выбора цветных ролей!'
                        '\n⬅ | Ищите его вверху списка канала ',
            color=0x8cc63f
        )
        await inter.send(embed=embed)

        for channel in inter.guild.channels:
            if channel.name == '🧮-Цветные роли':
                channel = self.bot.get_channel(int(channel.id))

        # red
        await inter.guild.create_role(name='Красный', color=0xFF0000)  # <:krasni:1015975810068389888>
        await inter.guild.create_role(name='Темно-красный', color=0x8B0000)  # <:temnokrasni:1015975816477294712>
        await inter.guild.create_role(name='Малиновый', color=0xDC143C)  # <:malinovi:1015975812731764757>
        await inter.guild.create_role(name='Светло-коралловый', color=0xF08080)  # <:svetlokoralovi:1015975814908608542>
        await inter.guild.create_role(name='Лососевый', color=0xFFA07A)  # <:lososevi:1015975811553177620>
        await inter.guild.create_role(name='Индийский красный', color=0xCD5C5C)  # <:indiskikrasni:1015975808722030612>

        red_embed = Embed(
            title='Красные цвета',
            description=f'{(disnake.utils.get(inter.guild.roles, name="Красный")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Темно-красный")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Малиновый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Светло-коралловый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Лососевый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Индийский красный")).mention}',
            color=0xff0000)

        emb1 = await channel.send(embed=red_embed)
        await emb1.add_reaction(emoji='<:krasni:1015975810068389888>')
        await emb1.add_reaction(emoji='<:temnokrasni:1015975816477294712>')
        await emb1.add_reaction(emoji='<:malinovi:1015975812731764757>')
        await emb1.add_reaction(emoji='<:svetlokoralovi:1015975814908608542>')
        await emb1.add_reaction(emoji='<:lososevi:1015975811553177620>')
        await emb1.add_reaction(emoji='<:indiskikrasni:1015975808722030612>')

        # orange
        await inter.guild.create_role(name='Оранжевый', color=0xFFA500)  # <:orangevi:1015976174448554075>
        await inter.guild.create_role(name='Темно-оранжевый', color=0xFF8C00)  # <:temnoorangevi:1015976175761371158>
        await inter.guild.create_role(name='Красно-оранжевый', color=0xFF4500)  # <:krasnoorangevi:1015976171546083339>
        await inter.guild.create_role(name='Томатный', color=0xFF6347)  # <:tomatni:1015976177434898432>
        await inter.guild.create_role(name='Коралловый', color=0xFF7F50)  # <:koralovi:1015976169692201080>
        await inter.guild.create_role(name='Охра', color=0xD2691E)  # <:ohra:1015976173144117318>

        orange_embed = Embed(
            title='Оранжевые цвета',
            description=f'{(disnake.utils.get(inter.guild.roles, name="Оранжевый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Темно-оранжевый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Красно-оранжевый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Томатный")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Коралловый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Охра")).mention}',
            color=0xffa500)

        emb2 = await channel.send(embed=orange_embed)
        await emb2.add_reaction(emoji='<:orangevi:1015976174448554075>')
        await emb2.add_reaction(emoji='<:temnoorangevi:1015976175761371158>')
        await emb2.add_reaction(emoji='<:krasnoorangevi:1015976171546083339>')
        await emb2.add_reaction(emoji='<:tomatni:1015976177434898432>')
        await emb2.add_reaction(emoji='<:koralovi:1015976169692201080>')
        await emb2.add_reaction(emoji='<:ohra:1015976173144117318>')

        # yellow
        await inter.guild.create_role(name='Желтый', color=0xFFFF00)  # <:zhelti:1015976494826266674>
        await inter.guild.create_role(name='Золотой', color=0xFFD700)  # <:zolotoy:1015976496206192702>
        await inter.guild.create_role(name='Светло-желтый', color=0xFFFFE0)  # <:svetlozhelti:1015976491156262972>
        await inter.guild.create_role(name='Бежевый', color=0xFFE4B5)  # <:bezhevi:1015976487427526751>
        await inter.guild.create_role(name='Темное золото', color=0xDAA520)  # <:temnoezoloto:1015976492603289652>
        await inter.guild.create_role(name='Лимонный крем', color=0xFFFACD)  # <:limonnikrem:1015976489482715197>

        yellow_embed = Embed(
            title='Желтые цвета',
            description=f'{(disnake.utils.get(inter.guild.roles, name="Желтый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Золотой")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Светло-желтый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Бежевый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Темное золото")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Лимонный крем")).mention}',
            color=0xffff00)

        emb3 = await channel.send(embed=yellow_embed)
        await emb3.add_reaction(emoji='<:zhelti:1015976494826266674>')
        await emb3.add_reaction(emoji='<:zolotoy:1015976496206192702>')
        await emb3.add_reaction(emoji='<:svetlozhelti:1015976491156262972>')
        await emb3.add_reaction(emoji='<:bezhevi:1015976487427526751>')
        await emb3.add_reaction(emoji='<:temnoezoloto:1015976492603289652>')
        await emb3.add_reaction(emoji='<:limonnikrem:1015976489482715197>')

        # green
        await inter.guild.create_role(name='Зеленый', color=0x008000)  # <:zeleni:1015976808165941289>
        await inter.guild.create_role(name='Весенний зеленый', color=0x00FF7F)  # <:vesennizeleni:1015976806618247219>
        await inter.guild.create_role(name='Светло-зеленый', color=0x90EE90)  # <:svetlozeleni:1015976803246014474>
        await inter.guild.create_role(name='Оливковый', color=0x6B8E23)  # <:olivkovi:1015976801144684616>
        await inter.guild.create_role(name='Темно-зеленый', color=0x006400)  # <:temnozeleni:1015976804865032252>
        await inter.guild.create_role(name='Морской зеленый', color=0x2E8B57)  # <:morskoyzeleni:1015976799152386118>

        green_embed = Embed(
            title='Зеленые цвета',
            description=f'{(disnake.utils.get(inter.guild.roles, name="Зеленый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Весенний зеленый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Светло-зеленый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Оливковый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Темно-зеленый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Морской зеленый")).mention}',
            color=0x008000
        )
        emb4 = await channel.send(embed=green_embed)
        await emb4.add_reaction(emoji='<:zeleni:1015976808165941289>')
        await emb4.add_reaction(emoji='<:vesennizeleni:1015976806618247219>')
        await emb4.add_reaction(emoji='<:svetlozeleni:1015976803246014474>')
        await emb4.add_reaction(emoji='<:olivkovi:1015976801144684616>')
        await emb4.add_reaction(emoji='<:temnozeleni:1015976804865032252>')
        await emb4.add_reaction(emoji='<:morskoyzeleni:1015976799152386118>')

        # blue
        await inter.guild.create_role(name='Синяя сталь', color=0x4682B4)  # <:sinyastal:1015977212148719666>
        await inter.guild.create_role(name='Темная лазурь', color=0x00CED1)  # <:temnayalazur:1015977214031958046>
        await inter.guild.create_role(name='Бирюзовый', color=0x00FFFF)  # <:biruzovi:1015977206121504878>
        await inter.guild.create_role(name='Темное небо', color=0x00BFFF)  # <:temnoenebo:1015977215793569853>
        await inter.guild.create_role(name='Синий', color=0x0000FF)  # <:sini:1015977210252894228>
        await inter.guild.create_role(name='Морской синий', color=0x000080)  # <:morskoisini:1015977208382230658>

        blue_embed = Embed(
            title='Синие цвета',
            description=f'{(disnake.utils.get(inter.guild.roles, name="Синяя сталь")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Темная лазурь")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Бирюзовый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Темное небо")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Синий")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Морской синий")).mention}',
            color=0x0000FF)

        emb5 = await channel.send(embed=blue_embed)
        await emb5.add_reaction(emoji='<:sinyastal:1015977212148719666>')
        await emb5.add_reaction(emoji='<:temnayalazur:1015977214031958046>')
        await emb5.add_reaction(emoji='<:biruzovi:1015977206121504878>')
        await emb5.add_reaction(emoji='<:temnoenebo:1015977215793569853>')
        await emb5.add_reaction(emoji='<:sini:1015977210252894228>')
        await emb5.add_reaction(emoji='<:morskoisini:1015977208382230658>')

        # purple
        await inter.guild.create_role(name='Голубая фиалка', color=0x8A2BE2)  # <:golubayafialka:1015977577694896308>
        await inter.guild.create_role(name='Фиолетовый', color=0x800080)  # <:fioletovi:1015977576130433084>
        await inter.guild.create_role(name='Индиго', color=0x4B0082)  # <:indigo:1015977579347447838>
        await inter.guild.create_role(name='Сине-фиолетовый', color=0x6A5ACD)  # <:sinefioletovi:1015977580995817492>
        await inter.guild.create_role(name='Темный сине-фиолетовый',
                                      color=0x483D8B)  # <:temnisinefioletovi:1015977582514159696>
        await inter.guild.create_role(name='Темно-пурпурный', color=0x8B008B)  # <:temnopurpurni:1015977584137347083>

        purple_embed = Embed(
            title='Фиолетовые цвета',
            description=f'{(disnake.utils.get(inter.guild.roles, name="Голубая фиалка")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Фиолетовый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Индиго")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Сине-фиолетовый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Темный сине-фиолетовый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Темно-пурпурный")).mention}',
            color=0x800080)

        emb6 = await channel.send(embed=purple_embed)
        await emb6.add_reaction(emoji='<:golubayafialka:1015977577694896308>')
        await emb6.add_reaction(emoji='<:fioletovi:1015977576130433084>')
        await emb6.add_reaction(emoji='<:indigo:1015977579347447838>')
        await emb6.add_reaction(emoji='<:sinefioletovi:1015977580995817492>')
        await emb6.add_reaction(emoji='<:temnisinefioletovi:1015977582514159696>')
        await emb6.add_reaction(emoji='<:temnopurpurni:1015977584137347083>')

        # special
        await inter.guild.create_role(name='Специальный зеленый', color=0x8cc63f)  # <:specialgreen:1015977624188756119>
        await inter.guild.create_role(name='Черный', color=0x0e0c0c)  # <:black:1015977620548091904>
        await inter.guild.create_role(name='Белый', color=0xffffff)  # <:white:1015977625723871283>
        await inter.guild.create_role(name='Discord', color=0x2F3136)  # <:discord:1015977621936422937>

        special_embed = Embed(
            title='Особые цвета',
            description=f'{(disnake.utils.get(inter.guild.roles, name="Специальный зеленый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Черный")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Белый")).mention}'
                        f'\n{(disnake.utils.get(inter.guild.roles, name="Discord")).mention}',
            color=0x8cc63f)

        emb7 = await channel.send(embed=special_embed)
        await emb7.add_reaction(emoji='<:specialgreen:1015977624188756119>')
        await emb7.add_reaction(emoji='<:black:1015977620548091904>')
        await emb7.add_reaction(emoji='<:white:1015977625723871283>')
        await emb7.add_reaction(emoji='<:discord:1015977621936422937>')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        print(f'Событие: {payload.event_type}')
        print(f'Сервер: {payload.guild_id}')
        print(f'Пользователь: {payload.user_id}')
        print(f'Реакция: {payload.emoji}')
        print(f'Сообщение: {payload.message_id}')
        print(f'Время: {str(datetime.datetime.now())[:-7]}')
        print('--------------------------------------')

        guild = disnake.utils.find(lambda g: g.id == payload.guild_id, self.bot.guilds)
        if payload.emoji.id == 1015975810068389888:
            role = disnake.utils.get(guild.roles, name="Красный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015975816477294712:
            role = disnake.utils.get(payload.member.guild.roles, name="Темно-красный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015975812731764757:
            role = disnake.utils.get(payload.member.guild.roles, name="Малиновый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015975814908608542:
            role = disnake.utils.get(payload.member.guild.roles, name="Светло-коралловый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015975811553177620:
            role = disnake.utils.get(payload.member.guild.roles, name="Лососевый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015975808722030612:
            role = disnake.utils.get(payload.member.guild.roles, name="Индийский красный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)

            # orange
        if payload.emoji.id == 1015976174448554075:
            role = disnake.utils.get(payload.member.guild.roles, name="Оранжевый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976175761371158:
            role = disnake.utils.get(payload.member.guild.roles, name="Темно-оранжевый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976171546083339:
            role = disnake.utils.get(payload.member.guild.roles, name="Красно-оранжевый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976177434898432:
            role = disnake.utils.get(payload.member.guild.roles, name="Томатный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976169692201080:
            role = disnake.utils.get(payload.member.guild.roles, name="Коралловый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976173144117318:
            role = disnake.utils.get(payload.member.guild.roles, name="Охра")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)

            # yellow
        if payload.emoji.id == 1015976494826266674:
            role = disnake.utils.get(payload.member.guild.roles, name="Желтый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976496206192702:
            role = disnake.utils.get(payload.member.guild.roles, name="Золотой")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976491156262972:
            role = disnake.utils.get(payload.member.guild.roles, name="Светло-желтый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976487427526751:
            role = disnake.utils.get(payload.member.guild.roles, name="Бежевый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976492603289652:
            role = disnake.utils.get(payload.member.guild.roles, name="Темное золото")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976489482715197:
            role = disnake.utils.get(payload.member.guild.roles, name="Лимонный крем")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)

            # green
        if payload.emoji.id == 1015976808165941289:
            role = disnake.utils.get(payload.member.guild.roles, name="Зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976806618247219:
            role = disnake.utils.get(payload.member.guild.roles, name="Весенний зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976803246014474:
            role = disnake.utils.get(payload.member.guild.roles, name="Светло-зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976801144684616:
            role = disnake.utils.get(payload.member.guild.roles, name="Оливковый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976804865032252:
            role = disnake.utils.get(payload.member.guild.roles, name="Темно-зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015976799152386118:
            role = disnake.utils.get(payload.member.guild.roles, name="Морской зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)

            # blue
        if payload.emoji.id == 1015977212148719666:
            role = disnake.utils.get(payload.member.guild.roles, name="Синяя сталь")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977214031958046:
            role = disnake.utils.get(payload.member.guild.roles, name="Темная лазурь")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977206121504878:
            role = disnake.utils.get(payload.member.guild.roles, name="Бирюзовый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977215793569853:
            role = disnake.utils.get(payload.member.guild.roles, name="Темное небо")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977210252894228:
            role = disnake.utils.get(payload.member.guild.roles, name="Синий")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977208382230658:
            role = disnake.utils.get(payload.member.guild.roles, name="Морской синий")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)

            # purple
        if payload.emoji.id == 1015977577694896308:
            role = disnake.utils.get(payload.member.guild.roles, name="Голубая фиалка")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977576130433084:
            role = disnake.utils.get(payload.member.guild.roles, name="Фиолетовый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977579347447838:
            role = disnake.utils.get(payload.member.guild.roles, name="Индиго")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977580995817492:
            role = disnake.utils.get(payload.member.guild.roles, name="Сине-фиолетовый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977582514159696:
            role = disnake.utils.get(payload.member.guild.roles, name="Темный сине-фиолетовый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977584137347083:
            role = disnake.utils.get(payload.member.guild.roles, name="Темно-пурпурный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)

            # special
        if payload.emoji.id == 1015977624188756119:
            role = disnake.utils.get(payload.member.guild.roles, name="Специальный зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977620548091904:
            role = disnake.utils.get(payload.member.guild.roles, name="Черный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977625723871283:
            role = disnake.utils.get(payload.member.guild.roles, name="Белый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        if payload.emoji.id == 1015977621936422937:
            role = disnake.utils.get(payload.member.guild.roles, name="Discord")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: RawReactionActionEvent):
        print(f'Событие: {payload.event_type}')
        print(f'Сервер: {payload.guild_id}')
        print(f'Пользователь: {payload.user_id}')
        print(f'Реакция: {payload.emoji}')
        print(f'Сообщение: {payload.message_id}')
        print(f'Время: {str(datetime.datetime.now())[:-7]}')
        print('--------------------------------------')

        guild = disnake.utils.find(lambda g: g.id == payload.guild_id, self.bot.guilds)
        if payload.emoji.id == 1015975810068389888:
            role = disnake.utils.get(guild.roles, name="Красный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015975816477294712:
            role = disnake.utils.get(guild.roles, name="Темно-красный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015975812731764757:
            role = disnake.utils.get(guild.roles, name="Малиновый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015975814908608542:
            role = disnake.utils.get(guild.roles, name="Светло-коралловый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015975811553177620:
            role = disnake.utils.get(guild.roles, name="Лососевый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015975808722030612:
            role = disnake.utils.get(guild.roles, name="Индийский красный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)

            # orange
        if payload.emoji.id == 1015976174448554075:
            role = disnake.utils.get(guild.roles, name="Оранжевый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976175761371158:
            role = disnake.utils.get(guild.roles, name="Темно-оранжевый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976171546083339:
            role = disnake.utils.get(guild.roles, name="Красно-оранжевый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976177434898432:
            role = disnake.utils.get(guild.roles, name="Томатный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976169692201080:
            role = disnake.utils.get(guild.roles, name="Коралловый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976173144117318:
            role = disnake.utils.get(guild.roles, name="Охра")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)

            # yellow
        if payload.emoji.id == 1015976494826266674:
            role = disnake.utils.get(guild.roles, name="Желтый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976496206192702:
            role = disnake.utils.get(guild.roles, name="Золотой")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976491156262972:
            role = disnake.utils.get(guild.roles, name="Светло-желтый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976487427526751:
            role = disnake.utils.get(guild.roles, name="Бежевый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976492603289652:
            role = disnake.utils.get(guild.roles, name="Темное золото")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976489482715197:
            role = disnake.utils.get(guild.roles, name="Лимонный крем")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)

            # green
        if payload.emoji.id == 1015976808165941289:
            role = disnake.utils.get(guild.roles, name="Зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976806618247219:
            role = disnake.utils.get(guild.roles, name="Весенний зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976803246014474:
            role = disnake.utils.get(guild.roles, name="Светло-зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976801144684616:
            role = disnake.utils.get(guild.roles, name="Оливковый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976804865032252:
            role = disnake.utils.get(guild.roles, name="Темно-зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015976799152386118:
            role = disnake.utils.get(guild.roles, name="Морской зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)

            # blue
        if payload.emoji.id == 1015977212148719666:
            role = disnake.utils.get(guild.roles, name="Синяя сталь")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977214031958046:
            role = disnake.utils.get(guild.roles, name="Темная лазурь")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977206121504878:
            role = disnake.utils.get(guild.roles, name="Бирюзовый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977215793569853:
            role = disnake.utils.get(guild.roles, name="Темное небо")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977210252894228:
            role = disnake.utils.get(guild.roles, name="Синий")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977208382230658:
            role = disnake.utils.get(guild.roles, name="Морской синий")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)

            # purple
        if payload.emoji.id == 1015977577694896308:
            role = disnake.utils.get(guild.roles, name="Голубая фиалка")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977576130433084:
            role = disnake.utils.get(guild.roles, name="Фиолетовый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977579347447838:
            role = disnake.utils.get(guild.roles, name="Индиго")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977580995817492:
            role = disnake.utils.get(guild.roles, name="Сине-фиолетовый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977582514159696:
            role = disnake.utils.get(guild.roles, name="Темный сине-фиолетовый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977584137347083:
            role = disnake.utils.get(guild.roles, name="Темно-пурпурный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)

            # special
        if payload.emoji.id == 1015977624188756119:
            role = disnake.utils.get(guild.roles, name="Специальный зеленый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977620548091904:
            role = disnake.utils.get(guild.roles, name="Черный")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977625723871283:
            role = disnake.utils.get(guild.roles, name="Белый")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        if payload.emoji.id == 1015977621936422937:
            role = disnake.utils.get(guild.roles, name="Discord")
            if role is not None:
                member = disnake.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        channel = self.bot.get_channel(1009519458445971608)
        await channel.send(f'Привет {member.mention}! Рада видеть тебя на сервере!')
        print(f'Участник "{member}" вошел на сервер "{member.guild}" время - {str(datetime.datetime.now())[:-7]}')
        print('--------------------------------------')

    @commands.Cog.listener()
    async def on_member_remove(self, member: Member):
        print(f'Участник "{member}" вышел с сервера "{member.guild}" время - {str(datetime.datetime.now())[:-7]}')
        print('--------------------------------------')

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        print(
            f'Сообщение "{message.content}" от пользователя "{message.author}" на сервере "{message.guild}" в канале '
            f'"{message.channel}" время - {str(datetime.datetime.now())[:-7]}')
        print('--------------------------------------')


def setup(bot):
    bot.add_cog(UserActivities(bot))
