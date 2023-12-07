#create a single string seperated with space from two string by swapping the character at position 1

a='abc'
b='xyz'
print("Before Swap :",a," ",b)
a1= a[:1] + b[1:]
b1= b[:1] + a[1:]

print("After swap:",a1," ",b1)
