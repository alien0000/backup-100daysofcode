def minList(l):
    min =l[0]
    for item in l:
        if item<min:
            min=item
        return min
        

        


l=[]
n=eval(input("enter number of the element in the list: "))
print("enter list elements :")
for i in range(0,n):
    ele=eval(input())
    l.append(ele)
m=minList(l)
print("the minimun number in the list is ",m)



