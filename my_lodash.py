# Removes leading and trailing whitespace or specified characters from string.
def trim(my_string):
    
    return my_string

# Reverses array so that the first element becomes the last, the second element becomes the second to last, and so on.
def reverse(my_array):

    return my_array

# Creates a duplicate-free version of an array, using SameValueZero for equality comparisons, in which only the first occurrence of each element is kept. 
# The order of result values is determined by the order they occur in the array.
def uniq(my_array):

    return my_array

# This method is like uniq except that it accepts iteratee which is invoked for each element in array to generate the criterion by which uniqueness is computed. 
# The order of result values is determined by the order they occur in the array.
# The values returned are not transformed with the iteratee, they are kept the same.
def uniq_by(my_array, transform_function):

    return my_array

# Iterates over elements of collection, returning the first element predicate returns truthy for. 
# The predicate is invoked with three arguments: (value, index|key, collection).
def find(my_array, predicate_function):

    return my_array

# Creates an array of elements, sorted in ascending order by the results of looking up each element's fieds specified in the fields array.
# This method performs a stable sort, that is, it preserves the original sort order of equal elements. 
def sort_by(my_array, fields):

    return my_array

# Creates an object composed of keys generated from the results of running each element of collection thru iteratee. 
# The order of grouped values is determined by the order they occur in collection. 
# The corresponding value of each key is an array of elements responsible for generating the key. 
# The iteratee is invoked with one argument: (value).
def group_by(my_array, transform_function):

    return my_array

# Recursively flattens array.
def flatten_deep(my_array):

    return my_array

# This method is like _.defaults except that it recursively assigns default properties.
def defaults_deep(my_object, extra):

    return my_object

# Creates an array of unique values that is the symmetric difference of the given arrays. 
# The order of result values is determined by the order they occur in the arrays.
def xor(my_array, my_array2):

    return my_array
