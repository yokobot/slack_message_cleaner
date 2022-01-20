# coding: utf-8
import os
import logging
from urllib import response
import PySimpleGUI as sg
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

web_client = WebClient(token=os.environ.get("SLACK_USER_TOKEN"))

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [
    [sg.Text('メッセージを削除する slack channel 名を入力してください')],
    [sg.Text('channel', size=(10, 1)), sg.InputText('', size=(40, 1), key='channel')],
    [sg.Button('削除'), sg.Button('キャンセル')],
    [sg.Output(size=(80, 20))]
]

# ウィンドウの生成
window = sg.Window('slack message cleaner', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    elif event == '削除':
        print('slackのメッセージを削除する処理を書く')
        channel_id = values['channel']
        print(channel_id)
        response = web_client.conversations_history(channel=channel_id)
        print(response)

window.close()
