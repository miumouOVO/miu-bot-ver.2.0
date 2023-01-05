from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import sqlite3


@on_command('my_bread', aliases=('我的面包'))
async def talk(session: CommandSession):
    uid = str(session.ctx['user_id'])
    try:
        conn = sqlite3.connect("bread.db")
        c = conn.cursor()
        cursor = c.execute("SELECT shuliang, time from message where QQ=?",(uid,))
        for row in cursor:
            a = row
        b = a[0]
        await session.send('你现在有{0}个面包捏！'.format(b))
    except NameError:
        await session.send('您未创建账户,请使用‘创建面包账户’指令来创建账户并重新购买！')