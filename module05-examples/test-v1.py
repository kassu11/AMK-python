firstNames = ["John", "Jane", "Joe", "Jill", "Jack", "Jenny"]

print(firstNames[0])
print(firstNames[2])
print(firstNames[-2])
print(firstNames[1:3])
print(firstNames[3:3])

print(firstNames[-3:-1])
print(firstNames[-1][0:-1])

print(firstNames[0:5:2])

num = [1,2,3,4,5,6,7,8,9,10]

print(num[1::2])
print(num[:-3])

firstNames.remove("Joe")

firstNames.extend(num)

print(num)
print(firstNames)

print(firstNames.index(5)) # Palauttaa index numeron

if "Jill" in firstNames:
  print("Jill on listalla")

firstNames = ["John", "Jane", "Joe", "Jill", "Jack", "Jenny"]
firstNames.sort()

print(firstNames)