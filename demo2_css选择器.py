from bs4 import BeautifulSoup

html = """
<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48816&amp;keywords=&amp;tid=87&amp;lid=0">25927-游戏测试经理</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-23</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48817&amp;keywords=&amp;tid=87&amp;lid=0">25927-游戏测试经理</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-23</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48811&amp;keywords=&amp;tid=87&amp;lid=0">CSIG15-翻译君机器学习高级工程师（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-03-23</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48806&amp;keywords=&amp;tid=87&amp;lid=0">22989-腾讯云高级运维工程师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-03-23</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48807&amp;keywords=&amp;tid=87&amp;lid=0">22989-运营开发高级工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-03-23</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48795&amp;keywords=&amp;tid=87&amp;lid=0">TME-QQ音乐社交Android开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>3</td>
					<td>深圳</td>
					<td>2019-03-23</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48800&amp;keywords=&amp;tid=87&amp;lid=0">31112-腾讯视频web前端开发工程师(北京)</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-03-23</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48790&amp;keywords=&amp;tid=87&amp;lid=0">PCG19-腾讯视频后台开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-23</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48791&amp;keywords=&amp;tid=87&amp;lid=0">PCG19-腾讯视频媒资后台开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-03-23</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=48789&amp;keywords=&amp;tid=87&amp;lid=0">PCG04-腾讯视频Web质量测试工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-03-23</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">1455</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a">2</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=20#a">3</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=30#a">4</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=40#a">5</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=50#a">6</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=60#a">7</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=70#a">...</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=1450#a">146</a><a href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </tbody>

<div>
我是div
</div>
<p>
<!--我是注释-->
</p>
"""

soup = BeautifulSoup(html, 'lxml')

# 1.获取所有的tr标签
def task1():
    trs = soup.select("tr")
    for tr in trs:
        print(tr)
        print("*" * 30)

# 2.获取第二个tr标签
def task2():
    tr = soup.select("tr")[1]
    print(tr)

# 3.选择class等于f的tr
def task3():
    trs = soup.select("tr.f")
    for tr in trs:
        print(tr)

# 获取所有href属性
def task4():
    aList = soup.select('a')
    for a in aList:
        href = a['href']
        print(href)

# 5.获取所有的职位信息
def task5():
    trs = soup.select("tr")
    for tr in trs:
        infos = list(tr.stripped_strings)
        print(infos)

def task6():
    soup = BeautifulSoup(html, 'lxml')
    p = soup.find('p')
    for x in p.stripped_strings:
        print(x)

if __name__ == '__main__':
    task6()