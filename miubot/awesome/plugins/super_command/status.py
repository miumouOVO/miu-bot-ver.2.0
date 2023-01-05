from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import psutil

@on_command('zhuangtai', aliases=('状态'), permission=SUPERUSER)
async def creat_list(session: CommandSession):
    report = await report_get()
    await session.send(report)
  
async def report_get():
    mum = psutil.virtual_memory()
    tot = round(float(mum.total)/1024/1024/1024)
    usd = round(float(mum.used)/1024/1024)
    fee = round(float(mum.free)/1024/1024)
    cpu_status = psutil.cpu_percent(percpu=True)
    return f'当前使用情况如下：\n总内存：{tot}GB\n已用内存：{usd}MB\n剩余内存：{fee}MB\nCPU使用情况如下：\n{cpu_status}'