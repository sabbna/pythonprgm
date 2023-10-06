list=["sabna","jilu","ishal","ghil","mazi","ridhu"]
count=0
print(list)
a=input("enter the letter to find the occurance\n")
for n in list:
    for f in n:
        if f==a:
            count+=1
print("number of",w,"is:",count)
