from string import ascii_lowercase, ascii_uppercase
import re
import difflib

class Subtitles:

    ORIGINAL_SUBTITLES = 'The Lord of the Rings. The Fellowship of the Ring.srt'
    THE_MOST_USE_WORDS = '20k.txt'
    EN_CZ_DICTIONARY = 'en-cs.txt'

    def original_subtitles(self, filename=ORIGINAL_SUBTITLES) -> None:
        '''Converts the subtitles to a list'''
        with open(filename, 'r') as f:
            subtitles = f.read()
        # Remove of unnecessary characters
        self.original_list = re.findall(r'\w+', subtitles)

    def filter_text(self) -> None:
        '''Filters only text from the original subtitles list'''
        temporary_list = []
        for i in self.original_list:
            if i[0] in ascii_lowercase or i[0] in ascii_uppercase:
                temporary_list.append(i.lower())
        self.original_list = temporary_list

    def remove_duplicities(self) -> None:
        '''Removes duplicities from the original subtitles'''
        temporary_list = [*set(self.original_list)]
        temporary_list.sort()
        self.original_list = temporary_list

    def unknown_words(self, file=THE_MOST_USE_WORDS) -> None:
        '''Removes the most use words'''
        with open(file, 'r') as f:
            known_words = (f.read()).split()
        self.unknown_words = []

        for i in self.original_list:
            if i not in known_words:
                self.unknown_words.append(i)

    def format_dictionary(self, file=EN_CZ_DICTIONARY):
        '''Converts string dictionary to dict format'''
        with open(file, 'r') as f:
             dictionary_list = (f.read()).split('\n')

        self.dictionary_dict = dict()

        for i in dictionary_list:
            key, *val = i.split('\t')
            self.dictionary_dict[key] = val

    def create_key_list(self):
        '''Creates key list from dictionary'''
        self.key_list = []
        for key in self.dictionary_dict:
            self.key_list.append(key)

    def find_similar_words(self, file=THE_MOST_USE_WORDS):
        '''Creates list of similar words from list of unknown words'''
        self.similar_words = {}
        for i in self.unknown_words:
            try:
                similar = difflib.get_close_matches(i, self.key_list)[0]
                self.similar_words[i] = similar
            except IndexError as e:
                print(e)
                pass

        with open(file, 'r') as f:
            known_words = (f.read()).split()
        self.final_unknown_words = {}

        for key, value in self.similar_words.items():
            if value not in known_words:
                self.final_unknown_words[key] = value

    def translate(self):
        '''Translates final unknown words'''
        final_translate = {}
        for key, value in self.final_unknown_words.items():
            if value in self.dictionary_dict:
                final_translate[key] = [self.final_unknown_words[key]] + self.dictionary_dict[value]
        print(final_translate)



if __name__ == '__main__':
    forrest = Subtitles()
    forrest.original_subtitles()
    forrest.filter_text()
    forrest.remove_duplicities()
    forrest.unknown_words()
    forrest.format_dictionary()
    forrest.create_key_list()
    forrest.find_similar_words()
    forrest.translate()
