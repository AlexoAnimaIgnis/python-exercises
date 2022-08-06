alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

# dictionary is a collection of key-value pairs.
# Each key is connected to a value and you can use
# key to access the value associated with that key.


# When you provide a key, python returns the associated value

# Dictionaries are dynamic structures and you can add
# new key-value pairs to a dictionary any time.
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# modifying values in a dictionary
# To modify a value in a dictionary, 
# give the name of the dictionary with the key in square 
# brackets and then the new value 
# you want associated with that key

alien_0 = {'color': 'green'}
print(f"Alien original color: {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"Alien new color: {alien_0['color']}")

alien_0 = {'color': 'green','points':5}
del alien_0['points']
print(alien_0)