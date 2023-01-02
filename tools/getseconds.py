from disnake.ext.commands import BadArgument


def getseconds(string):
    b = ''
    a = ''
    for i in string:
        try:
            i = int(i)
            a = a + str(i)
        except:
            b = b + i
    if b == 'm' or b == 'minute' or b == 'minutes' or b == 'min' or b == 'м' or b == 'мин' or b == 'минут' or b == 'минуту' or b == 'минута' \
            or b == ' m' or b == ' minute' or b == ' minutes' or b == ' min' or b == ' м' or b == ' мин' or b == ' минут' or b == ' минуту' or b == ' минута':
        return int(a) * 60
    elif b == 's' or b == 'sec' or b == 'second' or b == 'seconds' or b == 'с' or b == 'сек' or b == 'секунд' or b == 'секунду' or b == 'секунды' \
            or b == ' s' or b == ' sec' or b == ' second' or b == ' seconds' or b == ' с' or b == ' сек' or b == ' секунд' or b == ' секунду' or b == ' секунды':
        return int(a)
    elif b == 'h' or b == 'hour' or b == 'hours' or b == 'ч' or b == 'часа' or b == 'час' or b == 'часов' \
            or b == ' h' or b == ' hour' or b == ' hours' or b == ' ч' or b == ' часа' or b == ' час' or b == ' часов':
        return int(a) * 3600
    elif b == 'd' or b == 'day' or b == 'days' or b == 'д' or b == 'дней' or b == 'дня' or b == 'день' \
            or b == ' d' or b == ' day' or b == ' days' or b == ' д' or b == ' дней' or b == ' дня' or b == ' день':
        return int(a) * 86400
    elif b == 'month' or b == 'mon' or b == 'months' or b == 'месяц' or b == 'мес' or b == 'месяцев' or b == 'месяца' \
            or b == ' month' or b == ' mon' or b == ' months' or b == ' месяц' or b == ' мес' or b == ' месяцев' or b == ' месяца':
        return int(a) * 604800
    elif b == 'y' or b == 'year' or b == 'years' or b == 'г' or b == 'год' or b == 'года' or b == 'лет' or b == 'л' \
            or b == ' y' or b == ' year' or b == ' years' or b == ' г' or b == ' год' or b == ' года' or b == ' лет' or b == ' л':
        return int(a) * 31536000
    else:
        raise BadArgument()
