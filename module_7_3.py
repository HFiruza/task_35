import pprint
import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                text = f.read()
            # Удаляем пунктуацию
            text_without_punctuation = text.lower().translate(str.maketrans('', '', string.punctuation))
            words = text_without_punctuation.split()
            all_words[file_name] = words
        return all_words

    def find(self, word):
        places = {} # места
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1
        return places

    def count(self, word):
        counters = {} # счетчики
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count
        return counters

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))