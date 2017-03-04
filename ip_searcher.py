# Python
The process of python learning.
import requests
url = 'http://m.ip138.com/ip.asp?ip='
ip_number = '202.204.80.112'
def get_web():
    try:
        r = requests.get(url + ip_number)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('succeed!')
    except:
        print('shit!')
if __name__ == '__main__':
    i = 0
    while i < 100:
        get_web()
        i += 1
