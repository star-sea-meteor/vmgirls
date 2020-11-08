import requests
from bs4 import BeautifulSoup
import re

# 首先获取到图片的名称和指向链接
url = "https://www.vmgirls.com/wp-admin/admin-ajax.php"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
# 将 i 扔进 循环里，构造data
for i in range(2, 11):
    data = {"append": "list-archive",
            "paged": i,
            "action": "ajax_load_posts",
            "query": 18,
            "page": "cat"}
    # 提交请求头
    req = requests.post(url=url, data=data, headers=headers)
    # 构造soup对象
    soup = BeautifulSoup(req.text, "lxml")
    # find_all 方法获取所有符合条件的 a 标签
    result = soup.find_all("a", class_="media-content")
    # 把result扔进循环里，构造 r
    for r in result:
        # 解析，获得图片名称和 url
        name = r["title"]+".jpeg"
        link = r["style"]
        link1 = link[23:-2]
        # 下载图片
        img = requests.get(url=link1,headers=headers)
        # 保存至目录下
        with open(name,"wb") as f:
            f.write(img.content)