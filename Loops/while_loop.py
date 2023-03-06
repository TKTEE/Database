data = {'color': 'red',
           'fruit': 'apple',
           'pet': 'dog',
           'car':'sedan'}

iterator = iter(data)

while True:
    try:
        key = next(iterator)
        value = data[key]
        print(f'{key}: {value}')
    except StopIteration:
        break

        # Get the next key from the iterator
        # Get the value corresponding to the key
        # Do something with the key-value pair

        # The iterator has reached the end of the dictionary