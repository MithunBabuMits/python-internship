#Python program to create a list, a dictionary, and a set. Perform basic operations like adding, removing, and modifying elements.

#list
fruits = ['apple','orange','banana']
print(fruits)
fruits.append('pineapple')
fruits.remove('apple')
fruits.insert(1,123)
print(fruits)

#dictionary

vehicle = {1:"car",2:"bus",3:"auto"}
print(vehicle)
vehicle[4] = 'train'
vehicle.pop(1)
print(vehicle)

#set

animals = set(["cat","dog","elephant"])
animals.add("monkey")
animals.remove("cat")
print(animals)