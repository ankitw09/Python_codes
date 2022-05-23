s = input("Enter numbers seprated by comma: ")
list_numbers = s.split(',')
sum = 0
for num in list_numbers:
    sum += float(num)
print(sum)
