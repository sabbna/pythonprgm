a=input("enter the sentence\n")
b=input("\nenter the word to search\n")
list=a.split()
count=0
for w in list:
    if w==b:
        count =count+1
print("no.of words repeated:",count)
