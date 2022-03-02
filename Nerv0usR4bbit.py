# ============================================== #
# POST EXPLOITATION ENUMERATION TOOL FOR WINDOWS #
# @34ZY						 #
# ============================================== #

import os
import time
import socket
import sys

# ============================================== #
# BANNER
# ============================================== #

def banner():
	print(r'''

        .--,_
       / ,/ /\
      / // /\ \
     / // /_\\|
   .'  ' (
  /__    \.-"""-._
 / 0>  ' .    '    `-.          |> ɴᴇʀᴠ0ᴜs ʀ4ʙʙɪᴛ >|
(       .  '      "   `.        
 `/─-.-'     "       '  ;       |> Pᴏsᴛ Exᴘʟᴏɪᴛᴀᴛɪᴏɴ Eɴᴜᴍᴇʀᴀᴛɪᴏɴ ᴛᴏᴏʟ >|
 /   `.'  "  .  .-'    " ;   	|> @34ZY >|
~     : .     .'          ;
      `.   ' :     '   '  ;
        )  _.". "     .  ";..
      .'_.'   .'   '  __.,   `\
     '"      ""''---'`    "''"`
--------------------------------------------------------------------------
		''')

# ============================================== #
# Progress bar
# ============================================== #

animation = "|/-\\"

# ============================================== #
# Enumeration process
# ============================================== #

def New_prompt():
	os.system("cmd.exe")

def Enum_system():

	try :
		THREADS = input('[-) Choose number of threads (1.5s by default) : ')
		#print(THREADS)

		if THREADS == '':
			THREADS = '1.5'
			print(f'\n\n[*] Threads set to default ({THREADS} seconds)')
			time.sleep(1)
			print('[!] R4bbit is hungry and try to get new friends ...')
			THREADS = 1.5
		else : 
			print(f'[+] R4bbit setting threads set to {THREADS} seconds.')
			time.sleep(1)
			THREADS = int(float(THREADS))

		LOCAL_USERNAME = os.getlogin()

		print(f'[*] R4bbit found local user is : {LOCAL_USERNAME}')
		time.sleep(1)
		print('[+] R4bbit try to find some infos reliated to this windo system ...\n')
		time.sleep(1)
		os.system("systeminfo")
		time.sleep(THREADS)
		print('\n--------------------------------------------------------------------------')
		print('\n[+] R4bbit try to watch if are there TCP open ports ...\n')
		time.sleep(0.5)
		os.system('netstat -ano|findstr /i tcp|findstr /i LISTENING')
		time.sleep(THREADS)
		print('\n--------------------------------------------------------------------------')
		print('\n[+] R4bbit check if this account have any interesting privilege ...\n')
		os.system(f'net user /domain {LOCAL_USERNAME}')
		time.sleep(THREADS)
		print('\n--------------------------------------------------------------------------')
		print('\n[+] R4bbit is checking interesting running services ...\n')
		os.system('wmic service get name,displayname,pathname,startmode |findstr /i "Auto" | findstr /i /v "C:\Windows"')
		print('\n--------------------------------------------------------------------------')
		time.sleep(THREADS)
		
		print('\n[+] R4bbit is checking local network status ...')
		print('[+] R4bbit is getting ip addresses ...')
		hostname = socket.gethostname()
		local_ip = socket.gethostbyname(hostname)
		print(f'[$] R4bbit found your local ip adress : {local_ip}')
		local_ip = '.'.join(local_ip.split('.')[:-1]) # Replace last byte from ip adress
		print('[+] R4bbit is asking for new friends in this network ...\n')

		i = 0
		staussum = 0
		time.sleep(THREADS)
		os.system(f'arp -a|findstr /i {local_ip}')
		
		print('\n[+] R4bbit try to ping his friends ... \n')
		print('\n[?] R4bbit is slow be patient ... <(O__O)> \n')

		for i in range(0,256,1):

			sys.stdout.write("\r" + animation[i % len(animation)])
			sys.stdout.flush()
			
			status = os.system(f'ping -n 1 -w 200 {local_ip}.' + f'{i} > nul && echo  ʕɔ•_•ʔɔ [$] New friend found : {local_ip}.' + f'{i}')
			time.sleep(THREADS)

		print('\n[!] R4bbit is now trying to find HIDDED friends (^ₒ^c) ...')
		time.sleep(2)
		os.system(f'arp -a')
		print('\n--------------------------------------------------------------------------')
		print('\n[!] R4bbit is sleepy. Going home now ... <(─__─")>')
		time.sleep(1)
		print('[*] Enjoy thoses juicy infos :3')
		time.sleep(0.3)
		print('[+] R4bbit finished to fetch this system.')

	except KeyboardInterrupt:
    		print('''\n/!\ R4bbit is hidding ...''')

# ============================================== #
# MAIN 
# ============================================== #

def main():
	banner()
	#New_prompt()
	Enum_system()
if __name__ == '__main__':
	main()
