# -*- coding:utf-8 -*-
# 作者【乔巴】： https://github.com/chopper-go

import requests
import re #正则
import time 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

saveFolder='D:\\有声小说'
pagetxt='D:\\pagetxt.txt' #调试用


# 广播剧列表
# allUrl='https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzk0OTI0NDgwOA==&action=getalbum&album_id=1864379555835101185&scene=173'


def getMediaEachPage(url):
    chrome_options = Options()  
    chrome_options.add_argument("--headless") 
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    Id=[]
    Name=[]
    media=[]
    try:
        driver.get(url) 
        pageSource=driver.page_source.replace("&nbsp;","")
        driver.close()
        Id=re.findall("voice_encode_fileid=\"(.*?)\"",pageSource)
        Name=re.findall("role=\"link\">(.*?)</strong>",pageSource)

        #获取不到音频信息时，查看源码
        l=len(Id)
        if (len(Id) == 0 or len(Name) == 0):
            print('获取不到音频信息, 查看源码 ', pagetxt)
            with open(pagetxt,'w',encoding='utf-8') as f:
                f.write(pageSource)

        media=[Id,Name]
        return media
    except Exception as e:
        print(e)

def SaveMP3(media):
    mediaId=media[0]
    MediaName=media[1]
    for i in range(0,len(mediaId)):
        savelink='https://res.wx.qq.com/voice/getvoice?mediaid='+mediaId[i]
        fileName=saveFolder + "\\" + MediaName[i]
        if os.path.exists(fileName):
            print(str(i) + '. '+ MediaName[i] + ' 已存在，跳过')
        else:
            try:
                file = requests.get(savelink)
                with open(fileName, 'wb') as f:
                    f.write(file.content)
                print(str(i) + '. '+ MediaName[i] + ' 下载成功')
            except:
                print(str(i) + '. '+ MediaName[i] + ' 下载失败，重试')
                SaveMP3(media)


def getList(url):
    chrome_options = Options()  
    chrome_options.add_argument("--headless") 
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()

    try:
        driver.get(url) 
        for i in range(0,10):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(0.5)
        pageSource=driver.page_source.replace("&nbsp;","").replace("amp;","")

        driver.close()
        allNames=re.findall("data-title=\"(.*?)\"",pageSource)
        allLinks=re.findall("data-link=\"(.*?)\"",pageSource)        
        all=[allNames,allLinks]
        ll=len(allNames)
        print('一共检索到 %d 部广播剧。' %ll)
        return all
    except Exception as e:
        print(e)

print('本工具用于下载微信公众号发布的广播剧、有声小说等音频\n')
choose= input('请根据下载方式输入 1 或 2 ：\n【1】下载专辑（网页中只有链接，不含音频）\n【2】直接下载（网页中含音频）\n')

if choose =='1':
    allurl =''
    if  allurl =='':
        allurl=input('请输入专辑链接(链接中含album)：')  
    allpages=getList(allUrl)
    pageName=allpages[0]
    pageLink=allpages[1]

    for i in range(0,len(pageName)):    
        # if input('是否下载 ' + pageName[i] + ' ? (Y/N) ')  =='Y':
            media=getMediaEachPage(pageLink[i])
            if len(media[1]) > 0:
                SaveMP3(media)
                print('='*6 ,pageName[i],'下载完成','='*6)
            else:
                print('!'*6 ,pageName[i],'未获取到，跳过','!'*6)
if choose =='2':
    SingleUrl =''
    if  SingleUrl =='':
        SingleUrl=input('请输入音频链接(网页中含播放的音频)：')
        media=getMediaEachPage(SingleUrl)
        if len(media[1]) > 0:
            SaveMP3(media)
            print('='*6 ,'下载完成','='*6)
else:
    print('='*6 ,'未下载，退出','='*6)
    
