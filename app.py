# coding: utf-8
import PySimpleGUI as sg

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [
    [sg.Text('メッセージを削除する slack workspace 名と channel 名を入力してください')],
    [sg.Text('workspace', size=(10, 1)), sg.InputText('', size=(40, 1), key='workspace')],
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

window.close()
