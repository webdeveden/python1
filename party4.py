class PartyAnimal:
    x=0

    def _int_(self):
        print('I am constructed')

    def party(self):
        self.x= self.x + 1
        print('So far', self.x)

    def _del_(self):
        print('I am destructed', self.x)

an= PartyAnimal()
an.party()
an.party()
an.party()
an= 42
print('an contains',an)
