# Python
The process of python learning.
import requests
url = 'https://item.jd.com/2384574.html'
def getweb( ):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[:1000])
    except:
        print('爬虫出现错误')
if __name__ == '__main__':
    getweb()
