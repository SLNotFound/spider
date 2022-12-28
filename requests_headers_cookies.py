# -*- coding: utf-8 -*-
# @Time: 2022/12/20 13:54
# @Author: grape
# @File: requests_headers_cookies.py

import requests

url = 'https://github.com/login'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
cookies_str = '_octo=GH1.1.179875971.1671587632; preferred_color_mode=light; tz=Asia%2FShanghai; _device_id=4737e3369b9351b7147a03e954f58430; has_recent_activity=1; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; user_session=akC9NdKiET1yqQZn9HAXF9GJzZoPasMeqYplU8t2JJonweE6; __Host-user_session_same_site=akC9NdKiET1yqQZn9HAXF9GJzZoPasMeqYplU8t2JJonweE6; logged_in=yes; dotcom_user=SLNotFound; _gh_sess=l%2F%2BkgwIdZDTc9JL9b0Ndz97WicfbUliDcHMRBmQUPE%2BusFAGb0niMFhQkcyzrIicN4P1UDj6sXS9DADTgo9D6bxF2%2FoPJ%2BB1nLNVVXnXTjJxsGTjFWRhz9LMBpiz2edJiPQh28xQz%2F4BNhUG4kZqNBdY1fIMtPYiUCdhpAYHwK4IxtaCPqyATUsWTDJXLBc%2Bt25ZiKq%2BASRlDcBP8bxnXuT0DmoZjMrpny%2FIPLG3V0JC4zRGf2%2F7wK7v1VB5lGJK1Jc0NBzi%2FNO4iDf1DiwmFqPkF9RVCZuKbFbkKroRsoTtyVrJIqZGHGv7JODWOJvIRis5psgHaevOUsOwbm2R7q1DjGNBhcN09Kc62%2BAJIJWZ4aM5SQvNYL9rdyN4X9TQBlYgcZwBOrPNRaNWRTzbFMt3%2BHGbTa4EL5F%2BH2J64B0JCURm3mxME9ZXs4IWoH6HdjtJVg%2Fd%2FsRlmECThZlKqwV2Y%2FtZHhX3XsMtBc6ZPyrRkMs53Nl1M%2Bbf1XoKfVP3aNTbHkJfRPI%2FI4Dja3NRLNSp24A1xlCE1%2FlxGfWJ0GZ0cewZw4Spwla0lhHlG5ndM%2FaRhv2Z7jEBsY1i9jZCTtO8jG%2FHjdVvq8NGh9%2BUE0CDtxf29ro1Kc3r9ACaDs%2FLsTzBjm6l5MZNTjmWdnwL%2Bk2B1OJ0KPg8woIRRT0xdzuD6Yc9FNOneKqb9Pwlw5B4AdtKtabZDnbyqwAqdEMSw5cR%2FNzkbt23s4ZCJuIuMunboMvI5WXAYuu3Ww6ubV%2B9c4TzpQ%3D%3D--VgtSEk0cLKA0JcDG--r0xwEcX7FNe6yZbA4CD8Kg%3D%3D'
cookies_dit = {cookie.split('=')[0]:cookie.split('=')[-1] for cookie in cookies_str.split('; ')}

session = requests.session()

response = session.get(url, headers=headers,)
with open('request_with_cookies.html', 'wb') as f:
    f.write(response.content)
