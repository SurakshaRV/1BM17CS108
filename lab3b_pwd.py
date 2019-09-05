import random
import re
def gen_pwd():
    sp='!@~#$%^&*()_-+={}[]|?><`,.'
    l=list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@~#$%^&*()_-+={}[]|?><`,.')
    pwd=[]
    while len(pwd)<14:
        pwd.append(l[random.randint(0,78)])
    pwd=''.join(pwd)
    if re.search('[A-Z]', pwd) and re.search('[a-z]', pwd) and re.search('(\d)+', pwd) and any(c in sp for c in pwd) :
        return pwd
    else:
        gen_pwd()

choice=1
while choice==1:
	print("Your new password: ")
	print(gen_pwd())
	choice=int(input("Want new password: [yes=1|no=0]? "))
