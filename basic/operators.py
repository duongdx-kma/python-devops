x=8
y=6

a = 19
b = 1

out = x < y
print(out)

out = not(x < y)
print(out)

out = (x < y) and (a > b)
print(out)

out = (x < y) or (a > b)
print(out)


# Membership operators
devops_tuple = ('linux', 'vagrant', 'aws', 'jenkins', 'ansible')
devops_list = ['linux', 'vagrant', 'aws', 'jenkins', 'ansible']
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
# tuple
print(devops_tuple)
print('linux' in devops_tuple)
print('linux' not in devops_tuple)

# list
print(devops_list)
print('linux' in devops_list)
print('linux' not in devops_list)

# dictionary
print(devops_dictionary)
print('aws' in devops_dictionary)
print('aws' not in devops_dictionary)
print('aws2' in devops_dictionary)
