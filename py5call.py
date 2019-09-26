class CallDetail():
	def __init__(self,calling,called,mins,ctype):
		self.__calllingNo=calling
		self.__calledNo=called
		self.__time=mins
		self.__callType=ctype
		
	def __str__(self):
		return f"\n Calling number: {self.__calllingNo}\n Called Number :{self.__calledNo}\n Call Duration: {self.__time}\n Call Type: {self.__callType}\n"
	
class Util():
	callTypes={'STD':0,'local':0,'ISD':0}
	def __init__(self):
		self.list_of_call_objects=[]
		
	def parse_customer(self,callstring):
		for s in callstring:
			callingNo,calledNo,time,ctype=s.split()
			Util().callTypes[ctype]+=1
			self.list_of_call_objects.append(CallDetail(callingNo,calledNo,time,ctype))
		
	def details(self):
		print("\nCall Details\n")
		for o in self.list_of_call_objects:
			print(o)
			
	def callCount(self):
		for k,v in Util.callTypes.items():
			print(f"\nCount of {k} calls :{v}")

list_of_call_string=[]
n=int(input("Enter the number of calls: "))
print("Enter the phone number that called, the number that was called, call duration and call-type{STD|ISD|local} ")	
for i in range(n):
	list_of_call_string.append(input())
callob=Util()
callob.parse_customer(list_of_call_string)
callob.details()
callob.callCount()
