list1 = ['Beans', 'Wheat', 'Bread']
list2 = ['Rice', 'Plantain', 'Pizza', 'Spaghetti']

checked_str1 = 'Rice' # 1
print(checked_str1 in list1 and list2)


checked_str2 = 'Pizza'
print(checked_str2 in list2 or list1)

print(checked_str2 in list1 or list2) # returns whole list with the value in it.
