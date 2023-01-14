# **subtitles.py**


## **Usefulness:**
This program was created to translate English movie subtitles, but can be used for any English text. Subtitles.py creates en-cz dictionary with less common English words from the English text.

## **Dependencies:**
**from string import ascii_lowercase, ascii_uppercase**
*   it is needed for `filter_text()` method to select only alphabet characters

**import re**
*   it is needed for `original_subtitles()` method to remove unnecessary characters

**import difflib**
*   it is needed for `find_similar_words()` method to compare the origin word with the dictionary word

## **Content of repository**
**30k.txt**
- a list of the 30,000 most common English words in order of frequency, derived from [Peter Norvig's](http://norvig.com/ngrams/) compilation of [1/3 million most frequent English words](http://norvig.com/ngrams/count_1w.txt).

**20k.txt**
- first 20,000 most common English words from list 30k.txt

**10k.txt**
- first 10,000 most common English words from list 30k.txt

**en-cs.txt**
- free English-Czech Dictionary from [svobodneslovniky](https://github.com/svobodneslovniky/svobodneslovniky)

**Forrest.Gump.1994.srt**
- free subtitles from [opensubtitles.org](https://www.opensubtitles.org/cs/search/sublanguageid-eng/idmovie-178)
- these subtitles are there only for example uses

##  **How to use it**
```Python
class Subtitles:

    ORIGINAL_SUBTITLES = 'Forrest.Gump.1994.srt'
    THE_MOST_USED_WORDS = '20k.txt'
    EN_CZ_DICTIONARY = 'en-cs.txt'
```
**ORIGINAL_SUBTITLES** - fill in whole file name of your English text

**THE_MOST_USE_WORDS** - choose 30k, 20k or 10k.txt depending on your english level

## **Result**
Created txt file named *whole file name of your English text*_translate.txt (for example Forrest.Gump.1994.srt_translate.txt). The words are sorted:

the original word : [similar word, translate],
for example:

'raccoons': ['raccoon', 'mýval']

## **Note**
When the Original subtitles contains names, names of cities etc.or word is not in dictionary, the program tries to find similar word and this similar word is had different meaning.
