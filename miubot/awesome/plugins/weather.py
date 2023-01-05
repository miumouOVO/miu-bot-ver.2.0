from nonebot import on_command, CommandSession
import random
import requests
import json

@on_command('weather', aliases=('天气','查天气','城市天气'))
#定义函数名以及执行命令
async def weather(session: CommandSession):
    city = session.current_arg_text.strip()
    #切除前缀（获取后方数据）
    if not city:
        #第一次返回为空执行
        city = (await session.aget(prompt='你想要看哪的天气捏')).strip()
        while not city:
            #多次返回为空执行
            city = (await session.aget(prompt='请输入城市名捏，不然找不到捏')).strip()
    #数据的返回和发送，可以用yield命令代替（待优化）
    report = await get_report(city)
    weather2 = await report_weather(city)
    await session.send(report)
    await session.send(weather2)

#返回反馈信息
async def get_report(city: str) ->str:
    return f'阿雕正在努力查天气中，请稍等，当城市为:{city}'

#返回API信息
async def report_weather(city: str) ->str:
    url = 'https://tenapi.cn/wether/?city=' + city
    tq = requests.get(url)
    code = tq.json()['code']
    if code == 200:
        city = tq.json()['data'][0]['city']
        time = tq.json()['data'][0]['date']
        weather3 = tq.json()['data'][0]['weather']
        wind = tq.json()['data'][0]['wind']
        return f'{city}\n日期:{time}\n天气:{weather3}\n风向:{wind}'
    else:
        back = random.choice(['没有找到捏，可能是城市不支持捏！','找不到捏，换一个吧！','找不到捏，要不检查一下城市名？'])
        return f'{back}'
