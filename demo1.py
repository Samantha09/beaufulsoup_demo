# beautifulsoup4_test.py

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">哈哈哈哈哈</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#创建 Beautiful Soup 对象
soup = BeautifulSoup(html, 'lxml')

#打开本地 HTML 文件的方式来创建对象
#soup = BeautifulSoup(open('index.html'))

#格式化输出 soup 对象的内容
# print (soup.prettify())

# 获取所有的p标签
# ps = soup.find_all("p")
# for p in ps:
#     print(p)
#     print("*" * 30)

# 获取第二个p标签
# ps = soup.find_all('p', limit=2)[1]
# print(ps)

# 获取class='title'的p标签
# ps = soup.find_all('p', attrs={"class":"title"})
# print(ps)

# 获取class, ip 等于规定值的标签
# ps = soup.find_all("a", attrs={"id":"link1", "class": "sister"})
# print(ps)

# 获取所有a标签的href属性
# aList = soup.find_all('a')
# for a in aList:
#     # 1.通过下表操作的方式：
#     href = a['href']
#     print(href)

# 获取标签中的文本信息
ps = soup.find_all('p')[1:]
for p in ps:
    aa = p.find_all('a')
    if len(aa) > 0:
        text = aa[0].string
        print(text)

p = soup.find_all('p')[1]
text = p.get_text()
print(text)

text = p.stripped_strings
print(text)

