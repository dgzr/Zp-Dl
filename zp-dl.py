# /usr/bin/python3
# Tuul Ampas Gayn , Cuman buat ngisi Waktu luang
# © Ezz-Kun(zen) 2020
# Start: Rabu Apr 29 2020,- (lupa) WIB
# Done : Kamis Apr 30 2020,- 16:30:05 WIB
# update : Mon Jun 22 14:15:00 WIB 2020
# sebenernya aku buat ini cuman buat sendiri sih biar cepet ,
# buat download dari Nekopoi :c
# karna ngeselin aja bruh , klo pas download malah nyaasar ke lazada :V
import requests as r	
import re,argparse,sys,time
from sys import argv
from urllib.parse import unquote
from random import choice as cos
from tqdm import tqdm

class TextRun(object):
	def __init__(self,string):
		self.color = ['\033[1;31m','\033[1;34m','\033[1;37m','\033[1;33m','\033[1;36m']
		for i in string +'\n':
			sys.stdout.write(cos(self.color)+str(i))
			sys.stdout.flush()
			time.sleep(0.030)

class ZipDl(object):
	def __init__(self):
		self.color = ['\033[1;31m','\033[1;34m','\033[1;37m','\033[1;33m','\033[1;36m']
	def Solo_Url(self,url,path):
		gets = r.get(url).text
		try:
			s = re.findall(r'document\.getElementById\(\'dlbutton\'\)\.href = \"\/d\/([\w\d]*)\/\" \+ \(([\d]*) % ([\d]*) \+ ([\d]*) % ([\d]*)\) \+ \"\/(.*)\";',gets)[0]
			ops = re.match(r"https:\/\/.*?.com\/",self.url).group(0)+'d/'+s[0]+'/'+str(int(s[1]) % int(s[2]) + int(s[3]) % int(s[4]))+'/'+unquote(s[5])
			name_ = re.search('property\=\"og:title"\ content\=\"(.*) "',gets).group(1)
			updt = re.findall('<font(.*?)</font><br',gets)[3].split('">')[-1]
			siz = re.findall('<font(.*?)</font><br',gets)[2].split('">')[-1]
		except Exception as Er:
			exit(f'---eror--- : {Er}')
		print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print(f'[+] Uploaded  : {updt}')
		print(f'[+] File Size : {siz}')
		print(f'[+] File Name : {name_}')
		print('[x] Downloading Content')
		yosh = r.get(ops,stream=True)
		progres = tqdm(total=int(yosh.headers.get('content-length', 0)), unit='B', unit_scale=True)
		with open(path+name_, 'wb') as f:
			for data in yosh.iter_content(1024):
				progres.update(len(data))
				f.write(data)
		progres.close()
		print(f'[x] succses, file saved in {path}\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	def Multi_Url(self,url,path):
		TextRun('[x] Getting All Url Contents')
		data = []
		name = []
		var = 0
		sto = 0
		list_url = open(url).read().splitlines()
		for url in range(int(len(list_url))):
			gets = r.get(list_url[var]).text
			try:
				s = re.findall(r'document\.getElementById\(\'dlbutton\'\)\.href = \"\/d\/([\w\d]*)\/\" \+ \(([\d]*) % ([\d]*) \+ ([\d]*) % ([\d]*)\) \+ \"\/(.*)\";',gets)[0]
				ops = re.match(r"https:\/\/.*?.com\/",list_url[var]).group(0)+'d/'+s[0]+'/'+str(int(s[1]) % int(s[2]) + int(s[3]) % int(s[4]))+'/'+unquote(s[5])
				name_ = re.search('property\=\"og:title"\ content\=\"(.*) "',gets).group(1)
				data.append(ops)
				name.append(name_)
				var +=1
			except Exception as Er:
				exit(f'---eror--- : {Er}')
		print(f'{self.color[2]}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		TextRun('[x] Start Download All Files')
		for download in range(int(len(data))):
			yosh = r.get(data[sto],stream=True)
			print(f'{self.color[1]}[{self.color[2]}x{self.color[1]}] {self.color[2]}Downloading File ``{self.color[1]}{name[sto]}``{self.color[2]}')
			progres = tqdm(total=int(yosh.headers.get('content-length', 0)), unit='B', unit_scale=True)
			with open(path+name[sto], 'wb') as f:
				for puki in yosh.iter_content(1024):
					progres.update(len(puki))
					f.write(puki)
			progres.close()
			sto +=1
		print(f'{self.color[1]}[{self.color[2]}x{self.color[1]}]{self.color[2]} Succses, All File Saved To {self.color[1]}{path}\n{self.color[2]}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

try:
	fis = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description='Author : Ezz-Kun(zen)\nA Simple ZippyShare Downloader')
	fis.add_argument('-u','--url',help='url (link) content',metavar='')
	fis.add_argument('-m','--multi',help='download file using multiple url',metavar='')
	fis.add_argument('-p','--path',help='path save file (ex:/sdcard/)',metavar='')
	args = fis.parse_args()
	if args.url and args.path:
		claSs = ZipDl()
		claSs.Solo_Url(args.url,args.path)
	elif args.multi and args.path:
		claSs = ZipDl()
		claSs.Multi_Url(args.multi,args.path)
	else:
		print(f'Usage : python {argv[0]} --help/-h for show all command')
except Exception as e:
#except EOFError:
#	pass
	print(f'--eror--: {e}')
