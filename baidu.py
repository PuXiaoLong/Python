# Python
The process of python learning.
import requests
kv = {'wd':'Python'}
url = 'http://www.baidu.com/s'
def get_web():
    try:
        r = requests.get(url,params = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[-1000:])
    except:
        print('ERROR')
if __name__ == '__main__':
    get_web()
