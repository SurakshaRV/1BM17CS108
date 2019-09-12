class Student():
	def __init__(self):
		self.__id=self.__age=self.__marks=None
		
	def val_marks(self):
		if self.__marks<=100 and self.__marks>=0:
			return True
		else:
			return False
			
	def val_age(self):
		if self.__age>=20:
			return True
		else:
			return False
			
	def check_qual(self):
		if self.val_age() and self.val_marks():
			if self.__marks>=65:
				return True
			else:
				return False
		else:
			return False
			
	def set_det(self,d,age,m):
		self.__id=d
		self.__age=age
		self.__marks=m
		
	def get_det(self):
		return f"\nStudent id: {self.__id} \nAge: {self.__age}\n Marks: {self.__marks} \n Qualified for admission?: {self.check_qual()}"
		
n=int(input("How many students? "))
st=[Student() for i in range(n)]
for i in range(n):
	print(f"Enter details of student {i+1}")
	age=int(input("age: "))
	m=int(input("marks: "))
	st[i].set_det(i+1,age,m)
print("\nStudents List\n")
for i in range(n):
	print(st[i].get_det())		
