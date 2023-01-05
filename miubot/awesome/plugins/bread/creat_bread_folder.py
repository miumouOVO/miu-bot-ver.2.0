from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import sqlite3
import time

@on_command('creat_bread', aliases=('创建面包账户','创建面包篮','创建面包库'))
async def talk(session: CommandSession):
    qid = str(session.ctx['user_id'])
    tm = time.time()
    t = tm - 3600
    conn = sqlite3.connect("bread.db")
    c = conn.cursor()
    c.execute("insert into message(QQ, shuliang, time, eattime) values (?, ?, ?, ?)",(qid, 0, t, t))
    conn.commit()
    conn.close()
    await session.send('创建成功,您目前有面包0个捏！')