# DOGchan：一个能够关键字触发自动回复的 Mastodon bot

## Summary
为实现咖啡馆猫狗双全而诞生的可以根据关键词触发相应自动回复的长毛象机器人 —— DOGchan，又叫汪汪 (以下提到会用汪汪代替)。  
@汪汪 并在嘟文中提到关键词，即可得到汪汪的回复，回复可见范围与原嘟可见范围一致。关键词列表如下：  

|  关键词   | 回复  |
|  ----  | ----  |
| 玩飞盘 / 玩飛盤  | 汪汪将捡回您扔的飞盘 |
| 学狗叫 / 學狗叫  | 汪汪将教您一种狗叫 |
| ruarua / 摸摸 / 揉揉  | 汪汪将让您摸摸 |
| 选酒 / 選酒 | 汪汪将为您选择一种酒 |

除此以外，汪汪会在北京时间每周三上午九点自动发送一张狗狗照片，陪您度过最难熬的周三。  

DOGchan (also called Wangwang) is an autoreply mastodon bot. It will toot a dog photo every Wednesday, and autorespond the toot which mentions it and contains the keywords.   
Language support: only Chinese for now.  

## Reference
DOGchan 的代码部分来源于 mastodon-bot-template，并参考了 mstdn-ebooks 和 Mastodon.py。  
Mastodon.py: [Docs](https://mastodonpy.readthedocs.io/en/stable/index.html#) , [GitHub](https://github.com/halcy/Mastodon.py)  
mastodon-bot-template: [reply.py](https://github.com/Lynnesbian/mastodon-bot-template/blob/9e72f6a490734f7af5897c40f20b4aecb0c2308b/reply.py)  
mstdn-ebooks: [reply.py](https://github.com/Lynnesbian/mstdn-ebooks/blob/master/reply.py)

## Install
### bot 账号
选择一个合适的站点注册 bot 账号，并修改资料，注意选中 “这是一个 bot 账号 / This is a bot account”。  
在管理面板找到开发/Development-创建新应用/New Application，创建新应用并给予读写权限，复制访问令牌。 

### 安装汪汪 bot
在服务器合适的位置进行如下操作：  

```bash
  git clone https://github.com/melocery/CATsama.git
  cd CATsama
  conda create -n mastbot python=3.8
  conda activate mastbot
  pip3 install requests beautifulsoup4 Mastodon.py
```

编辑 `mybot_usercred.example`，将复制的访问令牌粘贴到文件中，重命名文件为 `mybot_usercred.secret`。  

## Usage
### 自动发嘟
使用命令：  

```
  python selfie.py
```

即可实现发送一条带有图片的嘟嘟。  
如果需要将该命令设置为定时任务，则可使用：  

```
    0 9 * * 3  cd /root/miniconda/dogchan && /root/miniconda3/envs/mastbot/bin/python selfie.py >> /root/miniconda/dogchan/log/selfie_log.txt 2>&1
```

即可在每周三上午九点发送一条带有图片的嘟嘟。  

### 自动回复
手动运行脚本：  

```
  python dogchan.py
```

即可启动关键词触发的自动回复，Ctrl C、或关闭 Terminal、服务器都会停止运行。  
可使用 systemd 自动运行脚本。编辑 `systemd-example.service`，并存放在合适的文件夹即可。  
