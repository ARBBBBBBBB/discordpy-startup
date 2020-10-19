# インストールした discord.py を読み込む
import discord
import random


# 自分のBotのアクセストークンに置き換えてください
TOKEN = ''

CHANNEL_ID = 766900458504847412 # 任意のチャンネルID(int)
CHANNEL_ID_WATCHING = 726401343744376863

join_list = []


# 接続に必要なオブジェクトを生成
client = discord.Client()
    
# 任意のチャンネルで挨拶する非同期関数を定義

async def greet():
    greet_mes = True
    channel = client.get_channel(CHANNEL_ID)
    if greet_mes == True:
        await channel.send('やあ')  
        greet_mes = False
    else:
        await channel.send('またね')

# bot起動時に実行されるイベントハンドラを定義==========================================
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('オンラインになりました')
    
    await greet() # 挨拶する非同期関数を実行

@client.event
async def on_disconnect():
    print('オフラインになりました')
    
    await greet() # 挨拶する非同期関数を実行
    
#=============================================================================

#リストの取得と表示==============================================================
# コマンドに対応するリストデータを取得する関数を定義
def get_data(message):
    command = message.content
    data_table = {
        '/members': message.guild.members, # メンバーのリスト
        '/roles': message.guild.roles, # 役職のリスト
        '/text_channels': message.guild.text_channels, # テキストチャンネルのリスト
        '/voice_channels': message.guild.voice_channels, # ボイスチャンネルのリスト
        '/category_channels': message.guild.categories, # カテゴリチャンネルのリスト
    }
    return data_table.get(command, '無効なコマンドです')

# 発言時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    if message.content == '/join':
        print (message.author.id)
        join_list.append(message.author.id)
        await message.channel.send(str(message.author) + 'をプレイヤーに追加しました')
        print(join_list)
 
    # 「/profile」と発言したらプロフィールが返る処理
    elif message.content == '/profile':
        await message.channel.send('among_usしようぜ！！！')
        await message.add_reaction("😙")
        
    elif message.content == '/start':
        await message.channel.send('役職を配布します')
        channel = client.get_channel(CHANNEL_ID_WATCHING)
        if len(join_list) !=0:
            list(set(join_list))
            fox = str(random.choice(join_list))
            mention = '<@'+ fox + '>'
            await channel.send(mention) 
        else:
            channel = client.get_channel(CHANNEL_ID)
            await message.channel.send('参加者が登録されていません')
    elif message.content == '/end':
        join_list.clear()
        await message.channel.send('参加者をリセットしました')
        print(join_list)
    

    
#============================================================================


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

