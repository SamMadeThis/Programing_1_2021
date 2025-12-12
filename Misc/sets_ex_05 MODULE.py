#5.4. Sets

# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {};
# the latter creates an empty dictionary,
# a data structure that we discuss in the next section.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# show that duplicates have been removed

'orange' in basket                 # fast membership testing

'crabgrass' in basket
print ("\n----------------------------\n")
basket2= set(basket)
print("basket2")
print(basket2)
print ("\n----------------------------\n")
basket2.discard('banana')
print("basket2")
print(basket2)
print ("\n----------------------------\n")
print("basket")
print(basket)
print ("\n----------------------------\n")
basket2.add('quandong')
print("basket2")
print(basket2)
print ("\n----------------------------\n")
print("basket")
print(basket)
print ("\n----------------------------\n")
all_fruits = basket | basket2
print("all_fruits contains all fruits from both baskets without any duplicates")
print(all_fruits)
print ("\n----------------------------\n")
common_fruits = basket & basket2
print ("As the intersection of basket and basket2,")
print ("common_fruits contains only fruits that are common in both sets.")
print(common_fruits)

print ("\n----------------------------\n")
print ("The - (minus) operator can be used to get the difference between two sets:")
print(basket2 - basket)

print ("\n----------------------------\n")
print(basket - basket2)
