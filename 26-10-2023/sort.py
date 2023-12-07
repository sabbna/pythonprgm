import operator
dict={1:2,5:4,4:3,2:1,0:0}
print("orginal dictionary",dict)
sorted_dict=sorted(dict.items(),key=operator.itemgetter(1))
print("ascending order",sorted_dict)
sorted_dict=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
print("descending order by values:",sorted_dict)
