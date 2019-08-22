ip_arr=map(int,input("enter an array of integers ").split(' '))
op_arr=[]
for i in ip_arr:
    if (i%2)==0:
        op_arr.append(i)
print(op_arr)
