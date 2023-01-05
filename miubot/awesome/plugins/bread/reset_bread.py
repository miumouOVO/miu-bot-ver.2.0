from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import sqlite3

@on_command('reset_bread', aliases=('清零账户'), permission=SUPERUSER)
async def creat_list(session: CommandSession):
    qid = session.current_arg_text.strip()
    #切除前缀（获取后方数据）
    if not qid:
        #第一次返回为空执行
        qid = (await session.aget(prompt='请返回qid')).strip()
        while not qid:
            #多次返回为空执行
            qid = (await session.aget(prompt='请返回qid')).strip()
    return_resat_bread = await resait(qid)
    await session.send(return_resat_bread)
    
async def resait(qid):
    conn = sqlite3.connect("bread.db")
    c = conn.cursor()
    cursor = c.execute("UPDATE message set shuliang = ? where QQ=?",(0, qid,))
    conn.commit()
    conn.close()
    return f'已清零qid：{qid}的面包账户'