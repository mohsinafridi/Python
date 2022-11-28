# Tuple are Immutable.Once created ,it is not updated.
# but there are some ways around.
# Same for Update Operation as well.
# Tuple Can Update.


x = ("apple", "banana", "cherry","Mohsin")
y = list(x)
print(y)
y[1] = "kiwi"
y[3] = "Mohsin"
x = tuple(y)

print(x)

# Add (1) element in Tuple
test = ("1","2")
y = list(test)
y.append("3")
x = tuple(y)
print("Add (1)",x)

# Add (2)
test = (1,2)
new = (3,)
test+=new
print("Add (2)",test)