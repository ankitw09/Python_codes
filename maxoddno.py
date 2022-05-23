#method one to sum of odd no
max=0
i=0
a=0
while i<10:
    a=int(input("Enter no "))
    if(max < a and a%2!=0):
        max=a
    i=i+1
if(max > 0):
          print("maximum odd no from given ten no is: ",max)
else:
    print("No  odd number found")
    
#method two of sum of odd no using list
list1 = []
  
num = int(input("Enter number of elements in list: "))
  
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

j=0
maxelement=0
while j<num:
    if(maxelement < list1[j] and list1[j]%2!=0):
        maxelement=list1[j]
    j=j+1
print("Largest element is:", maxelement)

#method 3 of sum of odd no
digit=int(input("Enter ten digit no:"))
temp=digit
maxnum=0
while(temp!=0):
    dig=temp%10
    if(dig > maxnum and dig%2!=0):
        maxnum=dig
    temp=temp//10
print("max odd no in given integer: ",digit," is ",maxnum)

