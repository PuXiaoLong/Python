# Python
The process of python learning.
import requests
url = 'https://www.amazon.cn/dp/B017DOUQOK/ref=asw1_0078d366-376f-3523-98e9-a9350d2e221d_1_1082_KINDLE/455-2878440-9470435?pf_rd_p=2d517837-6cff-4486-a5cd-130d80da0d7b&pf_rd_s=desktop-takeover&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=7MDM9DHEY0CSWQ1DVQPQ&pf_rd_r=7MDM9DHEY0CSWQ1DVQPQ&pf_rd_p=2d517837-6cff-4486-a5cd-130d80da0d7b'
kv = {'user-agent':'Mozilla/5.0'}
def getweb():
    try:
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[:1000])
    except:
        print('shit there is a error')
if __name__ == '__main__':
    getweb()
