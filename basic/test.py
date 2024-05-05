# this is single comment

""""
    this is multiple comment
    this is multiple comment 1
    this is multiple comment 2
    this is multiple comment 3

"""

skill = "devops"

print(skill)


x, y, z, s1 = "alpha", "beta", 15, 11.2

print("variable x: ", x)
print("variable y: ", y)
print("variable z: ", z)
print("variable s1: ", s1)

print("variable x: %s" % x)
print("variable y: %s" % y)
print("variable z: %s" % z)
print("variable s1: %s" % s1)


# mutable - array
first_list = [12, 'string', 'string2', skill]
# push new item to array
first_list.append('kkkk')
print(first_list)

# immutable - tuple / collection of multi datatype
first_tuple = ('haha', 'ring', 'wedding', 2025)
print(first_tuple)

# dictionary
first_dictionary = {'name': 'Duongdx', 'province': 'HaNoi', 'Exercises': ['boxing', 'workout', 'pull up']}

print(first_dictionary)

# type

print('variable first_list is: ', type(first_list))
print('variable first_tuple is: ', type(first_tuple))
print('variable first_dictionary is: ', type(first_dictionary))