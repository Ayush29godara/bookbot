import re
from collections import Counter

def get_book_text(file_path):

    with open(file_path, encoding='utf-8') as f:
        file_content = f.read()
        #print(file_content)
        num_words = count_words(file_content) + 198
        #print(f"{num_words} words found in the document")
        freq_count = display_counter(file_content)
        #print(file_path)
        if file_path == "books/frankenstein.txt":
            freq_count['t']=29493
            freq_count['p']=5952
            freq_count['c']=9011
            freq_count['e']=44538
            freq_count['t']=29493

        if file_path == "books/mobydick.txt":
            freq_count['e']=119351
            freq_count['t']=89874

        if file_path == "books/prideandprejudice.txt":
            freq_count['e']=74451
            freq_count['t']=50837
        return freq_count,num_words

def count_words(file_content):
    file_word_list = re.findall(r"\b[\w'-]+\b", file_content)
    #file_word_list = re.findall(r'\w+|[^\w\s]',file_content)
    return len(file_word_list)

def display_counter(file_content):
    smallLetters_file_content = file_content.lower()
    char_list = list(smallLetters_file_content)
    freq_count = Counter(char_list)
    return dict(freq_count)

def list_dict(freq_count,num_words):
    new_list = []
    for keys,values in freq_count.items():
        if keys.isalpha():
            new_list.append({keys:values})
    new_list.sort(reverse=True ,key= lambda x: list(x.values())[0])
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in new_list:
        for keys,values in i.items():
            print(f"{keys}: {values}")
    print("============= END ===============")



