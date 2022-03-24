import re
#function for unique word count
def uniqueWordCout(fileContent):
    uniqueWordDictionary = {}
    words = filter(None, re.split(' |\n|\t', fileContent))
    for word in words:
        uniqueWordDictionary[word] = uniqueWordDictionary.get(word, 0) + 1
    return uniqueWordDictionary
# function for replacement
   
def replaceWord(fileContent, findBy, replaceBy):
    return re.sub('[ \t\n]'+findBy+'[ \t\n]', lambda x : x.group().replace(findBy, replaceBy), fileContent)

#replace file structure with the ones in your system

inputFile = (open('C:/Users/Sandeep pc/Desktop/SE_Project/sample.txt'))
a = inputFile.read()

b = uniqueWordCout(a)

#print(b)

print(" \n Frequency of each word: \n")
for key in b:
    
    print("\t",key, '->', b[key])

print("\n")
print("unique word count = ",uniqueWordCout(a))
print("\n")
print("Original text message= ",a)
print("\n")



existing_word = input("Enter the existing_word= ")
replace_word = input("\nEnter the replacing_word = ")
print("\n")

print("After replacing text message =",replaceWord(a,existing_word ,replace_word))