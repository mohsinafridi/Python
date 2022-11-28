# Python Try Except

# print(x) # NameError: name 'x' is not defined

try:
    print(x);
except SyntaxError:
   print("Syntax error") 
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") 
finally:
    print("Error found!hence I run")  