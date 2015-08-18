import urllib.request
import urllib.parse


url='http://appex.cn.bing.com/'
user_agent=r'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.5.2000 Chrome/30.0.1599.101 Safari/537.36'
head={'User_Agent':user_agent}
req=urllib.request.Request(url,headers=head)
response=urllib.request.urlopen(req)
mainpage=response.read().decode('UTF8')
import re
pic=re.search(r"'http://s.cn.bing.net/az/hprichbg/rb/(.{1,100}\..{2,5})'",mainpage)
print(pic.group(1))
url=pic.group(0)[1:len(pic.group(0))-1]
localfile="D:\wallpapers\\"
localfile=localfile+pic.group(1)
urllib.request.urlretrieve(url,localfile)
import ctypes
dll = ctypes.windll.LoadLibrary( 'User32' )
SPI_SETDESKWALLPAPER=0x0014
SPIF_UPDATEINIFILE=0x01
dll.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, localfile, SPIF_UPDATEINIFILE) 
