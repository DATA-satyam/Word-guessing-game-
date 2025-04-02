import random 
def choose_word():
    word =['python','java','javascript','html','css','csharp','ruby','swift','kotlin','typescript']
    return random.choice(word)


def word_status(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display+= '_'
    return display

print(word_status('python', ['p','y']))

def word_guessing_game():
    secet_word = choose_word()
    guessed_letters = []
    attempts = 7
    print('word guessing game')
    print('*******************')
    print('seceret word is:', word_status(secet_word, guessed_letters))
    while attempts>0:
        guess =input('guess a word:').lower()
        if len(guess)!=1 or not guess.isalpha():
            print('Please enter a single letter')
            continue
        if guess in guessed_letters:
            print('You already guessed that letter')
            continue
        guessed_letters.append(guess)

        if guess not in secet_word:
            attempts -= 1
            print (f"No letter'{guess}' occur in the word")
            print(f"you have {attempts} attempts remaining.")
        else:
            occurences = secet_word.count(guess)
            print(f"{guess} occurs {occurences}  times.")
        
        current_status = word_status(secet_word, guessed_letters)
        print("seceret word is", current_status)
        if "_" not in current_status:
            print("Congratulations! You guessed the word:", secet_word)
            break
    if "_" in current_status:
        print("Sorry! You ran out of attempts. The word was:", secet_word)
word_guessing_game()