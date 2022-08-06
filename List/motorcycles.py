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


# Removing item using pop() removes the last item in a list but it lets you work
# with that item after removing it.

# note: can also pass index to remove item from any position

test_pop = ['honda','yamaha','suzuki']
print(test_pop)
popped_motorcycle = test_pop.pop()
print(test_pop)
print(popped_motorcycle)

# DEL vs POP. Use pop() when you need to do something with the removed item.