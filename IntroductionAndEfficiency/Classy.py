"""
You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!
"""

class Classy(object):
    def __init__(self):
        self.items = []
        
        
    def addItem(self, item):
        self.items.append(item)
        print("added item= " +str(item)) 
        
    def getClassiness(self):
        classinessPoints=0
        print("in gC")  
        print("items[] = " + str(self.items))  
        for i in self.items:    
            if i == "tophat":
                classinessPoints += 2
                print("tophat classinessPoints= " +str(classinessPoints)) 
            elif i== "bowtie":
                classinessPoints += 4 
                print("bowtie classinessPoints= " +str(classinessPoints))           
            elif i == "monocle" :
                classinessPoints += 5
                print("monocle classinessPoints= " +str(classinessPoints)) 

        return classinessPoints
        

# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())


    # def addItem(self, item):
    #     self.items.append(item)
    #     print("added item= " +str(item)) 
        
    # def getClassiness(self):
    #     classinessPoints=0
    #     print("in gC")  
    #     print("items[] = " + str(self.items))  
    #     for i in self.items:    
    #         if i == "tophat":
    #             classinessPoints += 2
    #             print("tophat classinessPoints= " +str(classinessPoints)) 
    #         elif i== "bowtie":
    #             classinessPoints += 4 
    #             print("bowtie classinessPoints= " +str(classinessPoints))           
    #         elif i == "monocle" :
    #             classinessPoints += 5
    #             print("monocle classinessPoints= " +str(classinessPoints)) 

    #     return classinessPoints