print('We are playing FizzBuzz. \n Please enter an integer')
total = int(input())
for i in range (1,total+1):
    if i % 3 != 0 and i % 5 != 0: # none of them
        print(i)
    elif i % 5 != 0: #  if none of them and not 5 then only 3
        print('Fizz')
    elif i % 3 != 0: # then 5 but not 3
        print('Buzz')
    else:
        print('FizzBuzz')
            
