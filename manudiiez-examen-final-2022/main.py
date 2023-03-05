from phrase import Phrase


if __name__ == '__main__':
    phrase = Phrase()
    phrase.encode('dos palabras')
    # print(phrase)
    result = phrase.encoded
    phrase.decode(result)
    print(phrase.decoded)