class PartyAnimal:
    x=0
    name= ''
    def _init_(self,name):
        self.name= name
        print(self.name,'constructed')

    def party(self):
        self.x= self.x + 1
        print(self.name,'party count',self.x)

class FootballFan(PartyAnimal): # FootballFan is a classs which extends PartyAnimal. it has all the capabilities of
                                #PartyAnimal and more
    points=0
    def touchdown(self):
        self.points= self.points + 7
        self.party()
        print(self.name,'points',self.points)
s= PartyAnimal('Sally')
s.party()

j= FootballFan('Jim')
j.party()
j.touchdown()