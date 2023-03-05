import unittest

from phrase import Phrase


class MyTest(unittest.TestCase):

    def test_case_1(self):
        phrase = Phrase()
        phrase.encode('anana')
        self.assertEqual(f'{phrase}', '[[a: [1, 3, 5], n: [2, 4]]]')

    def test_case_2(self):
        phrase = Phrase()
        phrase.encode('dos palabras')
        self.assertEqual(
            f'{phrase}', '[[d: [1], o: [2], s: [3]], [p: [1], a: [2, 4, 7], l: [3], b: [5], r: [6], s: [8]]]')

    def test_case_3(self):
        phrase = Phrase()
        phrase.encode('examen final de computacion')
        self.assertEqual(
            f'{phrase}', '[[e: [1, 5], x: [2], a: [3], m: [4], n: [6]], [f: [1], i: [2], n: [3], a: [4], l: [5]], [d: [1], e: [2]], [c: [1, 8], o: [2, 10], m: [3], p: [4], u: [5], t: [6], a: [7], i: [9], n: [11]]]')

    def test_case_4(self):
        phrase = Phrase()
        phrase.encode('a a a a a')
        self.assertEqual(
            f'{phrase}', '[[a: [1]], [a: [1]], [a: [1]], [a: [1]], [a: [1]]]')

    def test_case_5(self):
        phrase = Phrase()
        phrase.encode('agita falsos usos la fatiga')
        self.assertEqual(
            f'{phrase}', '[[a: [1, 5], g: [2], i: [3], t: [4]], [f: [1], a: [2], l: [3], s: [4, 6], o: [5]], [u: [1], s: [2, 4], o: [3]], [l: [1], a: [2]], [f: [1], a: [2, 6], t: [3], i: [4], g: [5]]]')

    def test_case_6(self):
        phrase = Phrase()
        phrase.encode('anana')
        result = phrase.encoded
        phrase.decode(result)
        self.assertEqual(f'{phrase.decoded}', 'anana')

    def test_case_7(self):
        phrase = Phrase()
        phrase.encode('dos palabras')
        result = phrase.encoded
        phrase.decode(result)
        self.assertEqual(f'{phrase.decoded}', 'dos palabras')

    def test_case_8(self):
        phrase = Phrase()
        phrase.encode('examen final de computacion')
        result = phrase.encoded
        phrase.decode(result)
        self.assertEqual(f'{phrase.decoded}', 'examen final de computacion')

    def test_case_9(self):
        phrase = Phrase()
        phrase.encode('agita falsos usos la fatiga')
        result = phrase.encoded
        phrase.decode(result)
        self.assertEqual(f'{phrase.decoded}', 'agita falsos usos la fatiga')

if __name__ == '__main__':
    unittest.main()