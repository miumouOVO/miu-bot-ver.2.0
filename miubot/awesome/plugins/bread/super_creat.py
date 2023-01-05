from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import sqlite3
import time

@on_command('super_creat', aliases=('后台创建账户','指令创建账户'), permission=SUPERUSER)
async def creat_list(session: CommandSession):
    qid = session.current_arg_text.strip()
    #切除前缀（获取后方数据）
    if not qid:
        #第一次返回为空执行
        qid = (await session.aget(prompt='请返回qid')).strip()
        while not qid:
            #多次返回为空执行
            qid = (await session.aget(prompt='请返回qid')).strip()
    return_creat_bread = await creat(qid)
    await session.send(return_creat_bread)
    
async def creat(qid):
    tm = time.time()
    t = tm - 3600
    conn = sqlite3.connect("bread.db")
    c = conn.cursor()
    c.execute("insert into message(QQ, shuliang, time, eattime) values (?, ?, ?, ?)",(qid, 0, t, t))
    conn.commit()
    conn.close()
    return f'已创建面包账户：{qid}'
    