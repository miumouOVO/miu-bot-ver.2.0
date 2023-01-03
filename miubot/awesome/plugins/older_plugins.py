from nonebot import on_command, CommandSession

@on_command('talk', aliases=('我的面包','吃面包','查看面包'))
async def talk(session: CommandSession):
    report = await get_report()
    await session.send(report)

async def get_report():
    return f'雕bot正在更新中~\n请耐心等待面包机重构哦~\n到时候就有更好用的雕bot了捏！'