import random


class Hangman:
    def __init__(self, words):
        self.words = words
        self.word = self.choose_word()
        self.guesses = []
        self.remaining_guesses = 6

    def choose_word(self):
        return random.choice(self.words)

    def update_display(self):
        display = ""
        for letter in self.word:
            if letter in self.guesses:
                display += letter
            else:
                display += "_"
        return display

    def check_win(self):
        for letter in self.word:
            if letter not in self.guesses:
                return False
        return True

    def play_game(self):
        print("Welcome to the Medical Claims Hangman Game!")
        print("The word has {} letters. You have 6 chances to guess the word.".format(
            len(self.word)))
        while self.remaining_guesses > 0:
            print("Guesses remaining: {}".format(self.remaining_guesses))
            display = self.update_display()
            print(display)
            guess = input("Guess a letter: ")
            if guess in self.guesses:
                print("You have already guessed that letter.")
            elif guess in self.word:
                self.guesses.append(guess)
                if self.check_win():
                    print("Congratulations! You have won the game.")
                    return
            else:
                self.remaining_guesses -= 1
                print("That letter is not in the word.")
            print()
        print("Sorry, you have run out of guesses. The word was {}.".format(self.word))


def main():
    words = ["deductible", "copayment", "coinsurance",
             "preauthorization", "explanation", "denial"]
    game = Hangman(words)
    game.play_game()


if __name__ == "__main__":
    main()
