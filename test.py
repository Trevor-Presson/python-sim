import random

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)



mylines = []                             
with open ('names.txt', 'rt') as myfile: 
    for myline in myfile:               
        mylines.append(myline)

i = 1
while i < 3:
  print(i)
  i += 1
  p1 = Person(mylines[random.randint(0, 4)], 36)
  p1.myfunc()



# import csv
# csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)

# with open('names.txt', "rb") as csvfile:
#     for row in csv.DictReader(csvfile, dialect='piper'):
#         print row['name']



#Read the name file 


