# Sort a list Permanently with the Sort() method

# Sort permanently and can never be reverted back
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sort a list temporarily
sort_2 = ['bmw', 'audi', 'toyota', 'subaru']
print("Here's the original list")
print(sort_2)

print("\nheres the sorted list:")
print(sorted(sort_2))
print("\nheres the original list again")
print(sort_2)

