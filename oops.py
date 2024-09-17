#class and objects

class Mohit:
    age=21
    print("i'm from Lucknow")

#create object and pass class properties
x=Mohit()
print(x.age)


bornYear=int(input("enter born year"))
currentYear=int(input("enter current year"))
class AgeCalculator:
    AgeInYear=currentYear-bornYear
age=AgeCalculator()
print(age.AgeInYear)
