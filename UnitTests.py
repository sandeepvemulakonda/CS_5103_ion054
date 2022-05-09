import unittest
import StringUtil as Str


class MyTestCase(unittest.TestCase):
    str = Str.StringUtil()
    fileContent = ' Hi everyone. Hi again, this is Sandeep '
    def test_uniqueWordCount(self):
        actualOutput = self.str.uniqueWordCount(self.fileContent)
        expectedOutput = {"Hi": 2,
                          "everyone." : 1,
                          "again," : 1,
                          "this": 1,
                          "is" : 1,
                          "Sandeep":1}
        self.assertEqual(len(actualOutput), len(expectedOutput))


    def test_replaceWord(self):
        findBy = 'Hi'
        replaceBy = 'Hello'
        actualOutput = self.str.replaceWord(self.fileContent, findBy, replaceBy)
        expectedOutput = ' Hello everyone. Hello again, this is Sandeep '
        self.assertEqual(actualOutput, expectedOutput)

    def test_grepline_match(self):
        keyword = 'Sandeep'
        actualOutput = len(self.str.grepline(self.fileContent, keyword))
        expectedOutput = 1
        self.assertEqual(actualOutput, expectedOutput)

    def test_grepline_no_match(self):
        keyword = 'UTSA'
        actualOutput = len(self.str.grepline(self.fileContent, keyword))
        expectedOutput = 0
        self.assertEqual(actualOutput, expectedOutput)

if __name__ == '__main__':
    unittest.main()
