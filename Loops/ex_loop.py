data = {'color': 'red',
           'fruit': 'apple',
           'pet': 'dog',
           'car':'sedan'}

keys = list(data.keys())
i = 0
while i < len(keys):
        key = keys[i]
        value = data[key]
        print(key + ':' + value)
        i+=1
