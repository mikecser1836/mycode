#!/usr/bin/env python3

##Created a dictionary
switch = {'hostname':'sw1','ip':'10.0.1.1', 'version':'1,2','vendor':'cisco'}

##Display parts of the dictionary
print("Prints hostname value:", switch['hostname'])
print("Prints ip value: ", switch['ip'])

## Request a 'fake'key
#print(switch['lynx'])

## request a 'fake' key
# print( switch['lynx'] )

##request a 'fake' key with .get() method
print("First test - .get()")
print("Requesting fake key:", switch.get('lynx'))
print()

print("Second test - .get()")
print(switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))
print()

print("Third test - .get()")
print(switch.get('version'))
print()

print("Fourth test - .keys()")
print(switch.keys())
print()

print("Fifth test - .values()")
print(switch.values())
print()

print( "Sixth test - .pop()" )
switch.pop('version') # removes this key (and value) pair
print( switch.keys() )   # notice the value of version is gone
print( switch.values() ) # notice the value 1.2
print()

print( "Seventh test - ADD a new value" )
switch['adminlogin'] = 'karl08'
print( switch.keys() )
print( switch.values() )
print()

print( "Eighth test - ADD a new value" )
switch['password'] = 'qwerty'
print( switch.keys() )
print( switch.values() )
