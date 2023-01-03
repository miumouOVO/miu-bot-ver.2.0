from nonebot import on_command, CommandSession
import random
import requests
import json

@on_command('get_bettle', aliases=('捡瓶子','捡漂流瓶','漂流瓶','pick'))
#定义函数名以及执行命令
async def get_bettle(session: CommandSession):
    bettle = await get_report()
    await session.send(bettle)

async def get_report():
    url = 'http://ovooa.com/API/Piao/api.php?Select=0'
    msg = requests.get(url)
    title = msg.json()['data'][0]['title']
    text = msg.json()['data'][0]['text']
    time = msg.json()['data'][0]['time']
    return f'title:{title}\ntext:{text}\ntime:{time}'