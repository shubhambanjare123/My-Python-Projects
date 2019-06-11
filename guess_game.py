count = 0
while count<3:
    guess = int(input('Guess: '))
    print(guess)
    count += 1
    if guess == 9:
        print('you won')
        break
else:
    print('you loose')

input()
