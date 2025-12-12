# Using set() on a sequence eliminates duplicate elements.
# The use of sorted() in combination with set() over a sequence
# is an idiomatic way to loop over unique elements of the sequence in sorted order.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
