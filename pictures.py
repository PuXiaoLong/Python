# Python
The process of python learning.
import requests
import os
url = 'http://img0.dili360.com/rw5/ga/M00/45/C5/wKgBy1guyueAFg1vABWJTEejlTU417.tub.jpg'
root = 'c:/pics/'
path = root + url.split('/')[-1]
def get_pic():
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
            print('succeed')
    except:
        print('shit!')
if __name__ == '__main__':
    get_pic()
