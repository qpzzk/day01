import http.cookiejar,urllib.request
filename="cookie.txt"
cookie=http.cookiejar.MozillaCookieJar()
cookie.load("cookie.txt",ignore_discard=True,ignore_expires=True) #读取cookie文件
handler=urllib.request.HTTPCookieProcessor(cookie)  #将读取的cookiehandler里
opener=urllib.request.build_opener(handler)
response=opener.open("https://mail.qq.com/")
print(response.read())