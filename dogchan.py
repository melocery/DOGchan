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
    pattern1 = re.compile(r'学狗叫|學狗叫')
    pattern2 = re.compile(r'ruarua|摸摸|揉揉')
    pattern3 = re.compile(r'玩飞盘|玩飛盤')
    pattern4 = re.compile(r'选酒|選酒')
    pattern5 = re.compile(r'谢谢|謝謝')
    pattern6 = re.compile(r'帅|可爱|好看')
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

def ifreply(mastodon,notification):
    # check if we've already been participating in this thread
    post_id = notification['status']['id']
    try:
        context = mastodon.status_context(post_id)
    except:
        print("failed to fetch thread context")
        return False
    me = mastodon.account_verify_credentials()['id']
    posts = 0
    for post in context['descendants']:
        if post['account']['id'] == me and post['in_reply_to_id'] == post_id:
            return False
    return True

def autoreply(mastodon, since_id):
    notifications = mastodon.notifications(since_id)
    for noti in notifications:
        if noti['type'] != 'mention':
            continue
        if ifreply(mastodon, noti):
            process_mention(mastodon, noti)
        else:
            new_since_id = str(noti['id'])
            fo.write(new_since_id)
            return

fo = open("sinceid.txt", "w+")
since_id = fo.read()
autoreply(mastodon, since_id)
fo.close()
