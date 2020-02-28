class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    # function party(parameter){
    # parameter = parameter + 1
    # console.log('So far', parameter)

# this will create an instance of the class with an parameter
xy = PartyAnimal()

# using an as parameter, use party() function
xy.party()
xy.party()
xy.party()

# type() will return arrow bracket of what type it has
print("Type", type(xy))

# dir() will return list of methods and parameter used in the class
print("Dir", dir(xy))