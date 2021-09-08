import discord
import asyncio
from random import*

client = discord.Client()


token = "ODg0OTkyMDA3MTU4NzcxNzUy.YTgjCA.ceRxyKjuMyyKIOkoFRZGo7JUs3o"


#로또 구성함수
def start():
   
     listnum =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
     20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,
     38,39,40,41,42,43,44,45]

     shuffle(listnum)

     lotto = sample(listnum,6)
     lotto1 = sample(listnum,6)
     lotto2 = sample(listnum,6)
     lotto3 = sample(listnum,6)
     lotto4 = sample(listnum,6)
     lotto.sort()
     lotto1.sort()
     lotto2.sort()
     lotto3.sort()
     lotto4.sort()

     return "추천번호는\n"+str(lotto)+"\n"+str(lotto1)+"\n"+str(lotto2)+"\n"+str(lotto3)+"\n"+str(lotto4)+"\n입니다."
    

@client.event
async def on_ready():
    
    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    bot = discord.Game('또봇')
    await client.change_presence(status=discord.Status.online, activity=bot)

@client.event
async def on_message(message):
    if message.content == "#로또":
        await message.channel.send(start())
client.run(token)    