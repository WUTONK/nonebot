from nonebot import on_notice, NoticeSession


# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    # 发送欢迎消息
    if session.event.group_id == 1040643413 :
        await session.send('欢迎新朋友～')