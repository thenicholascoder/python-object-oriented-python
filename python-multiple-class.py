# create a template called PartyAnimal
class PartyAnimal:

    # variables
    x = 0
    name = ''

    # CONSTRUCTOR
    # self is variable calling the template itself
    # nam is the second parameter that will be sticked
    # inside self
    def __init__(self, nam):

        # the name from self is assigned to nam
        self.name = nam

        # print the parameter
        print(self.name, 'constructed')

    # method
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

# parameter of class will be passed inside self.name and then equal to nam
s = PartyAnimal('Sally')
s.party()

# parameter of class will be passed to self .name then passed to nam
j = PartyAnimal('Jim')

j.party()
s.party()

