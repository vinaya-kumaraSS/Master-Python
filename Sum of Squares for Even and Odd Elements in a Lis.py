def square(i):
    return i*i
MyList=[]
even_sum=0
odd_sum=0
ListNum=int(input("enter the number of elements:"))
for i in range(1,ListNum+1):
    ele=int(input())
    MyList.append(ele)
for i in MyList:
        if i%2==0:
            even_sum=even_sum+square(i)
        else:
            odd_sum=odd_sum+square(i)
print(f"[{even_sum},{odd_sum}]")