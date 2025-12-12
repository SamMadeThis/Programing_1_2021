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

