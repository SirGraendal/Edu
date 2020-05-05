import random

debug = False
cmd = ""


def game(choice):
    select = ['python', 'java', 'kotlin', 'javascript']
    secret_word = select[choice] if debug else random.choice(select)
    lives = 8
    guessed = set()
    valid = set("abcdefghijklmnopqrstuvwxyz")
    hint = list("-" * len(secret_word))
    if debug:
        print("Secret word:", secret_word)
        print("Valid: {}\n".format(valid))

    while lives:
        if debug:
            print("Tries:", lives)
            print("Guessed:", guessed)

        print("\n"+"".join(hint))
        guess = input("Input a letter:")

        if len(guess) != 1:
            print("You should print a single letter")
        elif guess in guessed:
            print("You already typed this letter")
        elif guess not in valid:
            print("It is not an ASCII lowercase letter")
        elif guess not in secret_word:
            print("No such letter in the word")
            guessed.add(guess)
            lives -= 1
            if not lives:
                print("You are hanged!\n")
        elif guess in secret_word:
            guessed.add(guess)
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    hint[i] = guess
            if hint == secret_word:
                print("\n{}".format(secret_word))
                print("You guessed the word {}".format(secret_word))
                print("You survived!")
                break


print("H A N G M A N")

while not cmd == "exit":
    cmd = input('Type "play" to play the game, "exit" to quit:')

    if cmd == "play":
        game(3)
