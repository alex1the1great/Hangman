from random import choice

# game variables.
words = ['python', 'javascript', 'java', 'swift', 'flutter', 'ruby']
word = choice(words)
wrong_guessed, lives, game_over = [], 7, False

# show word length using dash.
guesses = ['_'] * len(word)


# replace dash with user letter
def replace_dash(user_letter):
    for index in range(len(word)):
        if word[index] == user_letter:
            guesses[index] = user_letter


# Handle match letter from user.
def handle_match(user_letter):
    print('You guessed correctly.')

    replace_dash(user_letter)

    user_all_letter_join = ''.join(guesses)
    if user_all_letter_join == word:
        print('You have won the game.')

        # accessing global variable inside function.
        global game_over
        game_over = True

        print(f'Word: {word}')


# Handle not match letter from user
def handle_not_match(user_letter):
    global lives, game_over, wrong_guessed  # accessing global variable.
    lives -= 1
    print('Sorry, wrong letter.')

    wrong_guessed.append(user_letter)  # appending user letter.

    if lives <= 0:  # if all lives over.
        print('Sorry, all lives over.')
        game_over = True


while not game_over:
    # game information.
    correct_word = ''.join(guesses)
    print(f'Word to guesses: {correct_word}')
    print(f'Wrong guesses: {wrong_guessed}')
    print(f'Lives: {lives}')

    # prompt user for input
    user_letter = input('Enter a letter or type "quit": ')

    # convert user letter to lowercase & remove whitespaces.
    user_letter = user_letter.lower().strip()
    print('-' * 50)  # line divider for UI

    if user_letter == 'quit':
        print('Thanks for playing.')
        game_over = True
    elif user_letter in word:
        handle_match(user_letter)
    else:
        handle_not_match(user_letter)
