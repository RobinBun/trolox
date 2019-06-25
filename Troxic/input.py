#input gives you the possibility to
name = input('What is your name? ')
color = input('What is your favorite color? ')

print(name + ' likes ' + color)

#next

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)

weight_kg = input('What is your weight (kg)? ')

#to multiply an input with a float, you have to int() float() around it.

weight_lbs = float(weight_kg) * 2.20464

print(weight_lbs)