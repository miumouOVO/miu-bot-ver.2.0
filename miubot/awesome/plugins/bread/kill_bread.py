from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import sqlite3

@on_command('kill_bread', aliases=('删除账户'), permission=SUPERUSER)
async def creat_list(session: CommandSession):
    qid = session.current_arg_text.strip()
    #切除前缀（获取后方数据）
    if not qid:
        #第一次返回为空执行
        qid = (await session.aget(prompt='请返回qid')).strip()
        while not qid:
            #多次返回为空执行
            qid = (await session.aget(prompt='请返回qid')).strip()
    return_kill_bread = await kill(qid)
    await session.send(return_kill_bread)
    
async def kill(qid):
    conn = sqlite3.connect("bread.db")
    c = conn.cursor()
    c.execute("DELETE from message where QQ=?",(qid,))
    conn.commit()
    conn.close()
    return f'已清除qid：{qid}的面包账户'