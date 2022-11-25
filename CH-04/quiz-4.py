from  random import randint

fuel = randint(10,25)
miles = randint(200,400)

#MPG Mile per Gallon
# miles//gallons

print("The Car can travel " + str(miles//fuel) +" miles per gallon.")