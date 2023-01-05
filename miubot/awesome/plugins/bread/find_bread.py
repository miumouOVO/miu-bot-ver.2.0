from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import sqlite3
import time

@on_command('find_bread', aliases=('查看面包','查面包'))
async def talk(session: CommandSession):
    qid = session.current_arg_text.strip()
    #切除前缀（获取后方数据）
    if not qid:
        #第一次返回为空执行
        qid = (await session.aget(prompt='不知道要查谁的捏')).strip()
        while not qid:
            #多次返回为空执行
            qid = (await session.aget(prompt='请返回要查询者qq号捏')).strip()
    return_bread = await find(qid)
    await session.send(return_bread)
    
async def find(qid):
    try:
        conn = sqlite3.connect("bread.db")
        c = conn.cursor()
        cursor = c.execute("SELECT shuliang, time from message where QQ=?",(qid,))
        for row in cursor:
            a = row
        b = a[0]
        return f'他/她有{b}个面包捏！'
    except NameError:
        return '没有找到指定账户捏，该账户或许并没有创建面包账户捏！'
