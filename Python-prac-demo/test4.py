# using for loop

for i in range(0, 9):
    print(i)

print(".......................................")
# using while loop

count = 0
while count < 9:
    print(count)
    count = count + 1
print("Done")

print(".......................................")
# guessing game

secret_number = 13
chance = 0


while chance < 3:
    guess_number = int(input("input number: "))
    if guess_number < 13:
        print("Number is too small")
    elif guess_number > 13:
        print("Number is too large")
    elif guess_number == 13:
        print("Congratulations, You won")
        break
    chance = chance + 1
else:
    print("Better luck next time")

print(".......................................")

num = int(input("number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial*i
    print(factorial)
print(factorial)