# slack_message_cleaner

slackの無料バージョンを使用していて、メッセージ数が溢れそうになって時に削除する GUI です。
指定したチャンネルのメッセージを削除します（ピン留めされたメッセージは残ります）。
以下を事前に準備してください。

- slack user token
    - 以下の権限が必要です
    - channels:history, channels:read, chat:write, groups:history, groups:read, im:history, im:read, mpim:history, mpim:read, pins:read
- メッセージを削除する slack channel id

## poetry

`poetry` を使っています。
事前にインストールしてください。

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

## usage

1. poetry install
1. poetry run python app.py