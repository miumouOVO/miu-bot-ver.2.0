from nonebot import on_command, CommandSession

@on_command('talk', aliases=('测试启动'))
async def talk(session: CommandSession):
    report = await get_report()
    await session.send(report)

async def get_report():
    return f'测试成功，雕bot.ver.2.0已成功启动~'