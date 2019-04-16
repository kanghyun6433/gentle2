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
        embed.set_footer(text = "")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-야수선배'):
        await client.send_message(message.channel, '응앗-! (≧Д≦)')

    if message.content.startswith('뤼-투표'): 
         vote = message.content[4:].split("/")
         await client.send_message(message.channel, "투표- " + "투표해라 뤼기야!" + vote[0])
         for i in range(1, len(vote)):
            choose = await client.send_message(message.channel, "```" + vote[i] + "```" )
            await client.add_reaction(choose, '🤔')

    if message.content.startswith('뤼-야수선배'):
        await client.send_message(message.channel, '응앗-! (≧Д≦)')

    if message.content.startswith('뤼-약빨도링'):
        embed = discord.Embed(title="약빨도링", description="", color=0xFF0000)
        embed.set_footer(text = "청음뭐노...")
        embed.set_image(url="data:image/jpeg;base64,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 ")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-엔센'):
        embed = discord.Embed(title="엔센", description="", color=0xFF0000)
        embed.set_footer(text = "영상BBBBBBBBBBBBBBBBBBBB")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mAO4LcwyDgcqhGBTvJwiIyXHrH9ckLSv1bwiA=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-여우엘건'):
        embed = discord.Embed(title="여우엘건", description="", color=0xFF0000)
        embed.set_footer(text = "씨포디 배우고 시프다")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mD15GWyW7pCzmHEzEb7VUiMhmLIXDxIbOMh8Q=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-큐브'):
        embed = discord.Embed(title="큐브", description="", color=0xFF0000)
        embed.set_footer(text = "죠죠성애자")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mBtfkL_q-wpuG84OfCnoZ9off3FzaYAGzvf-g=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-엑스타시'):
        embed = discord.Embed(title="엑스타시", description="", color=0xFF0000)
        embed.set_footer(text = "음원괴물...")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mAlhbsHGuZqvGGxdBc6XS8mT5y_qeZVRQGJ7A=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-오스타'):
        embed = discord.Embed(title="오스타", description="", color=0xFF0000)
        embed.set_footer(text = "알랑가몰라..왜...곡 엌ㅋㅋㅋ")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8c3vcWgid7MIkFlEhz7ADl16DvCJNZckxdKLNdWxUe4oyImIANw")
        await client.send_message(message.channel, embed=embed)



client.run('NTY2NDIyMjUzODI3MzkxNDk4.XLGnqg.SDAg3rSv7HPAkfrqE8LlqSiNrto')
