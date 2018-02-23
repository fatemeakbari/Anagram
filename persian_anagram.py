from openpyxl import load_workbook


#sorted the word and delete space
def sorted_word(word):
    return "".join(sorted(word.replace(" ", "").lower()))

def fill_words_dictionary():
    #Loading Persian Dictionary
    wb = load_workbook(filename='MoinDictionary2.xlsx', read_only=True)
    ws = wb.active
    
    for row in ws.rows:
        #get word of Moin's dictionary 
        word = row[0].value
        #print('word:  ',word)
        #word = word.strip()
        sword = sorted_word(word)
        if not sword in words:
            words[sword] = []

        words[sword].append(word)

def main():
    word = input("inter the word: ")
    while word:
        sword = sorted_word(word)

        if sword in words:
            print("Anagram list:", ", ".join(words[sword]))
        else:
            print("No anagrams.")

        word = input("inter the word: ")


words = {}

fill_words_dictionary()

if __name__ == '__main__':
    main()
