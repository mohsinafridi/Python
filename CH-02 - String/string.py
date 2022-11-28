str_1 = "Mohsin Azam Afridi"

print(str_1)

#index
str_1 = "Mohsin Azam Afridi"
print(str_1[2])

print("apple"[4])

# slices
ex_10 = "apricots"
print(ex_10[:3])
print(ex_10[2:5])
print(ex_10[4:])


#concaten
concatenate = "Mo" + "" + "hsin"
print(concatenate)
print(str_1[5])

# Multiline String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Length
a = "Hello, World!"
print("Length is :", len(a))

# Check in string
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if True:
  print("Yes, 'free' is present.")