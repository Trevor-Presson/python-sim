#ACTIVITY DEMO 
# import csv

# class Activity: 
#     def __init__(self, name, need_effect, value):
#         self.name = name
#         self.need_effect = need_effect
#         self.value = value

# activityList = []
# with open('activities.txt', 'rb') as csvfile:
#      spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#      for row in spamreader:
#          activityList.append(Activity(name = row[0], need_effect = row[1], value = row[2]))

# for x in activityList: 
#     print(x.name, x.need_effect, x.value)

#Class with subclass 
class BigClass: 
    def __init__(self):
        self.name = "Trevor"
        self.LilClass = LilClass("Jeff")

class LilClass: 
    def __init__(self, church):
        self.church = "slick"

x = BigClass()
print (x.name, x.LilClass.church)


# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# element 'p' is searched
index = vowels.index('a')
print(index)

import math 
x2 = 100 
x1 = 50 
y2 = 100 
y1 = 50
dist = math.hypot(x2 - x1, y2 - y1)
print(dist)