"""
import json
from typing import Optional

from aiocqhttp.message import escape
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.helpers import render_expression

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models

# 定义无法获取腾讯智能机器人回复时的「表达（Expression）」
EXPR_DONT_UNDERSTAND = (
    '我现在还不太明白你在说什么呢，但没关系，以后的我会变得更强呢！',
    '我有点看不懂你的意思呀，可以跟我聊些简单的话题嘛',
    '其实我不太明白你的意思……',
    '抱歉哦，我现在的能力还不能够明白你在说什么，但我会加油的～'
)


# 注册一个仅内部使用的命令，不需要 aliases
@on_command('ai_chat')
async def ai_chat(session: CommandSession):
    # 获取可选参数，这里如果没有 message 参数，message 变量会是 None
    message = session.state.get('message')

    # 通过封装的函数获取腾讯智能机器人机器人的回复
    reply = await call_tencent_bot_api(session, message)
    if reply:
        # 如果调用腾讯智能机器人成功，得到了回复，则转义之后发送给用户
        # 转义会把消息中的某些特殊字符做转换，避免将它们理解为 CQ 码
        await session.send(escape(reply))
    else:
        # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取腾讯智能机器人回复时的「表达」
        # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
        await session.send(render_expression(EXPR_DONT_UNDERSTAND))


@on_natural_language
async def _(session: NLPSession):
    # 以置信度 60.0 返回 ai_chat 命令
    # 确保任何消息都在且仅在其它自然语言处理器无法理解的时候使用 ai_chat 命令
    return IntentCommand(60.0, 'ai_chat', args={'message': session.msg_text})


async def call_tencent_bot_api(session: CommandSession, text: Optional[str]) -> Optional[str]:
    # 调用腾讯智能机器人的 API 获取回复

    if not text:
        return None

    try:
        cred = credential.Credential(session.bot.config.TENCENT_BOT_SECRET_ID, session.bot.config.TENCENT_BOT_SECRET_KEY)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        params = {
            # "Action": "ChatBot",
            # "Version": "2019-04-08",
            # "Region": "ap-guangzhou",
            "Query": text,
        }
        req = models.ChatBotRequest()
        req.from_json_string(json.dumps(params))

        resp = client.ChatBot(req).to_json_string()
        print("response:", resp)
        resp_payload = json.loads(resp)
        return resp_payload.get('Reply')

    except TencentCloudSDKException as err:
        print(err)
        return None
"""