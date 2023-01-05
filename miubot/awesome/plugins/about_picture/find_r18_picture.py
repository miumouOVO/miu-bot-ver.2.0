from nonebot import on_command, CommandSession
from nonebot.permission import PRIVATE
import requests
import json

@on_command('r18_picture', aliases=('r18查图','r18找图'),permission=PRIVATE)
#定义函数名以及执行命令
async def talk(session: CommandSession):
    tag = session.current_arg_text.strip()
    #切除前缀（获取后方数据）
    if not tag:
        #第一次返回为空执行
        tag = (await session.aget(prompt='不知道要找什么图捏')).strip()
        while not tag:
            #多次返回为空执行
            tag = (await session.aget(prompt='请输入tag捏，不然不知道找什么图捏')).strip()
    #数据的返回和发送，可以用yield命令代替（待优化）
    report = await get_report(tag)
    picture = await report_picture(tag)
    await session.send(report)
    await session.send('阿雕温馨提示：手冲伤身捏，要少冲捏！')
    await session.send(picture)

#返回反馈信息
async def get_report(tag: str) ->str:
    return f'阿雕正在努力查图中，请稍等，当前tag为:{tag}'

#返回图片
async def report_picture(tag: str) ->str:
    try:
        url2 = 'https://api.lolicon.app/setu/v2?size=regular&tag=' + tag
        menu = requests.get(url2)
        setu_url = menu.json()['data'][0]['urls']['regular']
        return f'[CQ:image,file={setu_url}]'
    except IndexError:
        return '找不到图捏...'