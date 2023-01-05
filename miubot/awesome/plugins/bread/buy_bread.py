from nonebot import on_command, CommandSession
import sqlite3
import time
import random

@on_command('buy_bread', aliases=('买面包','🍞'))
async def talk(session: CommandSession):
    uid = str(session.ctx['user_id'])
    tm = time.time()
    buynum = int(random.randint(1,10))#随机购买数量
    #进行账户判定
    try:
        #读取初始数据
        conn = sqlite3.connect("bread.db")
        c = conn.cursor()
        cursor = c.execute("SELECT shuliang, time from message where QQ=?",(uid,))
        for row in cursor:
            a = row
        b = int(a[0])
        t = float(a[1])
        num = buynum + b
        nt = time.time()
        ft = t + 3600
        #进行时间判定
        if (ft <= nt):
            #存入数据
            conn = sqlite3.connect("bread.db")
            c = conn.cursor()
            cursor = c.execute("UPDATE message set shuliang = ? where QQ=?",(num, uid,))
            conn.commit()
            c = conn.cursor()
            cursor = c.execute("UPDATE message set time = ? where QQ=?",(nt, uid,))
            conn.commit()
            #发送数据
            await session.send('您成功购买了{0}个面包捏,您现在有{1}个面包捏！'.format(buynum,num))
        else:
            #如果超出时间
            st = ft - nt
            mn = int(st)
            lt = mn / 60
            elt = int(lt)
            await session.send('您现在还不可以买面包捏,您还需要等待{0}分钟捏！'.format(elt))
        #如果没有账户
    except NameError:
        await session.send('您未创建账户,请使用‘创建面包账户’指令来创建账户并重新购买！')