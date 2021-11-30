import discord
import requests
from random import randint
from discord.ext import commands
from datetime import datetime, timedelta
import os
from os import path
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix='/',help_command=None)

message_lastseen = datetime.now()
# Bot Token Taohu = input('Insert Token : ')

token = ('OTAyMTA0MzM3ODEwMDY3NDU5.YXZkIg.8REqslub1wnvCR3X8TEQF_LJhe8')

def randomText_Mention(target = "{0.author.mention}"):
    Words = ["ว่าไง?","อะไร?","ไม่สน","อย่ามายุ่ง","ลาก่อน","Leave me alone!!!!","สวย","เริ่ดมาก","เชิญห้องปกครอง","อ๊อยหย๋อ","ลาออก!","ไม่อ่าน ไม่ตอบ ไม่สน...",";w;","=A=!","- -*","แล้วไง?"
            ,"https://giphy.com/gifs/sad-cry-capoo-3og0IG0skAiznZQLde","https://giphy.com/stickers/cat-pearl-capoo-TFUhSMPFJG7fPAiLpQ"
            ,"OMG","มรีปัณหาร์อระไลห์หร่อส์","ขอเวลาอีกไม่นาน...","ขอเวลาอีกไม่นาน...*แค๊ก ๆ 8 ปีแล้ว*","แปป ๆ ไม่ว่าง","อุแงงงง","น้องบอทถูกใจสิ่งนี้","น้องบอทไม่ถูกใจสิ่งนี้","น้องบอทกดโกรธ :angry: สิ่งนี้","น้องบอทกดเลิฟ :heart: สิ่งนี้","ถึงโควิดจะทำให้โรงเรียนปิด แต่ยังมีดิสไว้แก้คิดถึงกัน"
            ,":notes: โรงเรียนของเราน่าอยู่~",":notes: เด็กเอ๋ยเด็กดี~",":notes: ดั่งไม้ยืนต้น~","ฉันจะฉาปแก","มะงื้ออออออ","แต่ความจริงคื๊อ...... ดาวมีไว้เบิ่ง~~",":notes: จากอีสานบ้านนามาอยู่กรุง จากแดนทุ่งลายยยยยยยย~"
            ,"แทงปลาไหล 20 ยก!","พิศวงวงวงวงวงวงวงวงวงวงวงวงวง","นั่นสิ","อิหยังวะ","เฮ็ดหยังหนิสู","สูกะดาย","อะไรกันครับเนี่ย!?","อะไรกันครับเนี่ย ผมงงไปหมดแล้ว","10 คะแนนเต็ม 10 คะแนนเต็มมมมมมมมมมมม!","แมสหมดแล้วค่ะ","ปังไม่หยุด","ปังมากแม่","ปังมาก"
            ,"หล่อนมีพิรุธ","ว่างมากหรอ","เหงาแหละดูออก","หรอจ๊ะ","จริงป๊ะจ๊ะ","แย่มาก","เยี่ยมมาก","เป็นแค่**เพื่อน**กันดีแล้ว","เพื่อนสนิทชุบแป้งทอด","ส้มหยุดดดดดด","#เด็กดีศรีมอดินแดง","...","ถถถถถ","555","55555+","555555555555","อืม","อ่า","หิว","ทำไม?","อือหื้อ","อิ๊วอิ๊ว อื้ออือ","เรียนไปทำไม..~ เรียนเพื่ออะไร...~","ตอนเรียนตั้งใจแบบนี้บ้างมั้ย","0-0","อุแวววววววววว","**Bhurrrrrr**","แตก 1","สวยพี่สวย","สยองงงงง","อ่าาาาาา","นะค่ะ"
            ,"ลำไยยยยยย","พักก่อน","หยุดจ่ะ หยุดจ่ะ ใด ๆ ก็คือลำไยเด้อ","ลำไย","อ๊ะเป่าาาา","ช่างแม่มั--- เอ้ย สนใจบ้างสิ ๆ","อะอะอะอ่าวอะอ่าวววว",":notes: หน่องนอนไม่ลั๊บ~","ภาพลักษณ์ชั้นกลายเป็นคนไม่ดี-อี","ออกจะดีออก","น้องกลับไปนอนนอนนะ","ยืมตังหน่อย","ไม่มีตังอะ","หนูอยากกลับบ้านนนนน","ออกไป!!!","Omae Wa Mou Shindeiru","Nani"
            ,"ว๊อดดดด","วายยยยยยยย","ว๊ายยยยยยยย","ฝันไป","-_____-?","อยากรวย","หนึ่งหนึ่งป่าวววววววววววววว","เดี๋ยวนี้เก่งขึ้นนะเราอะ","ว้ายยยยยยยย","เป็นแฟนกันมั้ย","เป็นแฟนกันมั้-- ไม่อะ เป็น**แค่คนคุยกับบอท**พอละ","เราชอบแก","เราชอบแก...ชอบแบบคนกับบอทคุยกัน","ทำไรอยู่อะ","เป็นห่วงนะ","ได้","ไม่","มันได้!","มันไม่ได้!","ทำไมหรอ?","ทำบุญบ้างนะ","ไปวัดมั้ย","เจอกันเวฬุวันนะ :full_moon_with_face:",":full_moon_with_face:",":new_moon_with_face:"
            ,"เศรษฐศาสตร์ต้องเรียนกับอาจารย์โม ถ้าอยากมีความรักโตๆต้องเรียนรู้กับน้องบอท","เหงาหงอยยยย","ไปกินข้าวแปป","ไว้คุยกันใหม่นะ","ไปอาบน้ำแปป","ไม่เอา","เกลียดดดดดดด","แต่..เรามีคนที่ชอบแล้วอะ","ทุกคนก็พูดแบบนี้","ใคร ๆ ก็ว่างั้นแหละ","ขอบคุณนะ","คนอย่างเธอ เป็นได้แค่บอทกับคนคุยแหละ","ระหว่างเราเป็นได้แค่บอทกับคนคุยเท่านั้นแหละ","ซู๊ดดดดดดดดดดดด","อื๊มมมมมมมม... อาหร่อยยยยยย","**นรก** is calling you.","**สวรรค์** is calling you.","เนื้อย่างกัน","ชาบูกัน"
            ,"อยากกินเนื้อย่าง เลี้ยงหน่อย","อยากกินชาบู เลี้ยงหน่อย","ไม่เอา!","เอา!","รักนะ แต่ไม่แสดงออก รักหลอก ๆ อย่ามาบอกว่ารัก","You got me feeling like a psycho, psycho","หยุดเถอะ","พักก่อน","https://youtu.be/rUAuEo3t0-o","รู้ว่าเหงา แต่เขาไม่กลับมาหรอก","ป๊าดดดดดดดดดดด","รู้ว่าเธอเหงา แต่เราไม่สนหรอก :P","ก็มาดิค้าบบบบบบบบบบ","ไม่ไหวละ","หมายเลขที่ท่านเรียกไม่สามารถติดต่อได้ในขณะนี้","หมายเลขที่ท่านเรียกไม่สามารถติดต่อได้ในขณะนี้*หรือ*เขาได้**บล็อก**คุณแล้วค่ะ"
            ,"คุณพี่อยู่จังหวัดอะไรคะ","คุณพี่อยู่จังหวัดอะไรค้าาาาาาาาา!!??","ณ จุดจุดนี้หนาคะะะะ","ปวดเฮ้ดดดดดดด","สตรองงงงงง","นี่ก็ขยี้จัง","อย่าให้รู้นะว่าแอบไปเล่นเกมส์หลังมอ","อย่าให้รู้นะว่าโดดซ้อมสแตน","อย่าให้รู้นะว่าแอบกินหนม ทำไมไม่แบ่งเราบ้าง","อย่าให้รู้นะว่าแอบกินหนม","เรื่องนี้ถึง","ห่วงมาก ทำไมไม่ถือเอาไว้ให้ดี ๆ เลือกเอาละกัน ถ้าไม่อยากเสียใจทีหลัง ก็รักษามันไว้ ตอนที่มีโอกาสอยู่ หรือจะเก็บมันขึ้นมาใหม่ เเต่มันก็ไม่เหมือนเดิมเเล้วนะ","https://giphy.com/gifs/capoo-cat-3ov9jZ0V6gOO0oa98Y","ช่วงนี้ระวังหน่อย...เห็นร้ายใครบ่อย ๆ"
            ,"https://giphy.com/gifs/meme-capoo-bugcat-JsVlBMEaHdOEGQKLXB","https://giphy.com/gifs/cat-capoo-bugcat-3o7bufrhglm1BTsfra","https://giphy.com/gifs/animation-capoo-bugcat-l4FGpa3DuEFMrghKE","https://giphy.com/gifs/capoo-3ov9jPBQ1UJRNS8MDe","https://giphy.com/gifs/wiggle-shaq-13CoXDiaCcCoyk","https://giphy.com/gifs/cat-humour-funny-ICOgUNjpvO0PC","https://giphy.com/gifs/minecraft-25oFarLxPqrNS","https://giphy.com/gifs/absurdnoise-halloween-4-5TOidpBAJBnQA"
            ,"เป็นปลื้มมมมมมมมมม","ว้าว","ว้าวววว","おまえ わ もう しんでいる","オラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラオラ","オラオラオラオラオラオラ","รู้นะว่าเหงา","รู้นะว่าเหงาแหละ ดูออก","เหงาแหละดูออก","คนไม่ดี","คนเฬว","คนดจีย์","ดจีย์~","คนดี","โรงเรียนเดียวกับเราเลย แต่ทำไมเราไม่เคยเห็นเธอเลยล่ะ","แกมาทำอะไรเอาตอนนี้","ไม่รักไม่ต้องมาแคร์ไม่ต้องมาดีกับฉัน","แกแหละ","เราแหละ","เขาแหละ","พวกเราแหละ","เธอแหละ","นายแหละ"
            ,"ถ้าเค้ารักแกจริง เค้าก็จะหาทางอยู่กับแกได้เองแหละ","No Comment","ถามว่าเรียนกี่โมง อยากจะไปส่ง ชิมิชิมิ","บอกเธอว่าไม่เป็นไร แต่ว่าในใจ ได้สิได้สิ","ฮัลโล่วววววว มีใครอยู่บ้างงงงงงงง","อย่าทำแบบนี้สิ","เด็กไม่ดี","ไม่ว่างจริง ๆ ~", "ละแมะ" , "ละแมะ ละไม่ว่างจริง ๆ อะหรือ อะหรือ อะหรือ อะหรือว่า","ไม่ว่างจริง ๆ อะหรือ อะหรือ อะหรือว่าเล่นเกมอยู่~","ไม่ว่างจริง ๆ อะหรือ อะหรือ อะหรือว่ามีคนคุยอยู่~", "ไม่ว่างจริง ๆ อะหรือ อะหรือ อะหรือว่ามีคนอื่น"
            ,"อะหรือ อะหรือ อะหรือ อะหรือว่า","ให้เธอ~ :rose:","ให้เธอ~ :v:","ให้เธอ~ :love_you_gesture:","เคยอม","ระหว่างเรามันคืออะไรเหรอ","พี่ชอบหมา ชอบแมว แล้วชอบหนูมั้ยคะ 🥺","Would you like coffee, tea or me?"]
    return Words[randint(0, len(Words)-1)] + f" {target}"

def randomImage_Mention(target = "{0.author.mention}"):
    Words = ["https://giphy.com/gifs/meme-capoo-bugcat-JsVlBMEaHdOEGQKLXB",
            "https://giphy.com/gifs/cat-capoo-bugcat-3o7bufrhglm1BTsfra",
            "https://giphy.com/gifs/animation-capoo-bugcat-l4FGpa3DuEFMrghKE",
            "https://giphy.com/gifs/capoo-3ov9jPBQ1UJRNS8MDe",
            "https://giphy.com/gifs/wiggle-shaq-13CoXDiaCcCoyk",
            "https://giphy.com/gifs/cat-humour-funny-ICOgUNjpvO0PC",
            "https://giphy.com/gifs/minecraft-25oFarLxPqrNS",
            "https://giphy.com/gifs/absurdnoise-halloween-4-5TOidpBAJBnQA",
            "https://giphy.com/gifs/sad-cry-capoo-3og0IG0skAiznZQLde",
            "https://giphy.com/stickers/cat-pearl-capoo-TFUhSMPFJG7fPAiLpQ"
    ]
    return Words[randint(0, len(Words)-1)] + f" {target}"

def randomKumKom_Mention(target = "{0.author.mention}"):
    Words = [
    
    ]
    return Words[randint(0, len(Words)-1)] + f" {target}"

def randomEmoji_Mention(target = "{0.author.mention}"):
    Words = ["🤔","😂","💩","👍","👀",":P","👍","😒","😜","🙄"]
    return Words[randint(0, len(Words)-1)] + f" {target}"

def randomText_Hello():
    Words = ["สวัสดีเจ้า","สวัสดีจ้า","สวัสดีครับ","สวัสดีค่ะ","ສະບາຍດີ","Annyeonghaseyo","Kon'nichiwa","Hello","привет!","ว่าไง",";w;?",
             "Meow Meooww?",":wave:","https://giphy.com/gifs/capoo-halloween-3ov9k0OmfNYeLdK4gg","Nǐ hǎo","วอล ที ที วอล ที","สวัสดีครั๊บบบบบบ!"]
    return Words[randint(0, len(Words)-1)] + " {0.author.mention}"

def download_url(url, directory = "__CACHE__"):
    if not os.path.exists(directory):
        os.mkdir(directory)
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise ValueError('Failed to download')

async def setBotName(bot, name):
    for GG in bot.guilds: #Make bot set itbot name on all server it join.
        await GG.me.edit(nick = name)

Guess_Num = {}

def Getname(bot,Id,Guild = None):
	if Guild == None:
		return bot.get_user(int(Id)).name
	else:
		Mininame = Guild.get_member(int(Id)).nick
		if Mininame != None:
			return bot.get_user(int(Id)).name+"(AKA. "+Mininame+")"
		return bot.get_user(int(Id)).name

@bot.event
async def on_ready():
    print('\nLogged in as ' + bot.user.name +" (" + str(bot.user.id) + ")\n------")
    await setBotName(bot,'🎃 Taohu')
    await bot.change_presence(activity=discord.Game(name='หนูยังทำอะไรได้ไม่มากนะคะ ~'))

async def on_member_join(bot, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'สวัสดีจร้าาาา {0.mention} สู่ {1.name}!\nขอให้สนุกกับเซิร์ฟเวอร์ของเรานะคะ :sparkling_heart: '.format(
            member, guild)
        await guild.system_channel.send(to_send)

async def on_member_remove(bot, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'หวังว่าเราจะได้พบกันน้าาาา  :pleading_face:  {0.mention}!'.format(member)
        await guild.system_channel.send(to_send)

@bot.command()
async def test(ctx):
    await ctx.channel.send("hello")

@bot.command()
async def shutdown(ctx):
    await ctx.channel.send('ไปก่อนนะคะ หวังว่าเราจะได้เจอกันอีก...')
    await bot.logout()

@bot.event 
async def on_message(message):
    global message_lastseen #ประกาศ message_lastseen
    if message.content.lower().startswith('/hello'):
        await message.channel.send(randomText_Hello().format(message))
        #Basic Codw

    elif message.content.lower().startswith('/help') or message.content.lower().startswith('!help'):
        em = discord.Embed(title="สิ่งที่น้องทำได้", description="มีแค่นี้แหละ")
        em.add_field(name="/help", value="ก็ที่ทำอยู่ตอนนี้แหละ")
        em.add_field(name="/hello", value="คำสั่งคนเหงา")
        em.add_field(name="/guest", value="ลองพิมพ์ดูสิ")
        await message.channel.send(content=None, embed=em)
        #Shuting Down Bot

    elif message.content.lower().startswith('/announce'):
        Mes_Str = message.content[len('/announce')+1:]
        channel = bot.get_channel(698217516392251393)
        if len(Mes_Str):
            await channel.send(("@everyone\n" + Mes_Str).format(message))
        if len(message.attachments):
            for attach in message.attachments:
                url = attach.url
                resFile = download_url(url)
                await channel.send(file=discord.File(resFile))
                os.remove(resFile)
            await message.delete()

    elif message.content.lower().startswith('/say'):
        Mes_Str = message.content[len('/say')+1:].split(" ")
        bot_channel_id = message.channel.id
        start_search_message = 0
        if "<#" in Mes_Str[0] and ">" in Mes_Str[0]:
            bot_channel_id = int(Mes_Str[0].replace("<#","").replace(">",""))
            start_search_message = 1            
        bot_send_message = Mes_Str[start_search_message::]
        bot_message = ""
        for c in bot_send_message:
            bot_message += c + " "
        channel = bot.get_channel(bot_channel_id)
        empty_message = bot_message.replace(" ","")
        if empty_message:
            await channel.send((bot_message).format(message))
        if len(message.attachments):
            for attach in message.attachments:
                url = attach.url
                resFile = download_url(url)
                await channel.send(file=discord.File(resFile))
                os.remove(resFile)
        await message.delete()
        print("message from bot.event")

    elif message.content.lower().startswith('/guest'):
        namae = str(message.author.id)
        GUILD = None
        try:
            GUILD = message.channel.guild
        except:
            pass
        
        await message.channel.send("Minigame By **Nepumi**\n\n:crossed_swords:**โห๋ 1-1 ได้ครับเจ้า"+Getname(bot,namae,GUILD)+"**:crossed_swords:\n" + \
                ":1234:วิธีการเล่นคือ ข้าจะ**คิดเลขหนึ่งตัวตั้งแต่ 1 ถึง 100**\nเจ้าต้องทายเลขของค่าให้ถูก**ภายใน 7 ครั้ง**\nสามารถทายโดยการ `? <ตัวเลข>` เช่น `? 12`\n" + \
                ":arrow_down:ถ้าเลขที่เจ้าตอบมัน**ต่ำกว่า** ข้าก็จะบอก**ต่ำไป** \n:arrow_up:แต่ถ้าเลขเจ้ามัน**สูงไป** ข้าก็จะบอก **สูงไป** \n:white_check_mark:แต่ถ้าถูก ข้าจะบอกว่าถูกเอง\n:x:ถ้าเจ้ากลัวที่จะแพ้ข้าก็สามารถออกได้โดยการ `? *` เอา หึๆๆๆ" \
                )

        NEW = {"Time" : 0,"Troll" : randint(0,2) == 0,"TrollSeq" : False,"ANS" : randint(1,100)}
        Guess_Num[namae] = dict(NEW)

    elif message.content.lower().startswith('? '):
        namae = str(message.author.id)
        GUILD = None
        try:
            GUILD = message.channel.guild
        except:
            pass

        if namae in Guess_Num:
            Mes_Str = message.content[len('? '):]
            if Mes_Str.startswith('*'):
                await message.channel.send(":x:เจ้ายอมแพ้สินะ "+Getname(bot,namae,GUILD))
                await message.delete()
                Guess_Num.pop(namae,None)
            else:
                LEK = 0
                try:
                    LEK = int(Mes_Str)
                except:
                    Guess_Num[namae]["Time"]+= 1
                    if Guess_Num[namae]["Time"] == 7:
                        await message.channel.send(":question:ข้าไม่รู้นะว่าเจ้าส่งอะไรมา("+Mes_Str+") แต่ตอนนี้เจ้าแพ้แล้ว... "+Getname(bot,namae,GUILD)+"\nเฉลยคือ "+str(Guess_Num[namae]["ANS"]))
                        await message.delete()
                        Guess_Num.pop(namae,None)
                    else:
                        await message.channel.send(":question:ข้าไม่รู้นะว่าเจ้าส่งอะไรมา("+Mes_Str+") แต่เหลือ: **"+str(7-Guess_Num[namae]["Time"])+" ครั้ง**นะเจ้า "+Getname(bot,namae,GUILD))
                        await message.delete()
                    return
                Guess_Num[namae]["Time"]+= 1
                if LEK > Guess_Num[namae]["ANS"]:
                    if Guess_Num[namae]["Time"] == 7:
                        if Guess_Num[namae]["Troll"] and Guess_Num[namae]["TrollSeq"]:
                            await message.channel.send(":white_check_mark:ข้าล้อเล่นๆๆ จริงๆ"+str(Guess_Num[namae]["ANS"])+"มันถูกละ555 เจ้าชนะนะ "+Getname(bot,namae,GUILD))
                            await message.delete()
                        else:
                            await message.channel.send(":x:"+Mes_Str+"น่ะ**มันสูงเกิน**... เจ้าแพ้แล้ว "+Getname(bot,namae,GUILD)+"\nเฉลยคือ "+str(Guess_Num[namae]["ANS"]))
                            await message.delete()
                        Guess_Num.pop(namae,None)
                    else:
                        await message.channel.send(":arrow_up:"+Mes_Str+"น่ะ**มันสูงเกิน**... เหลือ: **"+str(7-Guess_Num[namae]["Time"])+" ครั้ง**นะเจ้า "+Getname(bot,namae,GUILD))
                        await message.delete()
                elif LEK < Guess_Num[namae]["ANS"]:
                    if Guess_Num[namae]["Time"] == 7:
                        if Guess_Num[namae]["Troll"] and Guess_Num[namae]["TrollSeq"]:
                            await message.channel.send(":white_check_mark:ข้าล้อเล่นๆๆ จริงๆ"+str(Guess_Num[namae]["ANS"])+"มันถูกละ555 เจ้าชนะนะ "+Getname(bot,namae,GUILD))
                            await message.delete()
                        else:
                            await message.channel.send(":x:"+Mes_Str+"ของเจ้าน่ะ**มันต่ำเกิน**... เจ้าแพ้แล้ว "+Getname(bot,namae,GUILD)+"\nเฉลยคือ "+str(Guess_Num[namae]["ANS"]))
                            await message.delete()
                        Guess_Num.pop(namae,None)
                    else:
                        await message.channel.send(":arrow_down:"+Mes_Str+"ของเจ้าน่ะ**มันต่ำเกิน**... เหลือ: **"+str(7-Guess_Num[namae]["Time"])+" ครั้ง**นะเจ้า "+Getname(bot,namae,GUILD))
                        await message.delete()
                elif LEK == Guess_Num[namae]["ANS"]:
                    if Guess_Num[namae]["Troll"]:
                        if Guess_Num[namae]["Time"] == 7:
                            await message.channel.send(":arrow_up:"+Mes_Str+"ของเจ้าน่ะ**มันสูงเกิน**... ข้าล้อเล่น \n:white_check_mark:**"+Mes_Str+"**น่ะถูกแล้วนะ... เจ้า "+Getname(bot,namae,GUILD))
                            await message.delete()
                            Guess_Num.pop(namae,None)
                        else:
                            await message.channel.send(":arrow_up:"+Mes_Str+"ของเจ้าน่ะ**มันสูงเกิน**... เหลือ: **"+str(7-Guess_Num[namae]["Time"])+" ครั้ง**นะเจ้า "+Getname(bot,namae,GUILD))
                            await message.delete()
                            Guess_Num[namae]["TrollSeq"] = True
                    else:
                        await message.channel.send(":white_check_mark:ถถถถถูกต้อง ตัวเลขข้าคือ "+Mes_Str+" เก่งไม่เบาเลยนะเจ้า "+Getname(bot,namae,GUILD))
                        await message.delete()
                        Guess_Num.pop(namae,None)

    for Mem in message.mentions:
        if bot.user.name == Mem.display_name:
            if "ตารางสอบ" in message.content:
                await message.channel.send("ตอนนี้ยังไม่ใกล้สอบ... แต่ก็อย่าลืมทำการบ้านแล้วก็อ่านหนังสือด้วยนะคะ!")
            elif "โดเนท" in message.content:
                await message.channel.send("สามารถโดเนทได้ที่".format(message))
                await message.channel.send("- Promptpay: `0611125412`".format(message))
                await message.channel.send("- True Wallet: `0611125412`".format(message))
            elif "ตารางเรียน" in message.content:
                await message.channel.send("เอาไปเลยค่าาา จัดตารางเรียนด้วยหละ https://drive.google.com/drive/folders/1c_ZhG_JjkByLfmPMefcD33VaPGB2jpS0".format(message))
            elif "หวย" in message.content:
                await message.channel.send(f"อืมมมม..... เอาเป็นเลข {randint(0, 100):02d} ละกันน้าา หวังว่าจะถูกนะ")
            elif "ชื่ออะไร" in message.content:
                await message.channel.send(f"หนูชื่อเต้าหู้ค่ะ  จำให้ด้วยหละ!")
            elif "รูป" in message.content:
                await message.channel.send(randomImage_Mention().format(message))
            elif "แต้ม" in message.content:
                await message.channel.send(randomEmoji_Mention().format(message))
            elif "คำคม" in message.content:
                await message.channel.send(randomEmoji_Mention().format(message))
            else:
                await message.reply(randomText_Mention().format(message))
            break

    await bot.process_commands(message) #มีอธิบายสอนทำ Discord pot EP:3 





bot.run(token)
#insert bot Token Hear! ^^^