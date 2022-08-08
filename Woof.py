from mastodon import Mastodon, StreamListener
from bs4 import  BeautifulSoup
from multiprocessing import Pool
import os, random, re, json, re, sys, html

def extract_toot(toot):
    toot = toot.replace("&apos;", "'") #convert HTML stuff to normal stuff
    toot = toot.replace("&quot;", '"') #ditto
    soup = BeautifulSoup(toot, "html.parser")
    for lb in soup.select("br"): #replace <br> with linebreak
        lb.insert_after("\n")
        lb.decompose()
    for p in soup.select("p"): #ditto for <p>
        p.insert_after("\n")
        p.unwrap()
    for ht in soup.select("a.hashtag"): #make hashtags no longer links, just text
        ht.unwrap()
    for link in soup.select("a"): #convert <a href='https://example.com>example.com</a> to just https://example.com
        link.insert_after(link["href"])
        link.decompose()
    text = soup.get_text()
    text = re.sub("https://([^/]+)/(@[^ ]+)", r"\2@\1", text) #put mastodon-style mentions back in
    text = re.sub("https://([^/]+)/users/([^ ]+)", r"@\2@\1", text) #put pleroma-style mentions back in
    text = text.rstrip("\n") #remove trailing newline
    # text = re.sub(r"^@[^@]+@[^ ]+\s*", r"", text) #remove the initial mention
    text = text.lower() #treat text as lowercase for easier keyword matching
    return text

# 学狗叫
def WangWang():
    lessons_list = {'汪汪现在不想上课！放假！':5,
                    '这次的课程是撒娇小狗怎么叫 —— 闭上嘴巴，从喉咙深处发出介于 ‘哼’ 和 ‘嘤’ 之间的音，hing~hing~':14,
                    '这次的课程是傲娇小狗怎么叫 —— 配合眼神，发出一声不长不短又有下坠感的 ‘哼ing’，大家就都知道你在傲娇啦！':14,
                    '这次的课程是愤怒小狗怎么叫 —— 先从胸腔发出一声低沉的 ‘呜’，再连续三声响亮的 ‘汪’，村口大黄都能知道小狗在发怒！':14,
                    '这次的课程是生气小狗怎么叫 —— 呲牙，从牙缝中挤出气气的 ‘嘶——’！':14,
                    '这次的课程是开心小狗怎么叫 —— 放轻松，发出清脆的介于 ‘啊’ 和 ‘汪’ 之间的音，aang！aang！还要记得摇尾巴！':15,
                    '这次的课程是威严小狗怎么叫 —— 深呼吸，从胸腔发出自信又低沉的 ‘呜—— 呜——’，能把隔壁小比吓跑哦！':14,
                    '这次的课程是疲惫小狗怎么叫 —— 闭上嘴巴，轻轻发出一声长长的 ‘哼’，记得要带上有气无力的颤音！':14,
                    '这次的课程是困困小狗怎么叫 —— 困困小狗当然是睡觉！':10
    }
    value_list = []
    for key, value in lessons_list.items():
        value_list += value*[key]
    lesson = random.choice(value_list)
    return lesson

# 摸摸小狗
def RuaRua():
    Rua_list = {'汪汪来啦，不摸够十分钟是不会走的！':19,
                '汪汪飞奔到你脚边，贴贴！':19,
                '汪汪在你身边趴下，随便摸！':19,
                '汪汪决定把肚皮借给你一分钟！':19,
                '汪汪探出狗头，摸摸小狗头，什么都不愁！':19,
                '汪汪从你身边快乐跑过，没有给你摸摸的机会！':5,
    }
    value_list = []
    for key, value in Rua_list.items():
        value_list += value*[key]
    Rua = random.choice(value_list)
    return Rua

# 玩飞盘
def PlayFP():
    num = random.randint(0,10)
    if num == 0:
        content = '很可惜，汪汪没有追上飞盘，你的飞盘捡不回来啦！'
    elif num > 5:
        n = num - 5
        content = '汪汪不但捡回了你的飞盘，还在草坪上发现了' + str(n) + '个无主飞盘，请你帮我送给其它小狗吧！'
    else:
        content = '汪汪不但捡回了你的飞盘，还在草坪上发现了' + str(num) + '个无主飞盘，请你帮我送给其它小狗吧！'
    return content

# 选酒
def PickDrink():
    drink_list = [' :vha_Beer: ',' :vha_Bleeding_Jane: ',' :vha_BloomLight: ',
                ' :vha_BlueFairy: ',' :vha_Brandtini: ',' :vha_Cobalt_Velvet: ',
                ' :vha_CreviceSpike: ',' :vha_FlamingMoai: ',' :vha_Fluffy_Dream: ',
                ' :vha_Fringe_Weaver: ',' :vha_Froth_Water: ',' :vha_GrizzlyTemple: ',
                ' :vha_GutPunch: ',' :vha_Marsblast: ',' :vha_Mercuryblast: ',
                ' :vha_Moonblast: ',' :vha_Piano_Man: ',' :vha_Piano_Woman: ',
                ' :vha_Pile_driver: ',' :vha_SparkleStar: ',' :vha_SugarRush: ',
                ' :vha_SunshineCloud: ',' :vha_Suplex: ',' :vha_vha_Bad_Touch: ',' :vha_Zen_Star: ']
    d_flag = random.randint(0, len(drink_list)-1)
    drink = drink_list[d_flag]
    d = drink.split(':vha_')[1]
    content = '汪汪为您选的酒是 ' + d + drink + '！'
    return content

