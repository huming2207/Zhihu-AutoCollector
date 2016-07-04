# zhihu-collection-manager
一个基于Python的多线程知乎自动收藏/收藏管理脚本工具集。

***For those non-Chinese guys:***

Zhihu (Chinese: 知乎) is a Chinese online Q&A forum. See here: https://en.wikipedia.org/wiki/Zhihu

These python tools are designed for automatically collecting/managing answers on Zhihu.


### 使用方法 - zhc-autocollect
zhc-autocollect是一个按关键词自动爬取知乎上的帖子内容的脚本。

使用前请在***keyword.txt关键词列表***设置关键词，每行一个。

用本工具登录后，它会自动爬取你关注的人的点赞和回答，并将命中关键词列表的回答帖子加入指定收藏中。

参数说明：

	—-collection CollectionID    指定一个收藏夹ID （必须）

	—-thread ThreadAmount	      指定线程数，建议小于10，视情况最好在3到7左右。（可选）

输出结果示例：

```
/usr/local/bin/python3 /Users/Jackson/Documents/projects/Zhihu-AutoAnalyzer/zhc-autocollect.py
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

（下略）

```

### 使用方法 - zhc-backup
zhc-backup是一个备份知乎收藏夹的脚本。

参数说明：

	—-collection CollectionID    指定一个收藏夹ID （必须）

	—-thread ThreadAmount	      指定线程数，建议小于10，视情况最好在3到7左右。（可选）

	--download									下载（备份）模式，将自动下载指定收藏夹内容。

	--upload										上传（备份）模式，将自动上传脚本同目录中的备份数据到指定收藏夹。

示例输出：

```

/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/Jackson/Documents/projects/Zhihu-AutoCollector/zhc-backup.py --collection 82049870 --download --thread 3
----- Zhihu OAuth Login -----
email: *****************
password: **************

Login success.
Selected collection:  82049870
Thread amount:  3
Mode: Download (Backup)
Initializing...
Now backing up: 如何看待网传上海某医院给植物人注射葡萄糖使其质壁分离致死，家属起诉医院事件？ - 米调炫枫
Now backing up: 有哪些不在语文课本里，但脍炙人口，很多人都会背诵引用的名篇？ - 陈陈浩华
Now backing up: 520求各种撩妹技能？ - 空峰
Now backing up: 如何反驳「因为你迟到，全班40个人每人耽误一分钟，加起来是一节课」？ - licro
Now backing up: 10 个字可以写出什么样的微小说？ - 愚木
Now backing up: 有哪些不在语文课本里，但脍炙人口，很多人都会背诵引用的名篇？ - 顾凌峰
Now backing up: 如何评价《诸夏自由同盟宣言》与刘仲敬粉丝新建的诸夏论坛？ - 停姨间
Now backing up: 如何优雅的佩戴三角帽？ - 猫头鹰
Now backing up: 除了「困在同一天」，科幻小说还有哪些清奇的脑洞？ - 吴易
Now backing up: 真正的粉丝是什么样的？ - 帷幕
Now backing up: 真正的粉丝是什么样的？ - 凯常
Now backing up: 如何把深圳蛇口公安的通知翻译成精美的文言文？ - 麦克信田
Now backing up: 用什么可以替代求婚钻戒？ - 猫头鹰
Now backing up: 真正的粉丝是什么样的？ - 蠢凡凡
Now backing up: 如何看待很多成年人喊着过六一儿童节？ - 猫头鹰
Now backing up: 如何翻译“苟利国家生死以，岂因祸福避趋之”？ - 张天乙
Now backing up: 留学的你，还记得跨出国门第一天的感受么？ - 猫头鹰
Now backing up: 如何评价「偽中国語」？ - 京滨 HybridE210
Now backing up: 如何翻译“苟利国家生死以，岂因祸福避趋之”？ - 威廉姆斯
Now backing up: 有没有听起来很有钱的民谣？ - 夕林故人
Now backing up: 如何看待「中国是母亲，香港是孩子」的比喻？ - 猫头鹰
Now backing up: 人生一定会遇到那个对的人吗？ - 夜溟
Now backing up: 有哪些精彩有趣的名家跨界作品值得推荐？ - Einzbern
Now backing up: 有哪些经典的战前动员讲话？ - 匿名用户
Now backing up: 皮肤也能辅助呼吸，为什么把头闷就会死呢? - 到处挖坑蒋玉成
Now backing up: 你认为的最有意思的歪改诗句有哪些？ - 千古留名
Now backing up: 如果不考虑薪水尊严面子，你最想从事什么工作？ - Einzbern
Now backing up: 如何挑逗女朋友? - 龙共火火
Now backing up: 如何看待希拉里炮轰特朗普：我们在选总统而非独裁者？ - 涂样
Now backing up: 素质高的标准是什么？ - 涂样
Now backing up: 「政治控」为什么会大量乐此不疲地活跃存在？ - 邰原朗
Now backing up: 你认为净空法师怎么样？ - 凯常
Now backing up: 在内燃机广泛应用以前中国人怎么给人“加油”？ - 匿名用户
Now backing up: 东北人有哪些令你难以忘怀的特点？ - 陆堂闵
Now backing up: 喜欢昆虫的男生有哪里不对吗？ - 匿名用户

（下略）

```


### 使用方法 - zhc-merger
zhc-merger是一个合并知乎收藏夹的脚本。

***WIP***

### 使用方法 - zhc-copier
zhc-copier是一个复制知乎收藏夹的脚本

***WIP***


### 依赖
7sDream大神的zhihu-oauth: https://github.com/7sDream/zhihu-oauth

ThreadPool多线程库（自带）。
