import unittest
from subtitles import Subtitles


class Test(unittest.TestCase):

    def test_original_subtitles(self):
        file = 'test_subtitles.txt'
        test_document = Subtitles()
        test_document.original_subtitles(file)
        self.assertEqual(test_document.original_list[-1], 'these')

    def test_unknown_words(self):
        test_document = Subtitles()
        file = '10k.txt'
        test_document.original_list = ['hello', 'world', 'and', 'racoons']
        test_document.unknown_words(file)

        if 'racoons' in test_document.unknown_words:
            self.assertTrue('Test pass')
        else:
            self.assertFalse('Test fail')

        if 'and' not in test_document.unknown_words:
            self.assertTrue('Test pass')
        else:
            self.assertFalse('Test fail')


    def test_find_similar_words(self):
        test_document = Subtitles()
        file = '10k.txt'
        test_document.unknown_words = ['hello', 'world', 'and', 'racoons']
        test_document.key_list = ['hello', 'world', 'and', 'racoon']
        test_document.find_similar_words(file)
        a = {'racoons': 'racoon'}
        self.assertEqual(a, test_document.final_unknown_words)


if __name__ == '__main__':
    unittest.main()
