#Program to print fibonacci series
a=0
b=1
fibo=int(input("Enter number of terms you want to print: "))
i=0       
while fibo>i:
    if(i==0):
        print(a," ")
    elif(i==1):
        print(b," ")
    else:
        nextterm=a+b
        print(nextterm," ")
        a=b
        b=nextterm 
    i=i+1
print("program close")
