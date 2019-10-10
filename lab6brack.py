def isValid(s):
	bracs={'(':')','[':']','{':'}'}
	stack=[]
	for bracket in s:
		if bracket in bracs:
			stack.append(bracs[bracket])
		elif not stack or bracket!=stack.pop():
			return False
	return not stack
c=1
while c:	
	string=input("Enter brackets sequence: ")
	if isValid(string):
		print("Brackets are balanced")
	else:
		print("Brackets not balanced")
	c=int(input("continue?[1-yes|0-no]: "))

