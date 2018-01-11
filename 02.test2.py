import requests

response=requests.get('https://pic.bb164.com/d6/3389/338955-11.jpg')
print(response.content)
with open('/home/zzk/zzk_project/1.jpg','wb') as f:
    f.write(response.content)
    f.close()
