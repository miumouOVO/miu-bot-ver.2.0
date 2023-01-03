from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import sqlite3
import time

@on_command('open_shop', aliases=('面包店开张'), permission=SUPERUSER)
async def creat_list(session: CommandSession):
       conn = sqlite3.connect('bread.db')
       await session.send('数据库创建成功！')
       c = conn.cursor()
       c.execute('''CREATE TABLE message
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              QQ           INT    NOT NULL,
              shuliang        CHAR(500),
              time        CHAR(500),
              eattime        CHAR(500),
              SALARY         REAL);''')
       await session.send('数据表创建成功！\n面包机已就绪')
       conn.commit()
       conn.close()