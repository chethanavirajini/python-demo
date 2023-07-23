# flow controller
# c base programming use {} braces to show block of codes. but python use indentation for that


temperature = 25

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")

print("......................................")

# elif

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's nice day")
elif temperature > 10:
    print("It's bit cold")
else:
    print("It's cold")

print("......................................")
# Exercise

print("Exercise")

weight = float(input("Enter your weight: "))
unit = input("Enter unit: ")

if unit.upper() == "L":
    print("Weight in Kg: ", weight*0.453)
else:
    print("Weight in Kg: ", weight)





