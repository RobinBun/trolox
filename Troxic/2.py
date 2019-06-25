
#goal: file1.py contains data, that should be used in 2.py
# file1.py contains adress data, in 2.py this adressdata has to be extended with name and phonenumber
# in 3.py the phone number gets changed to the number of brickspaces


from Troxic.file1 import *

robin()

def personal(list, name,phone_number):
    # add string to list
    list.extend([name, phone_number])


    # return
    return r

# save street and plz in string
result = robin()
name = 'Robin Bungarz'
phone_number = '01741906796'
result = personal(result, name, phone_number)
print(result)




#first try def robin(name,phone_number):
    # create list named r
#    r = [str, plz]
# add string to list

#    r.extend([name, phone_number])

#   return r

# save name and phone_number in string
#name = 'Robin Bungarz'
#phone_number = '01741906796'
#result = robin(name, phone_number)
#print(result)

