def find_key(arr,key):
	if key in arr:
		return True
	else:
		return False
		
arr=list(map(int,input().split(' ')))
num=int(input("Enter the number to be found: "))
print(find_key(arr,num))
