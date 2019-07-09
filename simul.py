import random
import csv
import math

slamdict = {"hand" : "Slurp"}

#Classes---------------------------------------------
class Person:
  def __init__(self, name, age, income, assets, family_id, address_id):
    self.name = name
    self.age = age
    self.income = income
    self.assets = assets
    self.Attributes = Attributes()
    self.Needs = Needs()
    self.Family = Family(family_id)
    self.Address = Address(address_id)

class RealEstate: 
    def __init__(self, property_type, value, testdict):
        self.property_type = property_type
        self.value = value 
        self.testdict = { swag: 'Slam', jeff: 'yeet'}

class Activity: 
    def __init__(self, name, need_effect, value):
        self.name = name
        self.need_effect = need_effect
        self.value = value

class Attributes: 
    def __init__(self):
           self.charisma = random.randint(1, 10)
           self.strength = random.randint(1,10) 
           self.intelligence = random.randint(1,10)

class Needs: 
    def __init__(self):
        self.hygiene = 10
        self.social = 10 
        self.hunger = 10 
        self.thirst = 10 
        self.fun = 10 
 
class Family: 
    def __init__(self, family_id):
        self.family_id = family_id

class Address: 
    def __init__(self):

#Simulation Actions-------------------------------------------------

#Income
def earn_income(peoplelist):
    for x in peoplelist: 
        x.assets += x.income

#Pay Bills 
def pay_bills(peoplelist):
    for x in peoplelist: 
        x.assets -= x.income

# def start_activity(peoplelist):
#     for j in peoplelist: 
#         if j.Needs.fun == 10: 
           
            #y = filter(x.need_effect == "Hygiene" for x in activityList)
        
        #Grab record and apply

def subtract_needs(peoplelist):
    for x in peoplelist: 
        x.Needs.hygiene -= 1 
        x.Needs.social -= 1 
        x.Needs.hunger -= 1 
        x.Needs.thirst -= 1 
        x.Needs.fun -= 1

#Navigation 


        





#Read in randomizer lists-------------------------------------------
#Read in name options
# mylines = []                             
# with open ('names.txt', 'rt') as myfile: 
#     for myline in myfile:               
#         mylines.append(myline)

peoplelist = []
with open('names.txt', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         peoplelist.append(Person(name = row[0], age = random.randint(1, 80), income = random.randint(100, 1000), assets = 0, family_id = row[1], address_id = row[2]))

#Read in activity list
activityList = []
with open('activities.txt', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in spamreader:
         activityList.append(Activity(name = row[0], need_effect = row[1], value = row[2]))


#Create 10 People and add to list
# peoplelist = []
# i = 0 
# while i < 5:
#     peoplelist.append(Person(name = mylines[random.randint(0, 4)], age = random.randint(1, 80), income = random.randint(100, 1000), assets = 0))
#     i += 1


#Day Simulation------------------------------------------------------------
x = 0 
while x < 14: 
    x += 1
    #Earn Income
    if x % 7 == 0: 
        earn_income(peoplelist)
    #Pay Bills
    if x % 30 == 0:
        pay_bills(peoplelist)
    #start_activity(peoplelist)
        
        
#Print Output
for j in peoplelist:
    print(j.name, j.age, j.income, j.assets, j.Needs.fun)
    