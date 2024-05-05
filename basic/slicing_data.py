planet1 = 'Closest of Sun'

print(planet1)

print(planet1[1])
print(planet1[2])
print(planet1[3])
print(planet1[5])
print(planet1[-1])
print(planet1[-2])

# slicing a string, get substring from a string
print(planet1[0:4])
print(planet1[:]) # full string
print(planet1[:5])
print(planet1[11:])

print('-----------------------------------------')
print('|                slicing tuple          |')
print('-----------------------------------------')

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

# slicing a tuple
print(devops_tuple[0]) #linux
print(devops_tuple[3]) #jenkins
print(devops_tuple[-1]) #ansible
print(devops_tuple[2:4]) # return a tuple
print(devops_tuple[2:4][0]) # return a string
print('-----------------------------------------')
print('|                slicing list           |')
print('-----------------------------------------')
# slicing a list
print(devops_list[0]) #linux
print(devops_list[3]) #jenkins
print(devops_list[-1]) #ansible
print(devops_list[2:4]) # return a tuple
print(devops_list[2:4][0]) # return a string
print('-----------------------------------------')
print('|                slicing dict           |')
print('-----------------------------------------')
# slicing a dictionary
print(devops_dictionary['jenkins'][0])
print(devops_dictionary['ansible'])