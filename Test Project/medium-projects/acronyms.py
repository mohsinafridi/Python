user_input  = input(str("Enter any 2 words: ")).strip()

my_text = user_input.split()
a = ""

for i in my_text:
    a = a + i[0]

print("You input acroynm is ", a)