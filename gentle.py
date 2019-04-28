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

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Example ROle')
    await client.add_roles(member, role)

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
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mBOTjG4ThwD59vbjaSaCkjOkL_jXKHWjkeoNQ=s288-mo-c-c0xffffffff-rj-k-no")
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

    if message.content.startswith('뤼-엑스터시'):
        embed = discord.Embed(title="엑스터시", description="", color=0xFF0000)
        embed.set_footer(text = "음원괴물...")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mAlhbsHGuZqvGGxdBc6XS8mT5y_qeZVRQGJ7A=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-오스타'):
        embed = discord.Embed(title="오스타", description="", color=0xFF0000)
        embed.set_footer(text = "알랑가몰라..왜...곡 엌ㅋㅋㅋ")
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8c3vcWgid7MIkFlEhz7ADl16DvCJNZckxdKLNdWxUe4oyImIANw")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-겜북'):
        embed = discord.Embed(title="겜북", description="", color=0xFF0000)
        embed.set_footer(text = "스키나 만들어 주세요오오!!")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mCE93Zo2SJ32AVmn895xajDq49E5ikGacy0mw=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-대왕세종'):
        embed = discord.Embed(title="머앟세종", description="", color=0xFF0000)
        embed.set_footer(text = "영상 많이 느심")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mBuu8G1iQ--Se6PABtOaVf2VB2TylkzJtq8tw=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-slp'):
        embed = discord.Embed(title="slp", description="", color=0xFF0000)
        embed.set_footer(text = "실력이 느는게 보입니다! 힘내요!")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mASzxkBWQF9Pa0d9oFN_u1nuzBUavfi6_5-Yw=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-대한뚝배기'):
        embed = discord.Embed(title="위대한뚝배기", description="", color=0xFF0000)
        embed.set_footer(text = "")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mBSlyVj1dnkpckRPMPFjFFZHIhR57K0nRCr7g=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-샌즈'):
        await client.send_message(message.channel, '젠젠젠젠젠젠젠젠젠젠젠...젠젠..젠젠')


    if message.content.startswith('뤼-나옴'):
        embed = discord.Embed(title="나옴", description="", color=0xFF0000)
        embed.set_footer(text = "으으읔...나옴 엌ㅋㅋㅋ")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mDQWNSoEqqbjfa9cQgLcOVOk4ChfrPSst8VSQ=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-오빠워치'):
        embed = discord.Embed(title="오빠워치", description="", color=0xFF0000)
        embed.set_footer(text = "ㅗ빠워치")
        embed.set_image(url="https://cdn.discordapp.com/attachments/557926896374120458/568015688648884234/JPEG_20190402_011627.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-한'):
        embed = discord.Embed(title="한", description="", color=0xFF0000)
        embed.set_footer(text = "남")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mD05BiG1apM0e2E2LS4DZxG9NzFltGLY_Fg6A=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('뤼-취향'):
        await client.send_message(message.channel, '내취향은 레드존만 만드는 야수선배야!')

    if message.content.startswith('뤼-싸이'):
        await client.send_message(message.channel, '싸이오닉 에너지가 충전되었다.')

    if message.content.startswith('뤼-투쉬'):
        await client.send_message(message.channel, '(투쉬)')

    if message.content.startswith('뤼-안녕'):
        await client.send_message(message.channel, '응 안녕못해ㅋ')

    if message.content.startswith('뤼-아버지'):
        await client.send_message(message.channel, '너무 살아오셧네~')

    if message.content.startswith('뤼-아나'):
        await client.send_message(message.channel, '왔어난~')

    if message.content.startswith('뤼-마감'):
        await client.send_message(message.channel, 'https://cdn.discordapp.com/attachments/566809829507858477/567991610202390528/1174e574b96cffa3.PNG')

    if message.content.startswith('뤼-슈퍼걸'):
        await client.send_message(message.channel, '로 딸치고 싶다')

    if message.content.startswith('뤼-오니짱'):
        await client.send_message(message.channel, '와타시..오니짱오..스키!')

    if message.content.startswith('뤼-야동'):
        await client.send_message(message.channel, '아꼴려..아꼴려..아꼴려..아꼴려..')

    if message.content.startswith('뤼-감기'):
        await client.send_message(message.channel, '감감감감감감감감감감감감감감감감')

    if message.content.startswith('뤼-치노'):
        await client.send_message(message.channel, '노?신고 ㅅㄱ')

    if message.content.startswith('뤼-마더파더'):
        await client.send_message(message.channel, '거기써이!!')

    if message.content.startswith('뤼-김수미'):
        await client.send_message(message.channel, '칩(먹고싶다)')

    if message.content.startswith('뤼-심장'):
        await client.send_message(message.channel, '(심근경색)')

    if message.content.startswith('뤼-안즈땅'):
        await client.send_message(message.channel, '킄킄ㅋ킄 와타시노다로?')

    if message.content.startswith('뤼-졸려'):
        await client.send_message(message.channel, '오! 커피다! 원샷원샷워우엉샤샤샤샤')

    if message.content.startswith('뤼-일베'):
        await client.send_message(message.channel, '오빤..사실 메갈한다 뤼기야!')

    if message.content.startswith('뤼-메갈'):
        await client.send_message(message.channel, '오빤 사실 일베한다 뤼기야!')

    if message.content.startswith('뤼-강북멋쟁이'):
        await client.send_message(message.channel, '쟤 왜저래~;;')

    if message.content.startswith('뤼-왜'):
        await client.send_message(message.channel, '몰라')

    if message.content.startswith('뤼-노래'):
        await client.send_message(message.channel, '가랑!!!!눈아!!! 읶ㅆ지 레잇고! 레잇꼬! 마마...다드 다으(서해물과 날씨맑은상행선)')

    if message.content.startswith('뤼-오키'):
        await client.send_message(message.channel, '오끼잇!')

    if message.content.startswith('뤼-뤼기야!'):
        await client.send_message(message.channel, '오빤...한남이지만..나는너를 사랑해!')

    if message.content.startswith('뤼-히카킨'):
        await client.send_message(message.channel, '젠뚜맨~')

    if message.content.startswith('뤼-사랑'):
        await client.send_message(message.channel, '스러워||?????||')

    if message.content.startswith('뤼-추억'):
        await client.send_message(message.channel, '당신이 주었던..마더파더(의미심장)')

    if message.content.startswith('뤼-젠틀맨역사'):
        await client.send_message(message.channel, '잰')

    if message.content.startswith('뤼-임춘식'):
        await client.send_message(message.channel, '맨에사는 젠틀젠틀')

    if message.content.startswith('뤼-엔딩'):
        await client.send_message(message.channel, '함께해서 즐거웠고 다시 만나지 말자 하하ㅏ하하하하하ㅏㅎ')

    if message.content.startswith('뤼-만가설'):
        await client.send_message(message.channel, '몰라.')

    if message.content.startswith('뤼-명박'):
        await client.send_message(message.channel, '여러분 이거 다 싸이~!')

    if message.content.startswith('뤼-중딱'):
        await client.send_message(message.channel, '신나는 노?래~')

    if message.content.startswith('뤼-은뱅이'):
        embed = discord.Embed(title="은뱅이", description="", color=0xFF0000)
        embed.set_footer(text = "골뱅이 먹고 싶다.")
        embed.set_image(url="https://yt3.ggpht.com/a-/AAuE7mB_IB06eNN0piBdAfAYUxHslpKE1TNcV0MLLg=s288-mo-c-c0xffffffff-rj-k-no")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('노'):
        await client.send_message(message.channel, '노?신고합니다')

    if message.content.startswith('뤼-역할추가'):
        role = discord.utils.get(member.server.roles, name='Example ROle')
        await client.add_roles(member, role)
        


    





    


    


client.run('NTY2NDIyMjUzODI3MzkxNDk4.XLGnqg.SDAg3rSv7HPAkfrqE8LlqSiNrto')
