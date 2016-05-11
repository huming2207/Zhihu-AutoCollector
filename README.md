# Zhihu-AutoCollector
一个基于Python的多线程的知乎爬虫+按关键字词自动收藏工具

### 使用方法
使用前请在***keyword.txt关键词列表***设置关键词，每行一个。

用本工具登录后，它会自动爬取你关注的人的点赞和回答，并将命中关键词列表的回答帖子加入指定收藏中。

### 依赖
7sDream大神的zhihu-oauth；
ThreadPool多线程库（自带）。

### 输出结果

```
/usr/local/bin/python3 /Users/Jackson/Documents/projects/Zhihu-AutoAnalyzer/main.py
----- Zhihu OAuth Login -----
email: ********@gmail.com
password: **********

Need for a captcha, getting it......
Please open /Users/Jackson/Documents/projects/Zhihu-AutoAnalyzer/captcha.gif for captcha
captcha: ****
Login success.
Name: 测试一下


 Keywords are:


['苟利国家生死以', '岂因祸福避趋之', '历史的行程', '蛤蛤', 'I would like speak few words', 'I think I speak very poor English', '钦点', '内定', '硬点', '我蛤', '长者', '最吼', '吼啊', '坠吼', '鸭嘴笔', '见着风是得雨', '无可奉告', 'too young', 'too simple', 'sometimes naive', 'naive', 'naïve', "I'm angry", '大新闻', '+1s', '效率efficiency', '几百个教授一致通过', 'excited', 'Excited', '三个代表', '军队一律不得经商', '军队经商', '军队不得经商', '赛艇', '续命', '续一秒', '续秒', '红衣', '难再续', '香港记者', '谈笑风生', '西方哪个国家', '华莱士']



Follower ID:  1c7f429366f5db6b3cf05e2b6eaac0a9
Follower ID:  e9d107d95d1f518e4ab2f321ec7603d1
Follower ID:  266234b44facbd71869d9a2dc454037b
Follower ID:  df4e3b2fbffecc191bb394de8c2d4f77
Follower ID:  75664e0c053db655bd4a1ffc1d335ea8
Follower ID:  9ce96ea7174a8665540e7eb74f9db9a1
Follower ID:  f04f2cf01a1c1a87df7bab3b95314ed3
Found  于雅枫 's answer ID: 97199771 , with keyword  红衣
Found  于雅枫 's answer ID: 97199771 , with keyword  难再续
Found  Summer Clover 's answer ID: 99512799 , with keyword  大新闻
Found  小王子 's answer ID: 66188227 , with keyword  大新闻
Found  贺仙 's answer ID: 98465211 , with keyword  蛤蛤
Found  王不二 's answer ID: 84432832 , with keyword  谈笑风生
Found  Ran dom 's answer ID: 60548921 , with keyword  三个代表
Found  陈阿直 's answer ID: 90390432 , with keyword  too young
Found  大简木一乐 's answer ID: 39356889 , with keyword  长者
Found  匿名用户 's answer ID: 93620547 , with keyword  +1s
Found  黑则明 's answer ID: 97940687 , with keyword  长者
Found  黑则明 's answer ID: 97940687 , with keyword  坠吼
Found  黑则明 's answer ID: 97940687 , with keyword  赛艇
Found  李鹏 's answer ID: 96222634 , with keyword  naive
Found  李鹏 's answer ID: 96222634 , with keyword  赛艇
Found  贺仙 's answer ID: 64481120 , with keyword  excited
Found  闲人王氏 's answer ID: 91897974 , with keyword  大新闻
Found  匿名用户 's answer ID: 93854386 , with keyword  +1s
Found  王冶坪 's answer ID: 95874827 , with keyword  +1s
Found  Hermite Bai 's answer ID: 81052112 , with keyword  军队一律不得经商
Found  于雅枫 's answer ID: 69683949 , with keyword  谈笑风生
Found  Ross 李 's answer ID: 79540035 , with keyword  赛艇
Found  高潮 's answer ID: 87361321 , with keyword  见着风是得雨
Found  高潮 's answer ID: 87361321 , with keyword  三个代表
Found  李少荃 's answer ID: 94901410 , with keyword  三个代表
Found  高潮 's answer ID: 87361321 , with keyword  军队经商
Found  彭路遥 's answer ID: 76623614 , with keyword  赛艇
Found  NE恶灵 's answer ID: 91853834 , with keyword  吼啊
Found  贺仙 's answer ID: 77132771 , with keyword  赛艇
Found  张兆杰 's answer ID: 63050233 , with keyword  大新闻
Found  天下之水 's answer ID: 89713352 , with keyword  无可奉告
Found  杨嘉煜 's answer ID: 87431899 , with keyword  谈笑风生
Found  夏木 's answer ID: 89535638 , with keyword  大新闻
Found  千古留名 's answer ID: 85213074 , with keyword  历史的行程
Found  邓涵 's answer ID: 52715937 , with keyword  红衣
Found  Hannibal Lecter 's answer ID: 91022943 , with keyword  谈笑风生
Found  阿五 's answer ID: 93066628 , with keyword  naive
Follower ID:  e74a18105bd4610298f6402010da09c4
Found  凯常 's answer ID: 72185884 , with keyword  长者
Found  yalding 's answer ID: 76364092 , with keyword  红衣
Found  路人乙食肉馒 's answer ID: 74273573 , with keyword  谈笑风生
Found  Lee General 's answer ID: 53279255 , with keyword  长者
Found  vczh 's answer ID: 84807466 , with keyword  excited
Found  匿名用户 's answer ID: 63014334 , with keyword  长者
Found  温义飞 's answer ID: 84028357 , with keyword  红衣
Found  楚歌 's answer ID: 96297104 , with keyword  历史的行程
Found  凤红邪 's answer ID: 84253765 , with keyword  谈笑风生
Found  凤红邪 's answer ID: 84253765 , with keyword  华莱士
Found  恶喵的奶爸 's answer ID: 54016601 , with keyword  excited
Found  王不二 's answer ID: 84432832 , with keyword  谈笑风生
Found  Moxos Yuri 's answer ID: 94256572 , with keyword  长者
Found  项木咄 's answer ID: 93064927 , with keyword  大新闻
Found  和彩 's answer ID: 16424385 , with keyword  too young
Found  狐照尾 's answer ID: 99496798 , with keyword  坠吼
Found  苏穆羽 's answer ID: 84223770 , with keyword  大新闻
Found  和彩 's answer ID: 16424385 , with keyword  too simple
Traceback (most recent call last):
  File "/Users/Jackson/Documents/projects/Zhihu-AutoAnalyzer/main.py", line 43, in <module>
    pool.map(do_check, me.followings)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/multiprocessing/pool.py", line 260, in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/multiprocessing/pool.py", line 602, in get
    self.wait(timeout)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/multiprocessing/pool.py", line 599, in wait
    self._event.wait(timeout)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/threading.py", line 549, in wait
    signaled = self._cond.wait(timeout)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/threading.py", line 293, in wait
    waiter.acquire()
KeyboardInterrupt

Process finished with exit code 1

```
