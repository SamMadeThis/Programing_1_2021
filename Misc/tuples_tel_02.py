#Here is a small example using a dictionary:
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
tel['jack']
del tel['sape']
tel['irv'] = 4127
tel

list(tel)
# lists all the items
sorted(tel)
# sorts the list in alphabetical order
'guido' in tel
# returns true
'jack' not in tel
# returns false
