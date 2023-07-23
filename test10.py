# for loops

numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)

print(".....................................")

# using while loop

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

print(".....................................")
# range function

num = range(5)
print(num)

for i in num:
    print(i)

print(".....................................")

for x in range(5, 10):
    print(x)

print(".....................................")

for y in range(1, 20, 2):    # third value is step
    print(y)

