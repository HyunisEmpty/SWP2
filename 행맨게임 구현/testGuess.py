import unittest

from guess import Guess
from hangman import Hangman


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('appple')
        self.g3 = Guess('cake')

    def tearDown(self):
        pass

    # test cases
    def testDisplayCurrent(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_e_____')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_e_a___')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_e_a__t')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_e_au_t')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'de_au_t')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'defau_t')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'default')

    def testDisplayGuessed(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayGuessed(), 'e')
        # self.assertEqual(self.g1.displayCurrent(), '_e_____')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), 'e a')
        # self.assertEqual(self.g1.displayCurrent(), '_e_a___')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayGuessed(), 'a e n')
        # self.assertEqual(self.g1.displayCurrent(), '_e_a___')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), 'a e n t')
        # self.assertEqual(self.g1.displayCurrent(), '_e_a__t')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), 'a e n t u')
        # self.assertEqual(self.g1.displayCurrent(), '_e_au_t')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), 'a e n t u d')
        # self.assertEqual(self.g1.displayCurrent(), 'de_au_t')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), 'a e n t u d f')
        # self.assertEqual(self.g1.displayCurrent(), 'defau_t')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), 'a e n t u d f l')
        # self.assertEqual(self.g1.displayCurrent(), 'default')

    def testGuess(self):
        # 리턴값이 올바른가?
        self.assertTrue(self.g1.guess('a'))
        self.assertFalse(self.g1.guess('k'))

    def testFinished(self):                 # 단어의 전체를 다맞춘 경우 정상 출력되는지를 확인
        self.g2.currentStatus = "apple"
        self.assertTrue(self.g2.finished())
        self.g3.currentStatus = "case"
        self.assertFalse(self.g3.finished())


class TestHangman(unittest.TestCase):

    def setUp(self):
        self.g1 = Hangman()

    def testRemainLife(self):
        self.assertTrue(self.g1.remainingLives == 6)
        self.assertFalse(self.g1.remainingLives == -1)
        self.assertFalse(self.g1.remainingLives == 10)

if __name__ == '__main__':
    unittest.main()