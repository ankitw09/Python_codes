def IsIn(stringfirst, stringsecond):
    if stringsecond in stringfirst:
        return True
    elif stringfirst in stringsecond:
        return True
    else:
        return False
       
if __name__ == '__main__':
    stringfirst = input("Enter first string:")
    stringsecond = input("Enter first string:")
    if IsIn(stringfirst, stringsecond):
        print("YES")
    else:
        print("NO")
