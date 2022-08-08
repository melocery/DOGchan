import random
import string
from mastodon import Mastodon

mastodon = Mastodon(
        access_token = 'mybot_usercred.secret',
        api_base_url = 'https://musain.cafe',
    )

media_file = random.choice(open("path2selfie.txt").read().splitlines())
selfie =  mastodon.media_post(media_file)
content = '汪汪陪您度过最难熬的周三！'

mastodon.status_post(content, media_ids = selfie, visibility = 'public')
