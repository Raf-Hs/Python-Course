class Father():
    def skills(self):
        print ("gardening, programming")

class Mother():
    def  skills(self):
        #print ("I love cooking")
        print ("cooking,art")

class Child(Father,Mother):
    def  skills(self):
        #print ("I enjoy sports")
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c = Child()
c.skills()


    