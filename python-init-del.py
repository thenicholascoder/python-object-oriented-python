class PartyAnimal:
    # initial value of x for method
	x = 0

    # __init__(self) = PYTHON CONSTRUCTOR, always run when class is created
	def __init__ (self):
		print('I am constructed')

    # method is a function inside a class
	def party(self):
		self.x = self.x + 1
		print('So far', self.x)

    # __del__(self) = PYTHON DECONSTRUCTOR, always run when class is destroyed, or overwritten 
	def __del__(self):
		print('I am destructed', self.x)

# call the class with an parameter
an = PartyAnimal()

# using an parameter, call party() method
an.party()
an.party()

# set variable
an = 42

# print variable
print('an contains', an)
