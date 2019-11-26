import requests


params= {"#q":"pizza"}
r=requests.get("http://google.com" , params=params)
r.url
print("status is:", r.status_code)
print(r.url)
print(r.cookies)
print(r.text)

f=open("./page.html", "w+")
f.write(r.text)