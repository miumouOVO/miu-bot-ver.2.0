from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import sqlite3
import time
import random

@on_command('open_shop', aliases=('吃面包','🍞🍞'))
async def talk(session: CommandSession):
    uid = str(session.ctx['user_id'])
    tm = time.time()
    eatnum = int(random.randint(1,10))#随机吃数量
    try:
        #读取初始数据
        conn = sqlite3.connect("bread.db")
        c = conn.cursor()
        cursor = c.execute("SELECT shuliang, eattime from message where QQ=?",(uid,))
        for row in cursor:
            a = row
        #数据处理
        bread = a[0]
        t = a[1]
        t = float(t)
        bread = int(bread)
        num = bread - eatnum
        nt = time.time()
        ft = t + 3600
        if (bread > 10):
            if (ft <= nt):
                #存入数据
                conn = sqlite3.connect("bread.db")
                c = conn.cursor()
                cursor = c.execute("UPDATE message set shuliang = ? where QQ=?",(num, uid,))
                conn.commit()
                c = conn.cursor()
                cursor = c.execute("UPDATE message set eattime = ? where QQ=?",(nt, uid,))
                conn.commit()
                #发送数据
                await session.send('您成功吃掉了{0}个面包捏,您现在有{1}个面包捏！'.format(eatnum,num))
            else:
                st = ft - nt
                mn = int(st)
                lt = mn / 60
                elt = int(lt)
                await session.send('您现在还不可以吃面包捏,您还需要等待{0}分钟捏！'.format(elt))
        else:
            await session.send('您的面包总数不够捏！')
    except NameError:
        await session.send('您未创建账户,请使用‘创建面包账户’指令来创建账户并重新购买！')