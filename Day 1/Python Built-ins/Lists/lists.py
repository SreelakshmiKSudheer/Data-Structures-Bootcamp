fruits = ['apple', 'banana', 'cherry']

'''Basic operations'''
print(fruits[0])        # Indexing → 'apple'
print(fruits[-1])       # Negative Indexing → 'cherry'

fruits[1] = 'blueberry' # Updating value
print(fruits)           # ['apple', 'blueberry', 'cherry']

print(len(fruits))      # Length → 3

print('apple' in fruits) # Membership → True

# Iteration
for fruit in fruits:
    print(fruit)

'''LIst methods'''
# Adding
fruits.append('date')               # Add at end
fruits.insert(1, 'banana')          # Add at specific index
fruits.extend(['elderberry', 'fig'])# Add multiple items

# Removing
fruits.remove('banana')             # Removes first occurrence
popped = fruits.pop()               # Removes last item
fruits.pop(1)                       # Removes by index
fruits.clear()                      # Removes all elements

# Re-adding for more examples
fruits = ['apple', 'banana', 'cherry', 'banana']

# Searching and Counting
index = fruits.index('banana')     # First index of 'banana'
count = fruits.count('banana')     # Count occurrences

# Sorting and Reversing
fruits.sort()                      # Ascending order
fruits.sort(reverse=True)          # Descending order
fruits.reverse()                   # Just reverse, not sort

# Copying
new_fruits = fruits.copy()         # Shallow copy

# Combining
more_fruits = fruits + ['grape', 'honeydew']


fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Basic Slicing
print(fruits[1:4])     # ['banana', 'cherry', 'date']
print(fruits[:3])      # ['apple', 'banana', 'cherry']
print(fruits[3:])      # ['date', 'elderberry', 'fig', 'grape']
print(fruits[-3:])     # ['elderberry', 'fig', 'grape']
print(fruits[:-2])     # ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(fruits[:])       # ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# Slicing with Step
print(fruits[::2])     # ['apple', 'cherry', 'elderberry', 'grape']
print(fruits[1::2])    # ['banana', 'date', 'fig']
print(fruits[::-1])    # ['grape', 'fig', 'elderberry', 'date', 'cherry', 'banana', 'apple']
