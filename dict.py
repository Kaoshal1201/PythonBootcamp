#it can store multiple data in key value pair
#e.g.
myDict={
    "name":"kaushal rai",
    "email":"kasuhalk.rai971@gmail.com",
    "mobile":"9305766845"
}

print(type(myDict))

print(myDict)

for item in myDict:
    print(myDict[item])

for keys in myDict:
    print(myDict[keys])

print(myDict.get("email"))

myDict["name"]="Abhinay"
print(myDict)