list1 = ["a","s","f","d","r","w","b","c","j"]
# new_list = list1.copy() #1
new_list = list(list1) #2
print(new_list)

# JOIn list

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)