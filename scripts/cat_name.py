#! python3
# cat_name.py is a script for a demonstration of how to take inputs from user as long as user giving input and also store them and aldo it shoes how list can be used to store similar vlues.

cat_names = []

while True:
    print('Enter name of cat no.' + str(len(cat_names) + 1) + ' (or nothing to stop)')
    name = input()
    if name == '':
        break
    else:
        cat_names += [name]

print('Entered cat names are:')
for name in cat_names:
    print(name, end = ' ')

print()

