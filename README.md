# WeAudioDL
【使用说明】
1. 安装requests, selenium, chrome webdriver
2. 下载并编辑 main.py，修改参数：saveFolder 保存路径,pagetxt 调试文件保存路径
3. 运行main.py，按提示输入微信公众号发布的链接，支持下载专辑/音频（链接中包含&album_id= 或 &mid=）

## 微信公众号的【专辑】下载
~~~
本工具用于下载微信公众号发布的广播剧、有声小说等音频。
请输入【专辑】或【音频】链接：
 https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzk0OTI0NDgwOA==&action=getalbum&album_id=1864379555835101185&scene=173
一共检索到 69 部广播剧。
...
是否下载 广播剧 | 《你的距离》by公子优 小剧场（郑希&羊仔） ? (Y/N)  Y
0.G:\mp3\有声小说\你的距离小剧场08·钢笔.mp3 已保存
1.G:\mp3\有声小说\你的距离小剧场09·一滴水的缘分.mp3 已保存
2.G:\mp3\有声小说\你的距离小剧场10·浏览器记录.mp3 已保存
3.G:\mp3\有声小说\你的距离反串小剧场·钢笔.mp3 已保存
4.G:\mp3\有声小说\你的距离主题曲《开车去北方》.mp3 已保存
5.G:\mp3\有声小说\你的距离主题曲《终极定理》.mp3 已保存
====== 《你的距离》by公子优 小剧场（郑希&羊仔） 下载完成 ======
是否下载 广播剧 | 《一个钢镚儿》第一季1-12期＋小剧场（吴晛&李轻扬） ? (Y/N) N
是否下载 广播剧 | 《一个钢镚儿》第二季1-14期（吴晛&李轻扬） ? (Y/N) N
是否下载 《攻略对象出了错》by金刚圈 1-16期（江山&锦鲤） ? (Y/N) Y
...
~~~

### 专辑 页面

![image](https://github.com/chopper-go/WeAudioDL/blob/main/image/1.png)


## 微信公众号发布的【音频】下载
获取当前页面的所有音频，并逐个下载，已下载的跳过
~~~
本工具用于下载微信公众号发布的广播剧、有声小说等音频。
请输入【专辑】或【音频】链接：
https://mp.weixin.qq.com/s?__biz=Mzk0OTI0NDgwOA==&mid=2247483785&idx=1&sn=08d08a074fbdee85727e6fc13a79ece8&cur_album_id=1864379555835101185#rd

0. 《小白杨》第一期.mp3 已存在，跳过
1. 小白杨第二集.mp3 已存在，跳过
2. 小白杨第三期.mp3 下载成功
3. 《小白杨》第四期.mp3 下载成功
4. 《小白杨》第五期.mp3 下载成功
5. 小白杨第六期.mp3 下载成功
6. 《小白杨》第七期.mp3 下载成功
~~~

### 音频 页面

  ![image](https://github.com/chopper-go/WeAudioDL/blob/main/image/2.png)

 ### 下载到本地文件夹：

  ![image](https://github.com/chopper-go/WeAudioDL/blob/main/image/3.png)

