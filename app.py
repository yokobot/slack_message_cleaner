# coding: utf-8
import time
import logging
import traceback
from urllib import response
import PySimpleGUI as sg
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


sg.theme('DarkAmber')   # デザインテーマの設定


# ウィンドウに配置するコンポーネント
layout = [
    [sg.Text('slack user token を入力してください')],
    [sg.Text('token', size=(10, 1)), sg.InputText('', size=(80, 1), key='token')],
    [sg.Text('メッセージを削除する slack channel 名を入力してください')],
    [sg.Text('channel', size=(10, 1)), sg.InputText('', size=(80, 1), key='channel')],
    [sg.Button('削除'), sg.Button('キャンセル')],
    [sg.Output(size=(120, 60))]
]


# ウィンドウの生成
window = sg.Window('slack message cleaner', layout)


# イベントループ
while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'キャンセル':
        for key in ['token', 'channel']:
            window[key]('')

    elif event == '削除':
        web_client = WebClient(token=values['token'])
        channel_id = values['channel']
        print(channel_id)

        try:
            #TODO ページング対応する
            response = web_client.pins_list(channel=channel_id)
            pins_list = []

            for item in response['items']:
                pins_list.appned(item['message']['ts'])

            response = web_client.conversations_history(channel=channel_id)

            for message in response['messages']:
                if message['ts'] not in pins_list:
                    result = web_client.chat_delete(
                        channel=channel_id,
                        ts=message['ts']
                    )
                    print('1 message deleteed')
                time.sleep(1)

        except SlackApiError as e:
            print(f"Error posting message: {e}")
        #TODO 終了処理を入れる

window.close()
