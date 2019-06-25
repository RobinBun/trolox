
#goal: file1.py contains data, that should be used in 2.py
# file1.py contains adress data, in 2.py this adressdata has to be extended with name and phonenumber
# in 3.py the phone number gets changed to the number of brickspaces

#theory which you should learn:
## how does python work
## data types
## what are data frames (of python - import pandas - extra task - convert list to data frame)

def robin(str,plz):
    # create list named r
    r = []

    # add string to list
    r.extend([str, plz])


    # return
    return r

# save street and plz in string
strasse = 'Am Steinrücken 5'
postleitzahl = '58453'

result = robin(strasse,postleitzahl)
print(result)


