# Program to multiply two matrices using nested loops


Row = int(input("Enter the number of rows for matrix:"))
Col = int(input("Enter the number of columns for matrix:"))

A = []
print("Enter the entries rowwise:")

for i in range(Row):		
	temp =[]
	for j in range(Col):	 
		temp.append(int(input()))
	A.append(temp)


B = []
print("Enter the entries rowwise:")

for i in range(Row):		
	temp =[]
	for j in range(Col):	 
		temp.append(int(input()))
	B.append(temp)

	
result =[[0 for i in range(Col)] for j in range(Row)]

for i in range(len(A)):
 
    # iterating by column by B
    for j in range(len(B[0])):
 
        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
	print(r)
