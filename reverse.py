#python program to check palindrome
a=input("Enter the string: ")
s=0;
e=len(a)-1
flag=1;
while s<=e:
    if(a[s]!=a[e]):
       flag=0
    s=s+1
    e=e-1
if(flag==1):
    print("The string ",a," is Palindrome")
else:
    print("The string ",a," is Not Palindrome")
#Code for checking number is Palidrome or not
b=int(input("Enter the number: "))
rev=int(0)
temp=int(b)
while temp!=0:
    digit=temp % 10
    rev=rev*10+digit
    temp=temp//10
if(rev==b):
    print("The Number ",b," is Palindrome")
else:
    print("The Number ",b," is Not Palindrome")
