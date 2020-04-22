import webbrowser
url = input('瞅啥？输入视频链接呀：')
api = 'https://jx.km58.top/jx/?url='
vip_url = api + url
webbrowser.open(vip_url)
