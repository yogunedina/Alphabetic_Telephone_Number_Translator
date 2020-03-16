'''
Author: Yewande Ogunedina
This is an Alphabetic Telephone Number Translator that returns complete number
Course: ITMD513 
'''

#Define telephone as a variable

telephone = input("Enter telephone number in 555-XXX-XXXX format: ")
newPhone = ''

#Assign alpabets to a variable 
for string_1 in telephone:
    if string_1 == 'A' or string_1 == 'B' or string_1 == 'C':
        string_1 = '2'
    elif string_1 == 'D' or string_1 == 'E' or string_1 == 'F':
        string_1 = '3'
    elif string_1 == 'G' or string_1 == 'H' or string_1 == 'I':
        string_1 = '4'
    elif string_1 == 'J' or string_1 == 'K' or string_1 == 'L':
        string_1 = '5'
    elif string_1 == 'M' or string_1 == 'N' or string_1 == 'O':
        string_1 = '6'
    elif string_1 == 'P' or string_1 == 'Q' or string_1 == 'R' or string_1 == 'S':
        string_1 = '7'
    elif string_1 == 'T' or string_1 == 'U' or string_1 == 'V':
        string_1 = '8'
    elif string_1 == 'W' or string_1 == 'X' or string_1 == 'Y' or string_1 == 'Z':
        string_1 = '9'

#assign newphone to char
    newPhone = newPhone + string_1
#print the telephone number 
print("Your number translates to", newPhone)
