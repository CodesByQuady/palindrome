#String List
word = input("Enter any word: ")
def palindrome(word):
    word_check = []
    for i in word:
        word_check.append(i)
    pal = word_check[ : : -1]
    if word_check == pal:
        print(word,"is a palindrome.")
    else:
        print(word,"is not a palindrome.")
    
palindrome(word)
