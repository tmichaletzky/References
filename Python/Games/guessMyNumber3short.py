import random

print('Hello')
name = input()

print('Hello ' + name)
sN = random.randint(1,20)

for taken in range(1,7):
    print('Guess')
    guess = int(input())

    if guess < sN:
        print('Low')
    elif guess > sN:
        print('High')
    else:
        break

if guess == sN:
    print('Nice')
else:
    print('It was ' + str(sN))
