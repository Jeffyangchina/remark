import requests
from bs4 import BeautifulSoup
headrs ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)/' \
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
}
test='http://home.yiguo.com/Trade/UMoney'
base_url = 'http://www.yiguo.com'
login_url = 'http://www.yiguo.com/Handler/getusername?datestamp=1507690693842&_=1507690693843'
sign_url = 'http://www.yiguo.com/?RndNumber=50625'
login_data = {
    'UserName':'13501630376',
    'Pwd':'yang1230',
 #   'VerifyCode':
}
s = requests.Session()
r = s.get(login_url,headers=headrs)
print(r.cookies)
print(r.status_code)
res = s.post(sign_url, login_data,headers=headrs,cookies=r.cookies)
print(res.status_code)
print(res.content)
#soup = BeautifulSoup(r, 'html.parser')
#_csrf = soup.find(attrs={'name':'csrf-token'})['content']