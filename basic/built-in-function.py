ipTuple = ('192', '168', '2', '9')

ip = ('.'.join(ipTuple))

print('your ip is: ', ip)
print('your ip is: ', ('-'.join(ipTuple)))

mobileBrand = ['iphone', 'samsung']
# insert data to list
mobileBrand.extend(['nokia', 'lg'])
print(mobileBrand)

# insert data to index
mobileBrand.insert(2, 'xiaomi')
print(mobileBrand)

# delete last value
mobileBrand.pop()
# delete 2 position value
mobileBrand.pop(2)
print(mobileBrand)

devops_dictionary = {
    'linux': "don't",
    'vagrant': "don't",
    'aws': 'done',
    'jenkins':
        [
            'authorization',
            'authentication',
            'pipeline',
            'multibranch-pipeline'
        ],
    'ansible': "don't"
}

# get list key
print(devops_dictionary.keys())

keyList = list(devops_dictionary.keys())
print(keyList[0])


