name = input('Your name: ')
print(f'Hello {name}! Welcome to my quiz game. Do you want to play? (yes/no)')
answer = input('> ').strip().lower()
if answer == 'yes':
    print('game on! 😁')
    score = 0
    print('1. How many days are in a week? ')
    answer = input('> ').strip().lower()
    if answer in ['7', '7 days', 'seven', 'seven days']:
        print('Correct! ')
        score +=1
    else:
        print('Incorrect! ')
    print('2. How many ribs does the human skeleton have? ')
    answer = input('> ').strip().lower()
    if answer in ['24', '24 ribs']:
        print('Correct! ')
        score +=1
    else:
        print('Incorrect! ')
    print('3. How many keys does a piano have? ')
    answer = input('> ').strip().lower()
    if answer in ['88', '88 keys']:
        print('Correct! ')
        score +=1
    else:
        print('Incorrect! ')
    print('4. From which direction does the sun rise? ')
    answer = input('> ').strip().lower()
    if answer in ['east', 'east side', 'from the east', 'east direction']:
        print('Correct! ')
        score +=1
    else:
        print('Incorrect! ')
    print('5. In greek mythology, Who was the god of the sea? ')
    answer = input('> ').strip().lower()
    if answer == 'poseidon':
        print('Correct! ')
        score +=1
    else:
        print('Incorrect! ')
else:
    print('We are not playing...😔')

print(f'You got {score} answers right')
if score == 5:
    print('You were Excellent! 🎉')

elif score >= 3:
    print('You did a good job! 🫡')

else:
    print('Try again soon! 😔')