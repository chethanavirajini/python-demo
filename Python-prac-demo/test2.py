# formatted string

first = 'John'
last = 'Smith'
message = first +' [' + last + '] '+ 'is a coder'  # string concatenation is too complicated.
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

print(".......................................")

course = 'Python for Beginners'
print(len(course))
print(course.upper())       # string acts as an object which methods can act on it
print(course)               # method does not chnage initial string
print(course.lower())
print(course.find('P'))
print(course.find('o'))
print(course.find('w'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print(course)
print('Python' in course)
print('python' in course)    # case sensitive
print(course.title())
