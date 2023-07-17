num=int(input("enter the number : "))
ls=[]
def get_series(num):
    if(num%2==0):
        num=num-1
        for i in range(1,num+1):
            ls.append(i*2-1)
        return ls
    else:
        for i in range(1,num+1):
            ls.append(i*2-1)
        return ls
    
print(get_series(num))