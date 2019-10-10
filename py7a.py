f1=open('file1.txt','w')
for val in range(2, 1001): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           f1.write(f"{val} ")
f1.close()
print("Done writing to file1")

def isHappyNumber(num):    
    rem = summ = 0
    while(num > 0):    
        rem = num%10;    
        summ= summ+ (rem*rem);    
        num = num//10;    
    return summ  

f2=open('file2.txt','w')
for i in range(1,1001):
	res=i
	while res!=1 and res!=4:
		res=isHappyNumber(res)
	if res==1:
		#print(res," ")
		f2.write(f"{i} ")
	elif res==4:
		pass
f2.close()
print("Done writing to file2")

f1=open('file1.txt','r')
f2=open('file2.txt','r')
n1=set(map(int,f1.read().split()))
n2=set(map(int,f2.read().split()))
print(n1.intersection(n2))
f1.close()
f2.close()
