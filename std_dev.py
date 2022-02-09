#Name: Lilliana Parra
#Github user: ParraL1
#Date: 2/9/2022
#Description:getting the standard deviation of a list of peoples ages while keeping the ages private


class Person:
   def __init__(self, name, age):
      self.name = name
      self._age = age

#Making sure the age is private information using an underscore
def std_dev(person_list):
   m = 0
   for person in person_list:
      m += person._age
   m /= len(person_list)
   total = 0
   for person in person_list:
      total += (person._age - m) ** 2
   return (total / (len(person_list))) ** 0.5
#Using the exponent 0.5 to get the square root for the answer