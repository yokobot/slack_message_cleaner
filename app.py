# coding: utf-8
import time
from urllib import response
import PySimpleGUI as sg
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


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
        print(channel_id + ' のメッセージを削除します.')

        try:
            response = web_client.pins_list(channel=channel_id)
            pins_list = []

            for item in response['items']:
                pins_list.append(item['message']['ts'])

            response = web_client.conversations_history(channel=channel_id)

            for message in response['messages']:
                if message['ts'] not in pins_list:
                    result = web_client.chat_delete(
                        channel=channel_id,
                        ts=message['ts']
                    )
                    print('1 message deleteed')
                time.sleep(1)

            while True:
                if not response.get('response_metadata'):
                    break
                else:
                    response = web_client.conversations_history(
                        channel=channel_id,
                        cursor=response['response_metadata']['next_cursor']
                    )

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

        print('all message are deleted.')
        #TODO ループをもうちょっとシンプルにする
        #TODO 処理中にcloseボタンが押された場合の処理を入れる

window.close()
