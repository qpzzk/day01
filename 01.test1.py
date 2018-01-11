import requests
#requests里面get方法传入网址url，向百度服务器发送请求完成http请求
#字典形式
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
response=requests.get('http://www.baidu.com',headers=headers)#里面还可以写User-Agent
print(response.text)
print(response.headers)
print(response.status_code)
