from nonebot import on_command, CommandSession


@on_command('cai_ys',aliases=('菜!',"菜！"))
async def weather(session: CommandSession):
    await session.send('菜！')
@on_command('ban_ys',aliases=('ban!','ban！'))
async def weather(session: CommandSession):
    await session.send('ban!')
    
    