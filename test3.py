# Three types of data types - numbers , String and Boolean
# variable can be converted into one type to another

birth_year = input("Enter your birth year? ")
# age = 2023 - birth_year

# print(age)  Error message is coming due to the different data types
# input gives always string value "1995" not 1995

correct_age = 2023 - int(birth_year)
print(correct_age)

# built-in function converting values of data types
int()
str()
float()
bool()

# Exercise 2

first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))

Sum = first_num + second_num

print("Sum: " + str(Sum))

# if we are not declare the data type as float or int this will take this as a string
# "10.1" + "20" = "10.120" as a string value


