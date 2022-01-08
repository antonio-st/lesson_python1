listWord = ['python', 'c++', 'c', 'scala', 'java', 'java script', 'c#',
            'delphi', 'visual basic']
letter = input('Input letter >> ')


def count_letter(listWord, letter):
    count = 0
    for word in listWord:
        if letter in word:
            count += 1
    print('Number of latters in the list:', listWord, '\n', '=', count)


count_letter(listWord, letter)
