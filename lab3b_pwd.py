import random

def gen_pwd():
	l='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@~#$%^&*()_-+={}[]|?><`,.'
	l=list(l)
	pwd=[]
	while len(pwd)<14:
		pwd.append(l[random.randint(0,89)])
	return ''.join(pwd)
	
choice=1
while choice==1:
	print("Your new password: ")
	print(gen_pwd())
	choice=int(input("Want new password: [yes=1|no=0]? "))
	
