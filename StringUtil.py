import re


class StringUtil:
    # function for unique word count
    def uniqueWordCount(self, fileContent):
        uniqueWordDictionary = {}
        words = filter(None, re.split(' |\n|\t', fileContent))
        for word in words:
            uniqueWordDictionary[word] = uniqueWordDictionary.get(word, 0) + 1
        return uniqueWordDictionary


    # function for replacement
    def replaceWord(self, fileContent, findBy, replaceBy):
        result = re.sub('[ \t\n]' + findBy + '[ \t\n]', lambda x: x.group().replace(findBy, replaceBy), fileContent)
        return result


    # function to print all lines that contains keyword as full word
    def grepline(self, fileContent, keyWord):
        lines = fileContent.split('\n')
        matchedLines = []
        print("keyword line")
        for line in lines:
            if (bool(re.search('[ \t\n]' + keyWord + '[ \t\n]', line + "\n"))):
                print(line)
                matchedLines.append(line)
        return matchedLines



# replace file structure with the ones in your system

# inputFile = (open("sample.txt"))
# a = inputFile.read()
#
# b = StringUtil.uniqueWordCout(a)
#
# # print(b)
#
# print(" \n Frequency of each word: \n")
# for key in b:
#     print("\t", key, '->', b[key])
#
# print("\n")
#
# print("\n")
# print("Original text message= ", a)
# print("\n")
#
# existing_word = input("Enter the existing_word= ")
# replace_word = input("\nEnter the replacing_word = ")
# print("\n")
#
# print("After replacing text message =", StringUtil.replaceWord(a, existing_word, replace_word))
# keyword = input("enter the keyword = ")
# StringUtil.grepline(a,keyword)

