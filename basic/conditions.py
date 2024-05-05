x = 46

if x < 30:
    print('x less then 30')
elif 30 <= x < 45:
    print('(x great then 30 or x equal 30) and  less then 45')
else:
    print('x great then 45')

print('out of condition scope')

os = 'linux'

switcher = {
    'linux': 'os is a linux system',
    'window': 'os is a window system',
    'macos': 'os is a macos system',
}

print(switcher.get(os, 'os is a DOT system'))

DevopsSkill = ['Jenkins', 'aws', 'gg cloud', 'azure', 'ansible']
DevelopSkill = ['javascript', 'react', 'vue']
preferredCountry = {'1': 'england', '2': 'Vietnamese', '3': 'russia'}

user_skill = input('enter your skill:')
user_nationality = input('enter your nationality:')

print("the type:", type(preferredCountry))

if (user_skill in DevopsSkill) or (user_nationality in preferredCountry.values()):
    print('you passed')
    print(f"we have {user_skill} in devops team or {user_nationality} is preferred country")
elif (user_skill in DevelopSkill) or (user_nationality in preferredCountry.values()):
    print('you passed')
    print(f"we have {user_skill} in Develop team or {user_nationality} is preferred country")
else:
    print('see you in the next interview')
