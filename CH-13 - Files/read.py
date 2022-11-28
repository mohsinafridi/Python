# f = open("C:\Practice Projects\Python\CH-13 - Files\python.txt","r")  # r -> read
# print("Read whole file: ", f.read())
# print("====================================")
# print("Read file Line : ", f.readline())
# print("Read file Line : ", f.readline())
# f.close()

print("====================================")
f1 = open("C:\Practice Projects\Python\CH-13 - Files\python.txt","a") # a - append ; w overwrite
f1.write("This is Addition in File using Python.")
f1.close()

f1 = open("C:\Practice Projects\Python\CH-13 - Files\python.txt","r")
print(f1.read())


print("====================================")

f2 = open("moo1.txt","r")
print("Read whole file: ", f2.read())

f3 = open("moo2.txt","w")