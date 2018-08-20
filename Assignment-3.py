
#Question 1
list1=[1,2,3,4,5]
list1.reverse()
print(list1)

#Question 2
str1="Acadview"
for i in range(len(str1)):
    if(ord(str1[i])>=65 and ord(str1[i])<97):
        print(str1[i])
        
#Question 3
a=input()
c=[]
c=a.split(",")
d=[]
for i in c:
    d.append(int(i))
print(d)


#Question 4
c=input()
d=c[::-1]
if(c==d):
    print("palindrome")
else:
    print("not palindrome")


#Question 5
import copy as c
a=[1,2,[5,6,7]]
b=c.deepcopy(a)
print(a)
print(b)
"""
Shallow copying is creating a new object and then copying the non static fields
of the current object to the new object. If the field is a value type, a bit by
bit copy of the field is performed.
Deep copy is creating a new object and then copying the non-static fields of the
current object to the new object. If a field is a value type, a bit by bit copy
of the field is performed."""
