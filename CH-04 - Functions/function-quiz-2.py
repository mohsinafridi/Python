# Volume of Rectangular Prism

length = int(input("Enter Length: "))
height = int(input("Enter height: "))
width = int(input("Enter width: "))

def calculateRectangularPrism(l,w,h):
     return l*w*h
 

print("Volume is ",str(calculateRectangularPrism(length,height,width)))