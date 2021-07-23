import random 

randomNumber = random.randint(0,9)
print(randomNumber)

print('This is a number guessing game')

name = input('Enter your Name: ')
print('Hello ' + name)
chance = 0

while chance < 5:
  number = int(input('Guess a Number between 0 to 9: '))
  if chance < 6: 
    if number == randomNumber :
      print(' Congratulations You Won!')
      break
    else:
      print('Try once again')
      chance = 0
      
  elif not chance < 5:
    print('You Lose!')
  chance+=1        


    



 

