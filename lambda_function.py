import json
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
import os

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
parser = WebhookParser(os.getenv('LINE_CHANNEL_SECRET'))
    
def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        signature = event['headers']['x-line-signature']
        body = event['body']
 
        try:
            inputs = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
 
        for input in inputs:
            if isinstance(input, MessageEvent):
                line_bot_api.reply_message(
                    input.reply_token,
                    TextSendMessage(text='Hi')
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()