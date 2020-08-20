import os
import getpass

os.system("clear")


os.system("tput setaf 7")
print("\t\t\t==============================================")
os.system("tput setaf 2")
print("\t\t\t|Hey Welcome to my TUI that makes life simple|")
os.system("tput setaf 7")
print("\t\t\t==============================================")

passwd=getpass.getpass("Enter the password: ")

apass="redhat"

if passwd != apass:
	print("Sorry! You've entered the wrong password..")
	exit()
	
print("In which mode do you want to open(local/remote)", end=": ")
location =input()

if location=="remote":
	print("Enter the ip address of remote host",end=": ")
	ip=input()
			
while(True):
	
	
	if location=="local":			#local mode
		
		print('''
		\t\t\tPress 1. to see DATE
		\t\t\tPress 2. to see CALENDAR
		\t\t\tPress 3. to open FIREFOX		
		\t\t\tPress 4. to EXIT
		''')

		a=int(input("Enter your choice "))
		print()
		
		if(a==1):
			os.system("date") 			
			os.system("date | espeak-ng")

		elif(a==2):
			os.system("cal")
			os.system("cal | espeak-ng")

		elif(a==3):
			os.system("firefox &")

		elif(a==4):
			exit()

		else:
			print("Please enter a valid choice: ")
		
	elif location=="remote":		#remote mode
		
		print('''
		\t\t\tPress 1. to see DATE
		\t\t\tPress 2. to see CALENDAR
		\t\t\tPress 3. to open FIREFOX		
		\t\t\tPress 4. to EXIT
		''')

		a=int(input("Enter your choice "))
		print()
		
		if(a==1):
			os.system("ssh {} date".format(ip))

		elif(a==2):
			os.system("ssh {} cal".format(ip))
        
		elif(a==3):
			exit("ssh {} firefox&".format(ip))
			
		elif(a==4):
			exit()

		else:
			print("Please enter a valid choice: ")

	
	else:
		print("Invalid choice, Enter Again !")
		exit()

	input("Press Enter to continue: ")		
	os.system("clear")


	

