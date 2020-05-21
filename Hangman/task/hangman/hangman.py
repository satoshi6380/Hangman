# Write your code here
import random
from string import ascii_lowercase

li = ('python', 'java', 'kotlin', 'javascript')
answer = random.choice(li)
word = '-' * len(answer)
typed = set()

print('H A N G M A N')

while input('Type "play" to play the game, "exit" to quit:') != 'play':
    if 'exit':
        exit()

count = 1
while count <= 8:
    print()
    print(word)
    letter = input('Input a letter:')
    if len(letter) != 1:
        print('You should print a single letter')
    elif letter in typed:
        print('You already typed this letter')
    elif letter not in ascii_lowercase:
        print('It is not an ASCII lowercase letter')
    elif letter not in answer:
        print('No such letter in the word')
        count += 1
    else:
        for i in range(len(answer)):
            if answer[i] == letter:
                word = word[:i] + letter + word[i + 1:]
        if word == answer:
            break
    typed.add(letter)

print('You are hanged!' if '-' in word else 'You guessed the word!\nYou survived!')
# print()
# print('Thanks for playing!')
# print("We'll see how well you did in the next stage")
