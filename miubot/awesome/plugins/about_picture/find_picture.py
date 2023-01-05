from nonebot import on_command, CommandSession
import requests
import json

@on_command('picture', aliases=('查图','找图'))
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
    await session.send(picture)

#返回反馈信息
async def get_report(tag: str) ->str:
    return f'阿雕正在努力查图中，请稍等，当前tag为:{tag}\n若没有收到就是被吞了捏（会优化的QAQ）'

#返回图片
async def report_picture(tag: str) ->str:
    try:
        url2 = 'https://api.lolicon.app/setu/v2?size=regular&tag=' + tag
        menu = requests.get(url2)
        setu_url = menu.json()['data'][0]['urls']['regular']
        return f'[CQ:image,file={setu_url}]'
    except IndexError:
        return '找不到图捏...'