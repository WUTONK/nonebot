from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg
import random

@on_command('shanghai_th',aliases=('上海'))
async def weather(session: CommandSession):
    sendWord = random.uniform(0,2)
    if sendWord == 0:
        await session.send('上海！')
    elif sendWord == 1:
        await session.send('上海！！💢')
    else:
        await session.send('上海！！！💢上海！！！💢')
 
@on_command('penglai_th',aliases=('蓬莱'))
async def weather(session: CommandSession):
    await session.send('蓬莱！！！蓬莱！！！')

@on_command('shanghai_th',aliases=('运势'))
async def weather(session: CommandSession):
    sendWord = random.uniform(0,5)
    if sendWord == 0:
        await session.send('')
    elif sendWord == 1:
        await session.send('')
    elif sendWord == 2:
        await session.send('')
    elif sendWord == 3:
        await session.send('')
    elif sendWord == 4:
        await session.send('')  
    else:          
        await session.send('')

@on_command('sayFumo',aliases=('fumo'))
async def weather(session: CommandSession):
    await session.send('FUMO!!!🌀FUMO!!!🌀')