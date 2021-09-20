from fastapi import APIRouter, HTTPException
from linebot.models import TextSendMessage
from linebot import LineBotApi
from features.flex_mesages import compare_price_flex
from models.receive import ReceiveCard, ReceiveText
from db import MongoDB
import os
import datetime

client = os.environ.get('MONGODB_URI')
# client = 'mongodb://127.0.0.1:27017'
db = MongoDB(database_name='CompareBOT', uri=client)
collection = 'imports'

route = APIRouter()


def get_profile(user_id, line_bot_api):
    profile = line_bot_api.get_profile(user_id)
    displayName = profile.display_name
    userId = profile.user_id
    img = profile.picture_url
    status = profile.status_message
    result = {'displayName': displayName, 'userId': userId, 'img': img, 'status': status}
    return result


@route.post(
    '/receive', status_code=200,
    summary="Create a flex message",
    response_description="The create flex message",
)
async def receive(item: ReceiveCard):
    """
      Create a flex message to send LINE OA pass channel access token

      -:key
          - **line** : LIST or Array
              **userId** : string
              **channel_access_token** : string
              **docno** : string
              **docdate** : string
              **duedate** : string
              **remark** : string
              **endpoint** : string

      description
          - **line** : multiple object
          - **userId** : token send user
          - **channel_access_token** : LINE account
          - **docno** : unknown
          - **docdate** : unknown
          - **duedate** : unknown
          - **remark** : unknown
          - **endpoint** : unknown

      :param item:
      :return {
              f'LINE OA: ': accounts,
              'message': 'description',
              'status': status (True, False)
          }:
    """
    try:
        item = item.dict()
        for i in item['line']:
            line_bot_api = LineBotApi(i['channel_access_token'])
            profile = get_profile(line_bot_api=line_bot_api, user_id=i['userId'])
            i['displayName'] = profile['displayName']
            i['img'] = profile['img']
            i['status'] = profile['status']
            _d = datetime.datetime.now()
            i["date"] = _d.strftime("%d/%m/%y")
            i["time"] = _d.strftime("%H:%M:%S")
            db.insert_one(collection='send_flex', data=i)
            del i['_id']
            userId = i['userId']
            if i['remark']:
                line_bot_api.push_message(userId,
                                          compare_price_flex(mainname=i['mainname'], docdate=i['docdate'],
                                                             acct_name=i['acct_name'], remark=i['remark'],
                                                             duedate=i['duedate'], docno=i['docno'],
                                                             endpoint=i['endpoint']))
            else:
                line_bot_api.push_message(userId,
                                          compare_price_flex(mainname=i['mainname'], docdate=i['docdate'],
                                                             acct_name=i['acct_name'], remark='ไม่มีข้อมูลเพิ่มเติม',
                                                             duedate=i['duedate'], docno=i['docno'],
                                                             endpoint=i['endpoint']))
        return {
            'message': 'please check your account LINE',
            'detail': {'status': True}
        }
    except:
        raise HTTPException(status_code=400, detail={'status': False})


@route.post(
    '/receive_text', status_code=201,
    summary="Create a message",
    response_description="The create message",
)
async def receive(item: ReceiveText):
    """
    Create a flex message to send LINE OA pass channel access token

    -:key
        - **line** : LIST or Array
            **userId** : string
            **channel_access_token** : string
            **message** : string
            **docno** : string
            **docdate** : string
            **duedate** : string
            **remark** : string
            **endpoint** : string

    description
        - **line** : multiple object
        - **userId** : token send user
        - **channel_access_token** : LINE account
        - **text** : message to user
        - **docno** : unknown
        - **docdate** : unknown
        - **duedate** : unknown
        - **remark** : unknown
        - **endpoint** : unknown

    :param item:
    :return {
            f'LINE OA: ': accounts,
            'message': 'description',
            'status': status (True, False)
        }:
    """
    try:
        oa = []
        item = item.dict()
        for i in item['line']:
            line_bot_api = LineBotApi(i['channel_access_token'])
            profile = get_profile(line_bot_api=line_bot_api, user_id=i['userId'])
            i['displayName'] = profile['displayName']
            i['img'] = profile['img']
            i['status'] = profile['status']
            db.insert_one(collection='send_message', data=i)
            userId = i['userId']
            text = i['text']
            line_bot_api.push_message(userId, TextSendMessage(text=text))
            bot_info = line_bot_api.get_bot_info()
            oa.append(bot_info.display_name)
        return {
            f'LINE OA: ': ", ".join(oa),
            'message': 'please check your account LINE',
            'detail': {'status': True}
        }
    except:
        raise HTTPException(status_code=400, detail={'status': False})
