motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
motorcycles.append('test')
print(motorcycles)

#INSERTING elements into a list
# insert() method opens a space at position and stores the value. This 
# operation shifts every other value in the list one position to the right:

motorcycles = ['honda','yamaha', 'suzuki']
motorcycles.insert(0, 'American Idol')
print(motorcycles)


# Removing an item using the del statement
test_delete = ['honda','yamaha','suzuki']
print(test_delete)
del test_delete[0]
print(test_delete)