from hangman import *


if __name__ == "__main__":
    
    def test_show(word):
        hangman = Hangman()
        hangman.set_word(word)
        print(hangman.show())

    def test_assign(word, tries):
        hangman = Hangman()
        hangman.set_word(word)
        for letter in tries:
            hangman.assign(letter)
        print(hangman.show())

    def test_play_win():
        hangman = Hangman()
        hangman.set_word("jarra")
        hangman.play()


    test_show('ahorcado')
    test_assign('avion', ["a", "v", "n", "z"])

    