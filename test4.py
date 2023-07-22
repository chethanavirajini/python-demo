# technically string is also an object which means it has some capabilities.
# remote controller as an object. it can TV on, TV off and changing Tv channels
# String is an immutable, can not change them, it creates new string in a memory when we try to change them

course = 'Python for Beginners'
print(course.capitalize())
print(course.upper())    # return a new string. does not change initial string
print(course.lower())
print(course.find('y'))
print(course.find('Y'))
print(course.find('for'))
print(course.replace('for', '4'))
print('Python' in course)

