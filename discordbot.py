# インストールした discord.py を読み込む
import discord
import latlon
import urllib.parse 
import demjson
import config

# 自分のBotのアクセストークンに置き換えてください
TOKEN = config.TOKEN

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content[0:5] == '/tama' :
        destination = latlon.getlatlon(message.content)
        await message.channel.send('じゃらじゃら')
        await message.channel.send(destination)
        # url = "https://maps.google.com/?q=" + urlencode(str(destination[0])+str(destination[1])).encode('ascii')
        # data = {"content": "34.98625332246909, 135.7589705460798"}
        parameter = urllib.parse.quote(str(destination[0])+","+str(destination[1]))
        url = "https://maps.google.com/?q=" + parameter
        await message.channel.send(url)


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
