motors = ["lexus", "benz", "Toyota", "Camry", "Sienna" ]
motors[0] = "GLK"
motors[2] = "Voxwagon"
print(motors)

#duplicated list(duplicated lexus even after replacing)
motors = ["lexus", "benz", "Toyota", "Camry", "Sienna", "lexus" ]
motors[0] = "GLK"
motors[2] = "Voxwagon"
print(motors)

#appending lists ie to add a new value to the list
motors = ["lexus", "benz", "Toyota", "Camry", "Sienna" ]
motors[0] = "GLK"
motors[2] = "Voxwagon"
motors.append("jeep")
print(motors)

#sorting of ists
motors = ["lexus", "Benz", "Toyota", "Camry", "Sienna" ]
motors[0] = "GLK"
motors[2] = "Voxwagon"
motors.sort()
print(motors)

#to sort in descending/reverse order
motors = ["Lexus", "Benz", "Toyota", "Camry", "Sienna" ]
motors[0] = "GLK"
motors[2] = "Voxwagon"
motors.sort(reverse=True)
print(motors)

#using index method


motors = []
motors.append("Lexus")
motors.append("jeep")
motors.append("Camry")
motors.append("Sienna")
print(motors)

#removing value from a list using remove method
fruits = ["apple", "apple", "banana", "mango"]
fruits.remove("apple")
fruits.remove("banana")
print(fruits)

#removing using index by pop method
fruits = ["apple", "apple", "banana", "mango"]
fruits.pop(1)
print(fruits) 


#printing list in a loop(range)
fruits = ("apple", "apple", "banana", "avacado")
for a in range (len(fruits)):
    print(fruits[a])

fruits = ("apple", "apple", "banana", "avacado")
for fruit in range (len(fruits)):
    print(fruits[fruit])


#dot-copy method
fruits = ["apple", "apple", "banana", "avacado"]
myfruits = fruits.copy()
print(myfruits)

#difference between slicing and range
fruits = ["apple", "apple", "banana", "avacado"]
myfruits = fruits[:2]
print(myfruits)