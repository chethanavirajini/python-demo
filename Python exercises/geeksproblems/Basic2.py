# Method 1

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print("Highest number: ", x)
else:
    print("Highest number: ", y)


# Method 2

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
num = [a, b]
print(num)
num = num.sort()
print(num[-1])
