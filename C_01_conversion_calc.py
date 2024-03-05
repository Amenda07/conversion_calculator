#creating a dictionary
distance_dictionary= {
    "mm": 1000,
    'cm': 100,
    'm': 1,
    'km':.001
}

#get amount and units

amount= float (input("How much? "))
from_unit= input('From unit? ')
to_unit= input('To unit? ')

#look up value
multiply_by= distance_dictionary[to_unit] #ex;if km is input to to_unit then the input is searched up i the dictionary and whartevr is stord in it is used
standard= amount * multiply_by

divide_by= distance_dictionary[from_unit]
answere=standard/ divide_by

print(f'There is {answere} {to_unit}(s) in {amount} {from_unit}')

