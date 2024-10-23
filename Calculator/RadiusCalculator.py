#vars
pi=3.14

#Define what the Calculator is for
print('Welcome, this calculator provides geometric values based on an inputted radius')

#Ask for user value
print('What is your radius?')
#Take Values, store as float
value = input()
value = float(value)

#Calculate Results
Diameter = value * 2
Circumference = 2 * pi * value
Area = pi * value ** 2
Volume = 4/3 * pi * value ** 3

#Print Results
print( 'Diameter =', Diameter) #print Diameter value * 2
print( 'Circumference =', Circumference)
print( 'Area =',Area)
print( 'Volume =',Volume)


