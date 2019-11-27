import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print('주사위 두개의 숫자: {}, {}'.format(dice1, dice2))

print(random.randrange(0, 11, 2))

num1 = random.randrange(1, 10, 2)
num2 = random.randrange(0, 100, 10)
print('num1: {}, num2: {}'.format(num1, num2))

menu = ['a', 'b', 'c', 'd', 'e']
print(random.choice(menu))

print(random.sample(menu, 2))
