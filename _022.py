'''
# Create a function that receives a list and a function that receives
a list and a function. The function passed will return True or False
if a list value is odd.
The surrounding function will return a list of odd numbers
'''

'''
create function that takes func into another list
pass that function into another list. Use that function against list
to generate list of odd numbers
'''

def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list, func):
    oddList = []

    for i in list:
        if func(i):
            oddList.append(i)
    return oddList

aList = range(1,50)
print(change_list(aList, isOdd))

#returns list of 1..to 49
