from nltk.tokenize import word_tokenize
import re


class RegularCleaning:
    @staticmethod
    def apply_re(x):
        x = re.sub("\\n|\\t", " ", x)  # remove new line and tab symbols
        x = re.sub("((?<=[A-Za-z])'s)", " ", x)  # replace 's preceded by a word by a space. Eg: Ana's -> Ana_
        x = re.sub("\(|\)|!|-|\[|\]|;|:|<|>|\.|,|/|\?|@|#|\$|%|\^|\&|\*|_|\~", " ",
                   x)  # replace punctuaction signs by space.
        return x

    @staticmethod
    def get_only_words(x):
        clean_x = re.sub("[^a-zA-Z]", " ", x)
        return clean_x

    @staticmethod
    def remove_single_characters(x):
        return ' '.join([w for w in word_tokenize(x) if len(w) > 1])

    @staticmethod
    def to_lower_case(x):
        return x.lower()

