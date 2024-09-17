print("kaoshal rai")

name=input("Enter your name")
print(name)

#wap to find the current age
currentYear=int(input("enter the current year"))
bornYear=int(input("enter the born year"))
ageInYear=currentYear-bornYear
print(ageInYear)

#wap for currency convertor
print("convert dollar into rupees")
dollarAmount=int(input("enter the amount in Dollar"))
dollarIntoRs=(dollarAmount*84)
print(dollarAmount,"converted",dollarIntoRs)

#wap to check you are elligible for voting
age=int(input("enter your age"))
if(age>=18):
 print("you are elligible for voting ")       
else:
 print("you are not elligible for voting")


 #wap to check the user  is eligible for job application 
 #if gender is female and age is greater than 17
 #if gender is male then they can apply for private job
age=int(input("enter your age"))
gender=input("enter your gender")
if(age>=18 and gender=="female"):
 print("you are eligible for government job")
elif(age>= 18 and gender=="male"):
 print("you are eligible for private job")
else:
 print("you are not eligible for any job")
 
 #method 2
if(age>17):
  if(gender=="female"):
    print("you are eligible for govt job")
  elif(gender=="male"):
    print("you are eligible for private job")
  else:
    print("your gender does not exist")
else:
    print("you r not eligible for any job")


        
#wap to check the greatest no among 3 no
a=int(input("first no."))
b=int(input("second no."))
c=int(input("third no."))
if(a>b and a>c):
  print("a is greater")
elif(b>a and b>c):
  print("b is greater")
else:
  print("c is greater")     

