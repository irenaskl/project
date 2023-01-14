from string import ascii_lowercase, ascii_uppercase
import re
import difflib


class Subtitles:

    ORIGINAL_SUBTITLES = 'Forrest.Gump.1994.srt'
    THE_MOST_USED_WORDS = '20k.txt'
    EN_CZ_DICTIONARY = 'en-cs.txt'

    def __init__(self):
        self.format_dictionary()
        self.create_key_list()

    def original_subtitles(self, filename=ORIGINAL_SUBTITLES) -> None:
        '''Converts the subtitles to a list'''
        with open(filename, 'r') as f:
            try:
                subtitles = f.read()
            except UnicodeDecodeError:
                with open(filename, 'r', errors='ignore') as f:
                    subtitles = f.read()

        # Remove unnecessary characters
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

    def unknown_words(self, file=THE_MOST_USED_WORDS) -> None:
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

        self.dictionary_dict = {}
        for i in dictionary_list:
            key, *val = i.split('\t')
            self.dictionary_dict[key] = val

    def create_key_list(self):
        '''Creates key list from dictionary'''
        self.key_list = []
        for key in self.dictionary_dict:
            self.key_list.append(key)

    def find_similar_words(self, file=THE_MOST_USED_WORDS):
        '''Creates dictionary of similar words from list of unknown words'''
        temporary = {}
        # Change plural on singular, because en-cs contents only singulars
        for original_word in self.unknown_words:
            if original_word.endswith('s'):
                singular_word = original_word[:-1]
                temporary[original_word] = singular_word
            else:
                temporary[original_word] = original_word

        self.similar_words = {}
        # Find the same or similar unknown words as in en-cs dictionary
        for key, value in temporary.items():
            try:
                similar = difflib.get_close_matches(value, self.key_list)[0]
                self.similar_words[key] = similar
            except IndexError as e:
                print(e)
                pass

        with open(file, 'r') as f:
            known_words = (f.read()).split()

        self.final_unknown_words = {}
        # Again try to remove the most used words,
        # because we have new known words because of changed
        # plural to singular.
        for key, value in self.similar_words.items():
            if value not in known_words:
                self.final_unknown_words[key] = value

    def translate(self):
        '''Translates final unknown words'''
        self.final_translate = {}
        for key, value in self.final_unknown_words.items():
            if value in self.dictionary_dict:
                self.final_translate[key] = ([self.final_unknown_words[key]]
                                            + self.dictionary_dict[value][:1])
        return str(self.final_translate)

    def save_translate(self):
        '''Saves final translate to format txt file'''
        file = (f'{self.ORIGINAL_SUBTITLES}_translate.txt')
        temporary = ''

        with open(file, 'w') as f:
            f.write(self.translate())

        # The final dictionary has the format:
        # origin word from subtitles : [the same or similar word in dictionary,
        # the translate].
        with open(file, 'r') as fp:
            for i in fp:
                temporary += (str(i).replace('],', ']\n'))

        with open(file, 'w') as fp:
            fp.write(temporary)


if __name__ == '__main__':
    document = Subtitles()
    document.original_subtitles()
    document.filter_text()
    document.remove_duplicities()
    document.unknown_words()
    document.find_similar_words()
    document.save_translate()
