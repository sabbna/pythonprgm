#accept a filename from user and print extension of that

a=input("enter the file name:")
if '.' in a:
    b=a.split(".")
    print(b)
    print(b[1])
else:
    print("format is wrong")
