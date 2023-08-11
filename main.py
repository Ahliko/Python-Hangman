import random as rd


class Hangman:
    def __init__(self):
        self.word = ""
        self.letters = []
        self.known_letters = []
        self.pos = 0
        self.lives = 10

    def generate_word(self):
        f = open("words.txt", "r")
        words = f.readlines()
        f.close()
        self.word = rd.choice(words).strip()
        self.letters = list("_" * len(self.word))

    def print_hangman(self):
        f = open("hangman.txt", "r")
        hangman = f.readlines()
        f.close()
        print("".join(hangman[self.pos:self.pos + 7]))

    def print_word(self):
        for letter in self.letters:
            print(letter, end=" ")
        print("\n")

    def update_word(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.letters[i] = letter

    def is_win(self):
        return "_" not in self.letters

    def is_lose(self):
        return self.lives == -1

    def lose_life(self):
        if not self.lives == 10:
            self.pos += 8
        self.lives -= 1
        print(f"Not present in the word, {self.lives} attempts remaining\n")

    def play(self):
        print("Good Luck, you have 10 attempts.")
        self.print_word()
        while True:
            letter = input("\nChoose: ")
            if letter in self.known_letters:
                print("Letter already chosen!")
                self.lose_life()
            elif letter in self.word:
                self.update_word(letter)
                self.known_letters.append(letter)
                self.print_word()
            else:
                self.lose_life()
                self.known_letters.append(letter)
            if not self.lives == 10:
                self.print_hangman()
            if self.is_lose():
                print("You lost!\n The word was:", self.word, "\n")
                return
            if self.is_win():
                print("You won!")
                return


def run():
    while True:
        game = Hangman()
        game.generate_word()
        game.play()
        if input("Play again? (y/n): ") == "n":
            return


if __name__ == "__main__":
    run()
