# /usr/bin/python3
# Tuul Ampas Gayn , Cuman buat ngisi Waktu luang
# © Ezz-Kun(zen) 2020
# Start: Rabu Apr 29 2020,- (lupa) WIB
# Done : Kamis Apr 30 2020,- 16:30:05 WIB
import requests as r	
import re,argparse
from sys import argv
from urllib.parse import unquote
from tqdm import tqdm

#-color-
m = '\033[1;31m'
h = '\033[1;32m'
ab = '\033[1;32m'
p = '\033[1;37m'

#-main-gan-
class ZipDl(object):
	def __init__(self,url,path):
		self.url = url
		self.path = path
		self.main()
	def main(self):
		print(f'{ab}[{p}*{ab}]{p} Checking Url Media')
		gets = r.get(self.url).text
		print(f'{ab}[{p}*{ab}]{p} Searching Url ')
		try:
			s = re.findall(r'document\.getElementById\(\'dlbutton\'\)\.href = \"\/d\/([\w\d]*)\/\" \+ \(([\d]*) % ([\d]*) \+ ([\d]*) % ([\d]*)\) \+ \"\/(.*)\";',gets)[0]
			ops = re.match(r"https:\/\/.*?.com\/",self.url).group(0)+'d/'+s[0]+'/'+str(int(s[1]) % int(s[2]) + int(s[3]) % int(s[4]))+'/'+unquote(s[5])
			print(f'{ab}[{p}*{ab}]{p} Searching Title')
			name_ = re.search('property\=\"og:title"\ content\=\"(.*) "',gets).group(1)
		except AttributeError:
			exit('---eror---')
		print(f'{ab}[{p}*{ab}]{p} Downloading Content')
		yosh = r.get(ops,stream=True)
		progres = tqdm(total=int(yosh.headers.get('content-length', 0)), unit='B', unit_scale=True)
		with open(self.path+name_, 'wb') as f:
			for data in yosh.iter_content(1024):
				progres.update(len(data))
				f.write(data)
		progres.close()
		print(f'{ab}[{p}*{ab}]{p} Okay File Saved As :> {h}'+name_)

try:
	fis = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description='Author : Ezz-Kun(zen)\nA Simple ZippyShare Downloader')
	fis.add_argument('-u','--url',help='url (link) content',metavar='')
	fis.add_argument('-p','--path',help='path save file (ex:/sdcard/)',metavar='')
	args = fis.parse_args()
	if args.url and args.path:
		ZipDl(args.url,args.path)
	else:
		print(f'''Usage : python {argv[0]} <options>
or python {argv[0]} -h for show all command''')
except Exception as e:
	print(f'--eror--: {m}{str(e)}')
