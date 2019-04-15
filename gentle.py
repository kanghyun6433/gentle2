import discord
import asyncio
import datetime
from requests import *
import random

 
client = discord.Client()

now = datetime.datetime.now()


 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
@client.event
async def on_message(message):
    if message.author.bot:
        return None

        id = message.author.id

    if message.content.startswith('뤼-정보'):
        embed = discord.Embed(title="젠틀봇", description="옵빤 싸이ㅣㅣㅣ야!!", color=0x00ff00)
        embed.set_footer(text = "하하하하하하하하하하하")
        embed.set_image(url="https://image.ytn.co.kr/general/jpg/2013/0502/201305020847443307_h.jpg")
        await client.send_message(message.channel, embed=embed)


    elif message.content.startswith('뤼-말해'):
        await client.send_message(message.channel, '남겨라 뤼기야!')
        msg = await client.wait_for_message(timeout=15.0, author=message.author)
        if msg is None:
            await client.send_message(message.channel, '시.바 빨리말해라 뤼기야! 다시시도: 뤼-말해')
            return
        else:
            await client.send_message(message.channel, msg.content)

    elif message.content.startswith('뤼-오늘'):
        embed = discord.Embed(title="지금씨각은?", description="", color=0x00ff00)
        embed.set_footer(text = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, choiceresult)

    if message.content.startswith('뤼-운세'):
        luck = ":o::o::o::o::o: :o::o::o::o::x: :o::o::o::x::x: :o::o::x::x::x: :o::x::x::x::x: :x::x::x::x::x:"
        luckchoice = luck.split(" ")
        lucknumber = random.randint(1, len(luckchoice))
        luckresult = luckchoice[lucknumber-1]
        embed = discord.Embed(title=luckresult, description=" ", color=0x00ff00)
        embed.set_footer(text = "X가 많을수록 불행한것이다 뤼이이기야!")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-도와줘'):
        await client.send_message(message.channel, '뤼-운세,뤼-골라,뤼-오늘,뤼-말해,뤼-정보,뤼-play,뤼-queue,뤼-skip.뤼-np,뤼-perms')
         
         
    if message.content.startswith('뤼-기야'):
        await client.send_message(message.channel, '오뻔 싸이!야!..하ㅏ하하하하하하하')

    if message.content.startswith('뤼-호성'):
        embed = discord.Embed(title="나랑께", description="", color=0xFF0000)
        embed.set_footer(text = " ")
        embed.set_image(url="https://pbs.twimg.com/profile_images/1266715535/_________400x400.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-섹스'):
        await client.send_message(message.channel, '개변태새끼')

    if message.content.startswith('뤼-노무현'):
        await client.send_message(message.channel, '일배새끼')

    if message.content.startswith('뤼-ㅇㅇㄱㅇㄴ'):
        await client.send_message(message.channel, '섹스하자') 

    if message.content.startswith('뤼-cldgonz'):
        embed = discord.Embed(title="구르미르님", description="https://www.youtube.com/channel/UCZh8J1a9eOoXdtwmbufUM-Q", color=0xFF0000)
        embed.set_footer(text = "젠틀맨의 시초")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-야수선배'):
        await client.send_message(message.channel, '응앗-! (≧Д≦)') 

    

    
client.run('NTY2NDIyMjUzODI3MzkxNDk4.XLGnqg.SDAg3rSv7HPAkfrqE8LlqSiNrto')
