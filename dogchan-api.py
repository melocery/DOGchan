from mastodon import Mastodon, StreamListener
from bs4 import  BeautifulSoup
from multiprocessing import Pool
import os, random, re, json, re, sys, html
import Woof

mastodon = Mastodon(
    access_token = 'mybot_usercred.secret',
    api_base_url = 'https://musain.cafe',
)

def process_mention(mastodon, notification):
    acct = "@" + notification['account']['acct'] #get the account's @
    print("mention detected")
    post = notification['status']
    mention_text = Woof.extract_toot(post['content'])
    print(mention_text)
    visibility = post['visibility']
    # mention_text = extract_toot(nfcts[0]['status']['content'])
    # pattern1 = re.compile(r'照片|自拍')
    # if pattern1.search(mention_text):
    #     media_file = random.choice(open("path2selfie.txt").read().splitlines())
    #     selfie =  mastodon.media_post(media_file)
    #     content = acct + ' '
    #     mastodon.status_post(
    #         status = content, # the toot you'd like to send
    #         in_reply_to_id = post['id'], # the post you're replying to
    #         media_ids = selfie,
    #         visibility=visibility 
    #     )
    pattern1 = re.compile(r'学狗叫|學狗叫')
    pattern2 = re.compile(r'ruarua|摸摸|揉揉')
    pattern3 = re.compile(r'玩飞盘|玩飛盤')
    pattern4 = re.compile(r'选酒|選酒')
    pattern5 = re.compile(r'谢谢|謝謝')
    pattern6 = re.complie(r'帅|可爱|好看')
    if pattern1.search(mention_text):
        print("Woof!")
        content = acct + ' ' + Woof.WangWang()
        mastodon.status_post(
            status = content, # the toot you'd like to send
            in_reply_to_id = post['id'], # the post you're replying to
            visibility=visibility
        )
    elif pattern2.search(mention_text):
        print("Rua!")
        content = acct + ' ' + Woof.RuaRua()
        mastodon.status_post(
            status = content,
            in_reply_to_id = post['id'],
            visibility=visibility
        )
    elif pattern3.search(mention_text):
        print("PlayFP!")
        content = acct + ' ' + Woof.PlayFP()
        mastodon.status_post(
            status = content,
            in_reply_to_id = post['id'],
            visibility=visibility
        )
    elif pattern4.search(mention_text):
        print("PickDrink!")
        content = acct + ' ' + Woof.PickDrink()
        mastodon.status_post(
            status = content,
            in_reply_to_id = post['id'],
            visibility=visibility
        )
    elif pattern5.search(mention_text):
        print("thanks!")
        content = acct + ' ' + '汪汪爱你！'
        mastodon.status_post(
            status = content,
            in_reply_to_id = post['id'],
            visibility=visibility
        )
    elif pattern6.search(mention_text):
        print("Kuakua!")
        content = acct + ' ' + '你是在夸汪汪吗？谢谢，汪汪爱你！'
        mastodon.status_post(
            status = content,
            in_reply_to_id = post['id'],
            visibility=visibility
        )
    else:
        print("Wang don't understand!")
        content = acct + ' ' + '汪汪不明白你在说什么，但决定让你摸摸！'
        mastodon.status_post(
            status = content,
            in_reply_to_id = post['id'],
            visibility=visibility
        )

class ReplyListener(StreamListener):
    def on_notification(self, notification): #listen for notifications
        if notification['type'] == 'mention': #if we're mentioned:
            process_mention(mastodon, notification)

# create a new instance of our ReplyListener class
rl = ReplyListener()
mastodon.stream_user(rl) #go!

