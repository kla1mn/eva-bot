import asyncio
from asyncio import sleep
from datetime import timedelta, datetime
from random import choice

import disnake
from disnake import Member, Embed
from disnake.ext import commands

from tools.getseconds import getseconds


# <:checkmark:905943731067305996>
# <:deletesign:905943741775368272>

# <:tick:1006284280240025671>
# <:redcross:1006285060888076289>

# <:greencheck:1006659369519304774> #
# <:redcross:1006554004320428052> #


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @commands.command(aliases=['кик'])
    async def kick(self, inter, member: Member, *, reason: str):

        author_kick = ['Ты пытаешься кикнуть самого себя!',
                       'Ты что творишь?! Себя нельзя кикать!',
                       'Даже не думай об этом! Себя нельзя кикать!',
                       'Ещё что захотел, нельзя себя кикать!',
                       'Давай ты не будешь меня дергать по пустякам, себя нельзя кикать!',
                       'Придумай что-нибудь получше, себя нельзя кикать!',
                       'Фантазии не хватает? Себя нельзя кикать!',
                       '👉🆔<:redcross:1006554004320428052>',
                       'Пошутил и хватит, себя нельзя кикать!',
                       'Очень смешно, себя нельзя кикать!',
                       'Dino "смееясь во весь голос": себя нельзя кикать!',
                       'Выглядит так, как будто ты хочешь кикнуть себя..']

        after_kick = [f'Участник **{member.mention}** был кикнут по причине **{reason}**',
                      f'Участник **{member.mention}** отлетел из-за **{reason}**',
                      f'Участник **{member.mention}** покинул наш чудный сервер по причине **{reason}**',
                      f'Участник **{member.mention}** пошел кушать (на самом деле кик за **{reason}**)',
                      f'Участник **{member.mention}** мне не понравился по причине **{reason}**',
                      f'Участник **{member.mention}** не пойдет играть в майнкарфт потому, что **{reason}**',
                      f'Участник **{member.mention}** собрал рюкзак и отправился в путешествие потому, '
                      f'что **{reason}**']

        angry = ['https://cdn.discordapp.com/attachments/1009866989105324155/1009867532733268068/IMG_8535.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867571065012315/IMG_8537.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867341116477479/IMG_8516.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867337572302949/IMG_8510.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867283230887987/IMG_8506.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867281809031289/IMG_8502.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867215253811230/IMG_8491.PNG']

        title_kick = ['Вот тебя и кикнули...', 'Тебя кикнули(', 'Обидно ведь, правда?',
                      'Да уж, вот и твоя очередь настала', 'Кто-то отлетел..', 'За что тебя так?',
                      'Возможно, ты еще сможешь вернуться к нам..', 'Ты был кикнут(']

        desc_kick = ['Не делай так больше, пожалуйста)', 'Давай в следующий раз без этого..',
                     'В следующий раз будь осторожнее..', 'Давай как-нибудь осторожнее(', 'А ты мне нравился((',
                     'Советую быть осторожнее..']

        if member.id == inter.author.id:
            embed = Embed(
                title='<:redcross:1006554004320428052> | kick',
                description=choice(author_kick),
                color=0xde001e)

            await inter.send(embed=embed)
            await inter.send(
                'https://cdn.discordapp.com/attachments/1009866989105324155/1009867531672109186/IMG_8532.PNG')
            return

        await member.kick(reason=reason)

        embed = Embed(
            title=f'<:greencheck:1006659369519304774>  | kick',
            description=choice(after_kick),
            color=0x8cc63f)
        embed.set_thumbnail(url=member.avatar.url)

        embed2 = Embed(
            title=choice(title_kick),
            description=choice(desc_kick),
            color=0x8cc63f,
            timestamp=datetime.now()
        )
        embed2.set_author(name=f'Кик с сервера "{inter.guild.name}"', icon_url=self.bot.user.avatar.url)
        embed2.add_field('Причина', reason.capitalize())
        embed2.set_footer(text=f'Администратор: {inter.author}', icon_url=inter.author.avatar.url)

        if inter.guild.icon:
            embed2.set_thumbnail(url=inter.guild.icon.url)

        await member.send(embed=embed2)
        await inter.send(embed=embed)
        await inter.send(choice(angry))

    @commands.has_permissions(ban_members=True, create_instant_invite=True)
    @commands.bot_has_permissions(ban_members=True, create_instant_invite=True)
    @commands.command(aliases=['разбан', 'разбань', 'разбанить'])
    async def unban(self, inter, id: int, *, reason: str = 'Разбан'):

        id = int(id)
        user = await self.bot.fetch_user(id)
        bans = await inter.guild.bans(limit=5000).flatten()

        author_unban = ['Ты пытаешься разбанить самого себя!',
                        'Ты что творишь?! Себя нельзя разбанить!',
                        'Даже не думай об этом! Себя нельзя разбанить!',
                        'Ещё что захотел, нельзя себя разбанить!',
                        'Давай ты не будешь меня дергать по пустякам, себя нельзя разбанить!',
                        'Придумай что-нибудь получше, себя нельзя разбанить!',
                        'Фантазии не хватает? Себя нельзя разбанить!',
                        '👉🆔<:redcross:1006554004320428052>',
                        'Пошутил и хватит, себя нельзя разбанить!',
                        'Очень смешно, себя нельзя разбанить!',
                        'Dino "смееясь во весь голос": себя нельзя разбанить!',
                        'Выглядит так, как будто ты хочешь разбанить себя..',
                        'Ты и так незабанен!']

        after_unban = [f'**{inter.author}** разбанил пользователя **{user}** по причине: **{reason}**',
                       f'**{inter.author}** подарил пользователю **{user}** новую жизнь потому, что **{reason}**',
                       f'**{inter.author}** на самом деле добрый! Только что, он разбанил пользователя **{user}** '
                       f'по причине: **{reason}**',
                       f'Повезло! Повезло! Пользователь **{user}** получил амнистию от **{inter.author} '
                       f'**по причине: **{reason}**',
                       f'**{inter.author}** подарил ещё один шанс пользователю **{user}** по причине: **{reason}**',
                       f'Пользователь **{user}** стал вести себя лучше потому, что **{reason}** и получил разбан от '
                       f'**{inter.author}**']

        welcome = ['https://cdn.discordapp.com/attachments/1009866989105324155/1009867407801729157/IMG_8522.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867405658427492/IMG_8517.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867340726419466/IMG_8515.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867337115111516/IMG_8509.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867336712466453/IMG_8508.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867216306569237/IMG_8493.PNG']

        title_unban = ['Ура! Тебя разбанили!', 'Тебя разбанили!', 'Круто, правда?',
                       'Я думала этого не случится.. ТЕБЯ РАЗБАНИЛИ!', 'Кого-то наконец-то разбанили)',
                       'ОГО! РАЗБАН!', 'Ты смогу вернуться к нам! Поздравляю!', 'Ты был разбанен!']

        desc_unban = ['Не делай так больше, пожалуйста)', 'Давай в следующий раз без этого..',
                      'В следующий раз будь осторожнее..', 'Давай как-нибудь осторожнее(',
                      'Советую быть осторожнее..']

        if id == inter.author.id:
            embed = Embed(
                title='<:redcross:1006554004320428052> | unban',
                description=choice(author_unban),
                color=0xde001e)
            await inter.send(embed=embed)
            await inter.send(
                'https://cdn.discordapp.com/attachments/1009866989105324155/1009867531672109186/IMG_8532.PNG')
            return

        if str(id) not in str(bans):
            embed = Embed(
                title='<:redcross:1006554004320428052> | unban',
                description=f'Пользователь **{user.name}**, итак, не забанен на сервере **{inter.guild.name}**',
                color=0xde001e)
            await inter.send(embed=embed)
            await inter.send(
                'https://cdn.discordapp.com/attachments/1009866989105324155/1009867532016029767/IMG_8533.PNG')
            return

        embed = Embed(
            title='<:greencheck:1006659369519304774> | unban',
            description=choice(after_unban),
            color=0x8cc63f)

        embed2 = Embed(
            title=choice(title_unban),
            description=choice(desc_unban),
            color=0x8cc63f,
            timestamp=datetime.now()
        )
        embed2.set_author(name=f'Разбан на сервере "{inter.guild.name}"', icon_url=self.bot.user.avatar.url)
        embed2.add_field('Причина', reason.capitalize())
        invite = await inter.channel.create_invite(max_uses=1, reason='Разбан')
        embed2.add_field('Ссылка на сервер', invite)
        embed2.set_footer(text=f'Администратор: {inter.author}', icon_url=inter.author.avatar.url)

        if inter.guild.icon:
            embed2.set_thumbnail(url=inter.guild.icon.url)

        await inter.guild.unban(user, reason=reason)
        await inter.send(embed=embed)
        await user.send(embed=embed2)
        await inter.send(choice(welcome))

    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.command(aliases=['бан', 'бань', 'забанить', 'забань'])
    async def ban(self, inter, member: Member, time: str, *, reason: str = None):

        wrong_time = ['Неверное время!',
                      'Неправильное время',
                      'Такое невозможно',
                      'Введи правильное время',
                      'Я знаю точно невозможное возможно... (Неверное время)']

        after_ban_2 = [
            f'Пользователь **{member.mention}** был забанен по причине **{reason}** на время - **{time}**',
            f'Пользователь **{member.mention}** не сможет **{time}** находиться на нашем сервере '
            f'по причине **{reason}**',
            f'Пользователь **{member.mention}** остается без сладкого на **{time}** по причине **{reason}**',
            f'Пользователь **{member.mention}** не сможет играть в майнкрафт **{time}** по причине **{reason}**']

        unban = [f'Пользователь **{member.mention}** наконец-то был разбанен',
                 f'Пользователь **{member.mention}** может вернуться к нам на сервер',
                 f'Пользователь **{member.mention}** получает билет в новую жизнь',
                 f'Пользователь **{member.mention}** покушал и теперь готов к новым приключениям',
                 f'Пользователь **{member.mention}** выспался и теперь имеет светлый и ясный ум']

        author_ban = ['Ты пытаешься забанить самого себя!',
                      'Ты что творишь?! Себя нельзя банить!',
                      'Даже не думай об этом! Себя нельзя банить!',
                      'Ещё что захотел, нельзя себя банить!',
                      'Давай ты не будешь меня дергать по пустякам, себя нельзя банить!',
                      'Придумай что-нибудь получше, себя нельзя банить!',
                      'Фантазии не хватает? Себя нельзя банить!',
                      '👉🆔<:deletesign:905943741775368272>',
                      'Пошутил и хватит, себя нельзя банить!',
                      'Очень смешно, себя нельзя банить!',
                      'Dino "смееясь во весь голос": себя нельзя банить!',
                      'Подожди, ты только что пытался себя забанить..?']

        after_ban = [
            f'Пользователь **{member.mention}** был забанен по причине **{reason}** навсегда',
            f'Пользователь **{member.mention}** не сможет больше находиться на нашем сервере '
            f'по причине **{reason}**',
            f'Пользователь **{member.mention}** остается без сладкого по причине **{reason}**',
            f'Пользователь **{member.mention}** не сможет играть в майнкрафт по причине **{reason}**']

        angry = ['https://cdn.discordapp.com/attachments/1009866989105324155/1009867532733268068/IMG_8535.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867571065012315/IMG_8537.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867341116477479/IMG_8516.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867337572302949/IMG_8510.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867283230887987/IMG_8506.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867281809031289/IMG_8502.PNG',
                 'https://cdn.discordapp.com/attachments/1009866989105324155/1009867215253811230/IMG_8491.PNG']

        welcome = ['https://cdn.discordapp.com/attachments/1009866989105324155/1009867407801729157/IMG_8522.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867405658427492/IMG_8517.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867340726419466/IMG_8515.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867337115111516/IMG_8509.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867336712466453/IMG_8508.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867216306569237/IMG_8493.PNG']

        title_ban = ['Вот тебя и кикнули...', 'Тебя кикнули(', 'Обидно ведь, правда?',
                     'Да уж, вот и твоя очередь настала', 'Кто-то отлетел..', 'За что тебя так?',
                     'Возможно, ты еще сможешь вернуться к нам..', 'Ты был кикнут(']

        desc_ban = ['Не делай так больше, пожалуйста)', 'Давай в следующий раз без этого..',
                    'В следующий раз будь осторожнее..', 'Давай как-нибудь осторожнее(', 'А ты мне нравился((',
                    'Советую быть осторожнее..']

        if time:
            if not getseconds(time):
                embed = Embed(
                    title='<:redcross:1006554004320428052> | ban',
                    description=choice(wrong_time),
                    color=0xde001e)

                await inter.send(embed=embed)
                return

            if member.id == inter.author.id:
                embed = Embed(
                    title='<:redcross:1006554004320428052> | ban',
                    description=choice(author_ban),
                    color=0xde001e)

                await inter.send(embed=embed)
                await inter.send(
                    'https://cdn.discordapp.com/attachments/1009866989105324155/1009867531672109186/IMG_8532.PNG')
                return

            await member.ban(reason=reason)

            embed = Embed(
                title=f'<:greencheck:1006659369519304774> | ban',
                description=choice(after_ban_2),
                color=0x8cc63f)
            embed.set_thumbnail(url=member.avatar.url)

            await inter.send(embed=embed)
            await inter.send(choice(angry))

            await asyncio.sleep(getseconds(time))

            embed = Embed(
                title=f'<:greencheck:1006659369519304774> | unban',
                description=choice(unban),
                color=0x8cc63f)
            embed.set_thumbnail(url=member.avatar.url)

            await inter.send(embed=embed)
            await inter.send(choice(welcome))

            await member.unban(reason='Истекло время бана.')

        if not time:
            if member.id == inter.author.id:
                embed = Embed(
                    title='<:redcross:1006554004320428052> | ban',
                    description=choice(author_ban),
                    color=0xde001e)

                await inter.send(embed=embed)
                await inter.send(
                    'https://cdn.discordapp.com/attachments/1009866989105324155/1009867531672109186/IMG_8532.PNG')
                return

            await member.ban(reason=reason)

            embed = Embed(
                title=f'<:greencheck:1006659369519304774> | ban',
                description=choice(after_ban),
                color=0x8cc63f)
            embed.set_thumbnail(url=member.avatar.url)

            embed2 = Embed(
                title=choice(title_ban),
                description=choice(desc_ban),
                color=0x8cc63f,
                timestamp=datetime.now()
            )
            embed2.set_author(name=f'Разбан на сервере "{inter.guild.name}"', icon_url=self.bot.user.avatar.url)
            embed2.add_field('Причина', reason.capitalize())
            invite = await inter.channel.create_invite(max_uses=1, reason='Разбан')
            embed2.add_field('Ссылка на сервер', invite)
            embed2.set_footer(text=f'Администратор: {inter.author}', icon_url=inter.author.avatar.url)

            if inter.guild.icon:
                embed2.set_thumbnail(url=inter.guild.icon.url)

            await member.send(embed=embed2)
            await inter.send(embed=embed)
            await inter.send(choice(angry))

    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.command(aliases=['очистка', 'удали', 'удалить', 'очисти', 'очистить'])
    async def clear(self, inter, count: int):
        after_clear = ['https://cdn.discordapp.com/attachments/1009866989105324155/1009867340726419466/IMG_8515.PNG',
                       'https://cdn.discordapp.com/attachments/1009866989105324155/1009867282538831882/IMG_8504.PNG',
                       'https://cdn.discordapp.com/attachments/1009866989105324155/1009867214637252608/IMG_8490.PNG']

        if count > 500:
            embed = Embed(
                title='<:redcross:1006554004320428052> | clear',
                description='Слишком много сообщений для удаления',
                color=0xde001e)

            await inter.send(embed=embed)
            return

        if 1 > count:
            embed = Embed(
                title='<:redcross:1006554004320428052> | clear',
                description='Неправильное количество сообщений для удаления',
                color=0xde001e)

            await inter.send(embed=embed)
            return
        count += 1
        await inter.channel.purge(limit=count)
        count -= 1
        if (count == 1 or (count % 10 == 1)) and count != 11:
            embed = disnake.Embed(
                title='<:greencheck:1006659369519304774> | clear',
                description=f'Было удалено **{count}** сообщение',
                color=0x8cc63f)

            await inter.send(embed=embed)
        elif ((count % 10 == 2 or count % 10 == 3 or count % 10 == 4) and count > 19) or \
                (count == 2 or count == 3 or count == 4):
            embed = disnake.Embed(
                title='<:greencheck:1006659369519304774> | clear',
                description=f'Было удалено **{count}** сообщения',
                color=0x8cc63f)

            await inter.send(embed=embed)
        else:
            embed = disnake.Embed(
                title='<:greencheck:1006659369519304774> | clear',
                description=f'Было удалено **{count}** сообщений',
                color=0x8cc63f)

            await inter.send(embed=embed)

        await inter.send(choice(after_clear))
        await sleep(600)
        await inter.channel.purge(limit=2)

    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command(aliases=['мут'])
    async def mute(self, inter, member: Member, time: str, *, reason: str = None):

        wrong_time = ['Неверное время!',
                      'Неправильное время',
                      'Такое невозможно',
                      'Введи правильное время',
                      'Я знаю точно невозможное возможно...']

        author_mute = ['Ты пытаешься замутить самого себя!',
                       'Ты что творишь?! Себя нельзя замутить!',
                       'Даже не думай об этом! Себя нельзя замутить!',
                       'Ещё что захотел, нельзя себя замутить!',
                       'Давай ты не будешь меня дергать по пустякам, себя нельзя мутить!',
                       'Придумай что-нибудь получше, себя нельзя замутить!',
                       'Фантазии не хватает? Себя нельзя мутить!',
                       '👉🆔<:deletesign:905943741775368272>',
                       'Пошутил и хватит, себя нельзя замутить!',
                       'Очень смешно, себя нельзя замутить!',
                       'Dino "смееясь во весь голос": себя нельзя замутить!',
                       'Подожди, ты только что пытался себя замутить..?']

        mute_itself = [f'Участник **{member.mention}** был замучен на **{time}** по причине **{reason}**',
                       f'Участник **{member.mention}** ушел думать о своем поведении на **{time}** '
                       f'по причине **{reason}**',
                       f'Участника **{member.mention}** отправили в угол на **{time}** по причине **{reason}**',
                       f'Участник **{member.mention}** был отправлен в ссылку на **{time}** по причине **{reason}**']

        after_mute = [f'Участник **{member.mention}** наконец-то был размучен',
                      f'Участник **{member.mention}** может снова раговаривать',
                      f'Участник **{member.mention}** получает билет в новую жизнь',
                      f'Участник **{member.mention}** покушал и теперь готов к новым приключениям',
                      f'Участник **{member.mention}** выспался и теперь имеет светлый и ясный ум',
                      f'Участник **{member.mention}** подумал о своих пакостях и больше не будет так делать']

        welcome = ['https://cdn.discordapp.com/attachments/1009866989105324155/1009867407801729157/IMG_8522.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867405658427492/IMG_8517.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867340726419466/IMG_8515.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867337115111516/IMG_8509.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867336712466453/IMG_8508.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867216306569237/IMG_8493.PNG']

        if not getseconds(time):
            embed = Embed(
                title='<:redcross:1006554004320428052> | mute',
                description=choice(wrong_time),
                color=0xde001e)

            await inter.send(embed=embed)
            return

        if member.id == inter.author.id:
            embed = Embed(
                title='<:redcross:1006554004320428052> | mute',
                description=choice(author_mute),
                color=0xde001e)

            await inter.send(embed=embed)
            await inter.send(
                'https://cdn.discordapp.com/attachments/1009866989105324155/1009867531672109186/IMG_8532.PNG')
            return

        delta = timedelta(seconds=getseconds(time))

        await inter.guild.timeout(user=member, duration=delta, reason=reason)

        embed = Embed(
            title=f'<:greencheck:1006659369519304774> | mute',
            description=choice(mute_itself),
            color=0x8cc63f)
        embed.set_thumbnail(url=member.avatar.url)

        await inter.send(embed=embed)
        await inter.send(
            'https://media.discordapp.net/attachments/1009866989105324155/1009867409718517880/IMG_8526.PNG')

        await asyncio.sleep(getseconds(time))

        embed = Embed(
            title=f'<:greencheck:1006659369519304774> | unmute',
            description=choice(after_mute),
            color=0x8cc63f)
        embed.set_thumbnail(url=member.avatar.url)

        await inter.send(embed=embed)
        await inter.send(choice(welcome))

    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command(aliases=['анмут', 'размут', 'размутить'])
    async def unmute(self, inter, member: Member, *, reason: str = None):
        welcome = ['https://cdn.discordapp.com/attachments/1009866989105324155/1009867407801729157/IMG_8522.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867405658427492/IMG_8517.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867340726419466/IMG_8515.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867337115111516/IMG_8509.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867336712466453/IMG_8508.PNG',
                   'https://cdn.discordapp.com/attachments/1009866989105324155/1009867216306569237/IMG_8493.PNG']

        after_mute = [f'Участник **{member.mention}** наконец-то был размучен',
                      f'Участник **{member.mention}** может снова раговаривать',
                      f'Участник **{member.mention}** получает билет в новую жизнь',
                      f'Участник **{member.mention}** покушал и теперь готов к новым приключениям',
                      f'Участник **{member.mention}** выспался и теперь имеет светлый и ясный ум',
                      f'Участник **{member.mention}** подумал о своих пакостях и больше не будет так делать']

        await inter.guild.timeout(user=member, duration=None, reason=reason)

        embed = Embed(
            title=f'<:greencheck:1006659369519304774> | unmute',
            description=choice(after_mute),
            color=0x8cc63f)
        embed.set_thumbnail(url=member.avatar.url)

        await inter.send(embed=embed)
        await inter.send(choice(welcome))

    @commands.has_permissions(manage_roles=True, manage_channels=True)
    @commands.bot_has_permissions(manage_roles=True, manage_channels=True)
    @commands.command(aliases=['close', 'закрыть', 'закрой', 'закрывай'])
    async def lock(self, inter):
        await inter.channel.set_permissions(inter.guild.default_role, send_messages=False)
        embed = Embed(
            title='<:greencheck:1006659369519304774> | lock',
            description='🔒⛔ | Чат закрыт',
            color=0x8cc63f
        )
        embed.add_field('Модератор', inter.author.mention)
        embed.add_field('Канал', inter.channel.mention)
        await inter.send(embed=embed)
        await inter.send(
            'https://cdn.discordapp.com/attachments/1009866989105324155/1009867409131327538/IMG_8525.PNG')

    @commands.has_permissions(manage_roles=True, manage_channels=True)
    @commands.bot_has_permissions(manage_roles=True, manage_channels=True)
    @commands.command(aliases=['open', 'открывай', 'открой', 'открыть'])
    async def unlock(self, inter):
        await inter.channel.set_permissions(inter.guild.default_role, send_messages=True)
        embed = Embed(
            title='<:greencheck:1006659369519304774> | unlock',
            description='🔓👐 | Чат открыт',
            color=0x8cc63f
        )
        embed.add_field('Модератор', inter.author.mention)
        embed.add_field('Канал', inter.channel.mention)
        await inter.send(embed=embed)
        await inter.send(
            'https://cdn.discordapp.com/attachments/1009866989105324155/1009867406035910697/IMG_8518.PNG')

    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.command(aliases=['slowmode', 'sm', 'slow mode', 'слоу мод', 'медленный режим', 'медленныйрежим', 'мр'])
    async def slow_mode(self, inter, time: str, channel: str = None):
        wrong_time = ['Неверное время!',
                      'Неправильное время',
                      'Такое невозможно',
                      'Введи правильное время',
                      'Я знаю точно невозможное возможно... (Неверное время)']

        if not channel:
            channel = inter.channel

        if time:
            if time == '0':
                await channel.edit(slowmode_delay=0)
                if inter.channel.id == channel.id:
                    await inter.send(
                        f'⏱ | Был отключен **slow mode** модератором {inter.author.mention}')
                else:
                    await inter.send(
                        f'⏱ | В канале **{channel}** был отключен **slow mode** модератором {inter.author.mention}')
                    await channel.send(
                        f'⏱ | Был отключен **slow mode** модератором {inter.author.mention}')

                return

            if not getseconds(time):
                embed = Embed(
                    title='<:redcross:1006554004320428052> | slowmode',
                    description=choice(wrong_time),
                    color=0xde001e)

                await inter.send(embed=embed)
                return

        await channel.edit(slowmode_delay=int(getseconds(time)))
        if inter.channel.id == channel.id:
            await inter.send(
                f'⏱ | Был установлен **slow mode** на **{time}** '
                f'модератором **{inter.author.mention}**')
        else:
            await inter.send(
                f'⏱ | В канале **{channel}** был установлен **slow mode** на **{time}** '
                f'модератором **{inter.author.mention}**')
            await channel.send(
                f'⏱ | Был установлен **slow mode** на **{time}** '
                f'модератором **{inter.author.mention}**')
        return


def setup(bot):
    bot.add_cog(Moderator(bot))
