# Define dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Access keys
for key in my_dict.keys():
    print(key)  # Outputs each key: 'a', 'b', 'c'

# Access value
for value in my_dict.values():
    print(value)  # Outputs each value: 1, 2, 3

# Access key,value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")  # Outputs key-value pairs
    # Key: a, Value: 1
    # Key: b, Value: 2
    # Key: c, Value: 3