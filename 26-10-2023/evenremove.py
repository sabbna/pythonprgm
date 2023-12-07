#From a list of integers create a list removing even nos

list= [1,2,3,4,5]
print(list)
for i in list:
    if i%2==0:
          list.remove(i)
  
print("List after removing even numbers:")
print(list)
