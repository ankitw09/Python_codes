x=int(input("Enter number x: "))
y=int(input("Enter number y: "))
z=int(input("Enter number z: "))
if(x > y and x > z and x%2!=0):
    print("maximum odd number from 3 no is: ", x)
elif(y > z and y%2!=0):
     print("maximum odd number from 3 no is: ", y)
elif(z%2!=0):
    print("maximum odd number from 3 no is: ", z)
else:
    print("NO odd number exist in 3 numbers")
