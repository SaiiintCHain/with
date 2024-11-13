import string

class WordsFinder:
    def __init__(self, *names):
        self.names = names

    def get_all_words(self):
        all_words = {}
        for name in self.names:
            with open(name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = text.translate(str.maketrans('','', string.punctuation +  '-'))
                words = text.split()
                all_words[name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        position = {}
        for name, words in self.get_all_words().items():
            if word in words:
                position[name] = words.index(word) + 1
        return position

    def count(self, word):
        word = word.lower()
        numbers = {}
        for name, words in self.get_all_words().items():
            how_many = words.count(word)
            if how_many >= 0:
                numbers[name] = how_many
        return numbers


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))