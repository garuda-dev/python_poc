
# 1) extracting values from a list using tuple unpacking

person = ['rock', 'lee', 16, 'm', 'black']
firstname, lastname, age, gender, hair = person

person = ['bob', 15, 'm', 'blue', 1.75]
name, age, *others = person

#others variable ‘catches’ all other variables that are not assigned. This is especially useful if our list has quite a lot of unnecessary data.


##2) use *args and **kwargs to unpack lists and dictionaries.

# func(*[1,2]) is sames as --->            func(1,2)
# func(**{'a':1, 'b':2})  is same as --->  func(a=1, b=2) 


#3) The built-in enumerate(list) function essentially generates both INDEX and ELEMENT of the list in 1 iteration.

fruits = ['apple', 'orange', 'pear']

for i, fruit in enumerate(fruits):
  print(i, fruit)

#4) The built-in zip function allows us to iterate through 2 or more lists at the same time.
fruits = ['apple', 'orange', 'pear']
prices = [4,5,6]

for fruit, price in zip(fruits, prices):
  print(fruit, price)
