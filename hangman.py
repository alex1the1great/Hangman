from random import choice

# declare game variables.
words = ['python', 'javascript', 'java', 'swift', 'flutter', 'ruby']
word = choice(words)  # randomly choose a word from words list.
guessed, lives, game_over = [], 7, False

# create a list of underscores to the length of the word
guesses = ['_'] * len(word)

while not game_over:
    # output game information
    hidden_word = ''.join(guesses)
    print(f'Word to guesses: {hidden_word}')
    print(f'Lives: {lives}')

    user_letter = input('Guess a letter or type quit: ')
    print('-' * 50)  # line divider for UI

    if user_letter == 'quit':
        print('Thanks for playing')
        game_over = True
    elif user_letter in word:
        print('You guessed correctly!')
        # create a loop to change underscore to proper letter
        for i in range(len(word)):
            if word[i] == user_letter:
                guesses[i] = user_letter
    else:
        lives -= 1  # decrement live for wrong answer
        print('Incorrect, you lost a life.')
        if lives <= 0:
            print('You lost all your lives, you lost!')
            game_over = True
        elif word == ''.join(guesses):
            print('Congratulations, you guessed it correctly.')
            game_over = True
