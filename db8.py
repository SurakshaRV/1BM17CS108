import sqlite3
con=sqlite3.connect("mydb7.db")
p=con.cursor()
con.execute("CREATE TABLE STUDENT (roll int primary key not null, name charvar not null, sem int not null, dept charvar)")
details=[[1,'abc',5,'cse'],[2,'def',5,'cse'],[3,'xyz', 5, 'cse']]
con.executemany("INSERT INTO STUDENT VALUES(?,?,?,?)",details)
st_list=con.execute("SELECT * FROM STUDENT")
print("student details:")
print("Reg. No.| Name | sem | dept ")
for row in st_list:
	print(row)
det=p.execute("SELECT * FROM STUDENT WHERE roll=2")
print("Details of student whose reg no is 2 ")
for r in det:
	print(r)
p.execute("UPDATE STUDENT SET dept='ISE' WHERE roll=3")
print("after updating:")
st_list2=con.execute("SELECT * FROM STUDENT")
print("student details:")
print("Reg. No.| Name | sem | dept ")
for row in st_list2:
	print(row)
con.execute("DELETE FROM STUDENT WHERE roll=1")	
print("After deleting roll 1")
st_list3=con.execute("SELECT * FROM STUDENT")
print("student details:")
print("Reg. No.| Name | sem | dept ")
for row in st_list3:
	print(row)
