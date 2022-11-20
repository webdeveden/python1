# construting objects

class PartyAnimal:
    x=0

    name= ''
    def _init_(self, z):
        self.name= z
        print(self.name,'constructed')

    def party(self):
        self.x= self.x + 1
        print(self.x,'party count',self.x)

s= PartyAnimal('sally')
s.party()

j= PartyAnimal('jim')
j.party()
s.party()
