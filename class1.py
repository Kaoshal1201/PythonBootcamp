friendName=["Kaoshal", "Shubham", "Mohit"]
print("before", friendName )

#to add the new friend name in last 
friendName.append ("Kaoshal")

#print after adding name 
print("after",friendName)

#to add the name in specific position
friendName.insert(0,"Kaoshal Rai")
print("Add the name at index 0",friendName)

#to remove the name for list
friendName.remove ("Kaoshal Rai")

#print after removing name from the list 
print(friendName)

#to clear the list 
#friendName.clear()
#print (friendName)

friendName.pop(1)
print(friendName)

#to sort the list 
friendName.sort()
print(friendName)
for eveniio in range (2,11,2):
    print(eveniio)
for no in range(1,11):
    if no %2==0:
        print(no)
    tuple={"Mohit""Shubham""Kaoshal"} 
    print(type(set))
    sets = {"Mohit","Shubham","Kaoshal"}
    sets.add("Kaoshal")
    sets.remove("Kaoshal")
    #sets[0] = "Random"
    print(sets)
    print(type(sets))

#while print 1 to 10
# i = 1
# while i < 11:
#     print(i)
#     break
#     i=i+1


# while i < 11:
#     print(i)
#     continue
#     i=i+1

    def myfunction(x,y):
        z = x*y
        print("area is", z)

        width =int(input("enter the width"))
        hight =int(input("enter the hight"))

    myfunction(2,4) 

    
def myfunction(width,height):
    a=width*height
    return area

width =int(input("enter the width"))
height =int(input("enter the height"))

area =myfunction(width,height)