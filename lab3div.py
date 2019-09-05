def divisors(num):
	for i in range(1,num//2+1):
		if (num%i)==0:
			print(i)
	print(num)
	
choice=1	
while choice==1:
	n=int(input("Enter a number: "))
	print("The divisors of {} are".format(n))
	divisors(n)
	choice=int(input("Try for a different number? [yes=1|no=0]"))
