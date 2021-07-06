# WeAudioDL
【使用说明】
1. 安装requests, selenium, chrome webdriver
2. 下载并打开 main.py，修改参数：allUrl 音频合辑链接，saveFolder 保存路径

## 修改微信公众号的音频专辑链接，下载音频  
结果预览
~~~
一共检索到 67 部广播剧。
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

### 1. 提供微信公众号的音频合辑链接（allUrl），获取所有音频列表，并逐个询问是否下载？
~~~
https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzk0OTI0NDgwOA==&action=getalbum&album_id=1864379555835101185&scene=173
~~~

广播剧合辑 页面

![image](https://github.com/chopper-go/WeAudioDL/blob/main/image/1.png)

点进每部广播剧的 页面

  ![image](https://github.com/chopper-go/WeAudioDL/blob/main/image/2.png)

 ### 2. 下载 每部广播剧的所有音频到本地文件夹，如下：

  ![image](https://github.com/chopper-go/WeAudioDL/blob/main/image/3.png)

