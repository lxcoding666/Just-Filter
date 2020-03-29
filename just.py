#!/usr/bin/python/lxcoding
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import time
import sys
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[37;1m'
# ( -- LOGO * INFO -- ) #

print(bcolors.FAIL + "   .-..-..-. .--. .-----.         .---. .-..-.   .-----. .--. .---. " + bcolors.ENDC)
print(bcolors.FAIL + "   : :: :: :: .--'`-. .-'         : .--': :: :   `-. .-': .--': .; :" + bcolors.ENDC)
print(bcolors.FAIL + " _ : :: :: :`. `.   : :   _____   : `;  : :: :     : :  : `;  :   .'" + bcolors.ENDC)
print(bcolors.WHITE + ": :; :: :; : _`, :  : :  :_____:  : :   : :: :__   : :  : :__ : :.`." + bcolors.ENDC)
print(bcolors.WHITE + "`.__.'`.__.'`.__.'  :_;           :_;   :_;:___.'  :_;  `.__.':_;:_;" + bcolors.ENDC)

#################################
# ( -- PROGRAMMED BY @LX.CODING -- ) #
#################################

								# ( -- DON'T CHANGE THE AUTHOR PLEASE -- ) #
# -------------------------------- ## --------------------------------- ## -------------------------------- #

print(bcolors.HEADER + "[$] MAILIST DOMAIN FILTER BY COUNTRY." + bcolors.ENDC)
print(bcolors.OKGREEN + "[$] URL = ('https://lx-coding.com/')." + bcolors.ENDC)
print(bcolors.UNDERLINE + "[$] SCRIPT PROGRAMMED BY LX.CODING PYTHON2." + bcolors.ENDC)

# -------------------------------- ## --------------------------------- ## -------------------------------- #
list = raw_input(' [X] MASUKAN LISTNYA GAYN .TXT => ')
# -------------------------------- ## --------------------------------- ## -------------------------------- #
print ' [X] SCRIPT STARTED NOW .. \n'; time.sleep(1)
# -------------------------------- ## --------------------------------- ## -------------------------------- #

for email in open(list, 'r'):
	email = email.strip()
	if '@aol.com' in email:
		aol = open('aol.txt','a+')
		aol.write(email + '\n')
		aol.close()
		print '[AOL] ',email
	elif '@ymail' in email:
		ymail = open('ymail.txt','a+')
		ymail.write(email + '\n')
		ymail.close()
		print '[YMAIL] ',email
	elif '@yahoo.com.au' in email:
		yahooau = open('yahoo.com.au.txt','a+')
		yahooau.write(email + '\n')
		yahooau.close()
		print '[YAHOO AU] ',email
	elif '@yahoo.com.sg' in email:
		yahoosg = open('yahoo.com.sg.txt','a+')
		yahoosg.write(email + '\n')
		yahoosg.close()
		print '[YAHOO SG] ',email
	elif '@yahoo.com.ar' in email:
		yahooar = open('yahoo.com.ar.txt','a+')
		yahooar.write(email + '\n')
		yahooar.close()
		print '[YAHOO AR] ',email
	elif '@yahoo.com.tw' in email:
		yahootw = open('yahoo.com.tw.txt','a+')
		yahootw.write(email + '\n')
		yahootw.close()
		print '[YAHOO TW] ',email
	elif '@yahoo.com.mx' in email:
		yahoomx = open('yahoo.com.mx.txt','a+')
		yahoomx.write(email + '\n')
		yahoomx.close()
		print '[YAHOO MX] ',email
	elif '@yahoo.com.br' in email:
		yahoomx = open('yahoo.com.br.txt','a+')
		yahoomx.write(email + '\n')
		yahoomx.close()
		print '[YAHOO BR] ',email
	elif '@yahoo.com' in email:
		yahoo = open('yahoo.txt','a+')
		yahoo.write(email + '\n')
		yahoo.close()
		print '[YAHOO] ',email
	elif '@rocketmail' in email:
		rocketmail = open('rocketmail.txt','a+')
		rocketmail.write(email + '\n')
		rocketmail.close()
		print '[ROCKETMAIL] ',email
	elif '@sky' in email:
		sky = open('sky.txt','a+')
		sky.write(email + '\n')
		sky.close()
		print '[SKY] ',email
	elif '@yahoo.co.uk' in email:
		yahoouk = open('yahoo.co.uk.txt','a+')
		yahoouk.write(email + '\n')
		yahoouk.close()
		print '[YAHOO UK] ',email
	elif '@yahoo.co.jp' in email:
		yahoojp = open('yahoo.co.jp.txt','a+')
		yahoojp.write(email + '\n')
		yahoojp.close()
		print '[YAHOO JP] ',email
	elif '@yahoo.fr' in email:
		yahoofr = open('yahoo.fr.txt','a+')
		yahoofr.write(email + '\n')
		yahoofr.close()
		print '[YAHOO FR] ',email
	elif '@yahoo.de' in email:
		yahoode = open('yahoo.de.txt','a+')
		yahoode.write(email + '\n')
		yahoode.close()
		print '[YAHOO DE] ',email
	elif '@yahoo.com.ph' in email:
		yahooph = open('yahoo.com.ph.txt','a+')
		yahooph.write(email + '\n')
		yahooph.close()
		print '[YAHOO PH] ',email
	elif '@yahoo.ca' in email:
		yahooca = open('yahoo.ca.txt','a+')
		yahooca.write(email + '\n')
		yahooca.close()
		print '[YAHOO CA] ',email
	elif '@yahoo.com.hk' in email:
		yahoohk = open('yahoo.com.hk.txt','a+')
		yahoohk.write(email + '\n')
		yahoohk.close()
		print '[YAHOO HK] ',email
	elif '@hotmail.co.jp' in email:
		hotmailjp = open('hotmail.co.jp.txt','a+')
		hotmailjp.write(email + '\n')
		hotmailjp.close()
		print '[HOTMAIL JP] ',email
	elif '@hotmail.co.uk' in email:
		hotmailuk = open('hotmail.co.uk.txt','a+')
		hotmailuk.write(email + '\n')
		hotmailuk.close()
		print '[HOTMAIL UK] ',email
	elif '@hotmail.com.au' in email:
		hotmailau = open('hotmail.com.au.txt','a+')
		hotmailau.write(email + '\n')
		hotmailau.close()
		print '[HOTMAIL AU] ',email
	elif '@hotmail.com.ar' in email:
		hotmailar = open('hotmail.com.ar.txt','a+')
		hotmailar.write(email + '\n')
		hotmailar.close()
		print '[HOTMAIL AR] ',email
	elif '@sbcglobal.net' in email:
		sbcglobal = open('sbc.txt','a+')
		sbcglobal.write(email + '\n')
		sbcglobal.close()
		print '[SBC] ',email
	elif '@att.net' in email:
		att = open('att.txt','a+')
		att.write(email + '\n')
		att.close()
		print '[ATT] ',email
	elif '@icloud.com' in email:
		icloud = open('icloud.txt','a+')
		icloud.write(email + '\n')
		icloud.close()
		print '[ICLOUD] ',email
	elif '@yandex.ru' in email:
		yanderu = open('yandex.ru.txt','a+')
		yanderu.write(email + '\n')
		yanderu.close()
		print '[YANDEX RU] ',email
	elif '@yandex.com' in email:
		yandex = open('yandex.com.txt','a+')
		yandex.write(email + '\n')
		yandex.close()
		print '[YANDEX] ',email
	elif '@comcast.net' in email:
		comcast = open('comcast.txt','a+')
		comcast.write(email + '\n')
		comcast.close()
		print '[COMCAST] ',email
	elif '@comcast.net' in email:
		comcast = open('comcast.txt','a+')
		comcast.write(email + '\n')
		comcast.close()
		print '[COMCAST] ',email
	elif '@cox.net' in email:
		cox = open('cox.txt','a+')
		cox.write(email + '\n')
		cox.close()
		print '[COX] ',email
	elif '@cox.net' in email:
		cox = open('cox.txt','a+')
		cox.write(email + '\n')
		cox.close()
		print '[COX] ',email
	elif '@optonline.net' in email:
		opto = open('optonline.txt','a+')
		opto.write(email + '\n')
		opto.close()
		print '[OPTONLINE] ',email
	elif '@naver.com' in email:
		naver = open('naver.txt','a+')
		naver.write(email + '\n')
		naver.close()
		print '[NAVER] ',email
	elif '@juno.com' in email:
		juno = open('juno.txt','a+')
		juno.write(email + '\n')
		juno.close()
		print '[JUNO] ',email
	elif '@juno.com' in email:
		juno = open('juno.txt','a+')
		juno.write(email + '\n')
		juno.close()
		print '[JUNO] ',email
	elif '@btopenworld' in email:
		btopenworld = open('btopenworld.txt','a+')
		btopenworld.write(email + '\n')
		btopenworld.close()
		print '[BTOPENWORLD] ',email
	elif '@ntlworld' in email:
		ntlworld = open('ntlworld.txt','a+')
		ntlworld.write(email + '\n')
		ntlworld.close()
		print '[NTLWORLD] ',email
	elif '@btinternet' in email:
		btinternet = open('btinternet.txt','a+')
		btinternet.write(email + '\n')
		btinternet.close()
		print '[BTINTERNET] ',email
	elif '@virginmedia' in email:
		virginmedia = open('virginmedia.txt','a+')
		virginmedia.write(email + '\n')
		virginmedia.close()
		print '[VIRGINMEDIA] ',email
	elif '@virginmedia' in email:
		virginmedia = open('virginmedia.txt','a+')
		virginmedia.write(email + '\n')
		virginmedia.close()
		print '[VIRGINMEDIA] ',email
	elif '@gmx' in email:
		gmx = open('gmx.txt','a+')
		gmx.write(email + '\n')
		gmx.close()
		print '[GMX] ',email
	elif '@web.de' in email:
		webde = open('web.de.txt','a+')
		webde.write(email + '\n')
		webde.close()
		print '[WEB DE] ',email
	elif '@arcor.de' in email:
		arcorde = open('arcor.de.txt','a+')
		arcorde.write(email + '\n')
		arcorde.close()
		print '[ARCOR DE] ',email
	elif '@t-online.de' in email:
		tonline = open('t-online.txt','a+')
		tonline.write(email + '\n')
		tonline.close()
		print '[T-ONLINE DE] ',email
	elif '@softbank.co.jp' in email:
		softbank = open('softbank-jp.txt','a+')
		softbank.write(email + '\n')
		softbank.close()
		print '[SOFTBANK JP] ',email
	elif '@mail.ru' in email:
		mailru = open('mailru.txt','a+')
		mailru.write(email + '\n')
		mailru.close()
		print '[MAIL RU] ',email
	elif '@free.fr' in email:
		freefr = open('free.fr.txt','a+')
		freefr.write(email + '\n')
		freefr.close()
		print '[FREE FR] ',email
	elif '@orange.fr' in email:
		orangefr = open('orange.fr.txt','a+')
		orangefr.write(email + '\n')
		orangefr.close()
		print '[ORANGE FR] ',email
	elif '@wanadoo.net' in email:
		wanadoo = open('wanadoo.txt','a+')
		wanadoo.write(email + '\n')
		wanadoo.close()
		print '[WANADO NET] ',email
	elif '@wanadoo.net' in email:
		wanadoo = open('wanadoo.txt','a+')
		wanadoo.write(email + '\n')
		wanadoo.close()
		print '[WANADO NET] ',email
	elif '@hotmail.com'  in email:
		hotmail = open('hotmail.com.txt','a+')
		hotmail.write(email + '\n')
		hotmail.close()
		print '[HOTMAIL] ',email
	elif '@live' in email:
		live = open('live.com.txt','a+')
		live.write(email + '\n')
		live.close()
		print '[LIVE.COM] ',email
	elif '@outlook.com' in email:
		outlook = open('outlook.txt','a+')
		outlook.write(email + '\n')
		outlook.close()
		print '[OUTLOOK] ',email
	elif '@msn.com' in email:
		msn = open('msn.com.txt','a+')
		msn.write(email + '\n')
		msn.close()
		print '[MSN] ',email
	else:
		others = open('others.txt','a+')
		others.write(email + '\n')
		others.close()
		print '[OTHERS] ',email
print '[X] SLESE JUGA CAPE BAT ANJINK ', len(open(list, 'r').readlines()), ' . Email'
