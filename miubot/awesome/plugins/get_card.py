from nonebot import on_command, CommandSession
import random

#命令定义与处理
@on_command('talk', aliases=('十连寻访','十连抽卡','十连','方舟十连'))
async def talk(session: CommandSession):
    report_message = await report_msg()
    report = await get_report()
    await session.send(report_message)
    await session.send(report)

#反馈信息
async def report_msg():
    return f'阿雕正在获取抽卡结果，请稍等一下捏！'

#处理抽卡链接
async def get_report():
    x = random.randint(1,100)
    x = str(x) 
    url1 = 'http://api.baimianxiao.cn/arknights/arknightsdraw/main.php'
    return f'[CQ:image,file={url1}?{x}]'