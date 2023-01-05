from nonebot import on_command, CommandSession
import requests

#命令定义与处理
@on_command('girl_picture', aliases=('姐姐图片','/姐姐'))
async def talk(session: CommandSession):
    report_message = await report_msg()
    report = await get_report()
    await session.send(report_message)
    await session.send(report)

#反馈信息
async def report_msg():
    return f'阿雕正在寻找图片，请稍等一下捏！'

#处理图片链接
async def get_report():
    url = 'https://player.lzti.com/open/img/mm?type=json'
    js = requests.get(url)
    picture_url = js.json()['img']
    return f'[CQ:image,file={picture_url}]'