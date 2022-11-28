# Delete a File

import os

# os.remove("moo2.txt")

if os.path.exists("moo2.txt"):
    os.remove("moo2.txt")
else:
  open("moo2.txt","w")    
  