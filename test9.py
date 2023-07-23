# lists - when we want to represent the list of objects , can be list of numbers, names etc..

names = ['John', 'Bob', 'Mosh', 'Sam', 'Marry']

print(names)
print(names[0])
print(names[1])
print(names[-1])
print(names[-2])
names[0] = 'Jon'
print(names)

print(names[0:3])  # represent objets start with start element and excluding end element

print("................................................")

# any of print statement list will not be chnages but it creates new list


# list method - like a object list having capabilities,

numbers = [ 1, 2, 3, 4, 5 ]
numbers.append(6)
numbers.insert(0, 9)
numbers.remove(3)

#numbers.clear()
print(numbers)
print(1 in numbers)
print(10 in numbers)
print(len(numbers))

















