# import module
import random

def orderFood(order_name, *args):
    print(f'you have ordered {order_name}')
    for dish in args:
        print(f'you have ordered {dish}')


print(orderFood('pork rib porridge', 'soup', 'salmon'))
print('--------------------------------------------')


def do_activity(*args, **kwargs):
    # args is a list
    print(args)
    # kwargs is a dict
    print(kwargs)
    for x in kwargs:
        print(kwargs[x])

    print('---------------------------')
    print('|      random choice       |')
    print('---------------------------')
    time = random.choice(args)
    activity = random.choice(list(kwargs.keys()))
    print(f'you should do {kwargs[activity]} during about {time}')


do_activity(
    10,
    15,
    20, 
    25,
    30,
    hobby='boxing',
    sport='jumping rope',
    learn='devops',
)