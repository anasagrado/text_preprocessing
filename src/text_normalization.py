from nltk.tokenize import word_tokenize

class TextNormalizationLanguage:
    def __init__(self, language = 'en'):
        from nltk.corpus import stopwords
        from nltk.stem import SnowballStemmer

        if language in ['sp', 'spanish']:
            self.stopwords = stopwords.words('spanish')
            self.stemmer = SnowballStemmer('spanish')
        elif language in ['en', 'english']:
            self.stopwords = stopwords.words('english')
            self.stemmer = SnowballStemmer('english')
        else:
            raise ValueError("Language should be either 'sp'/'spansih' or 'en'/'english' ")

    def apply_stopwords(self,x):
        res = [x for x in word_tokenize(x) if x not in self.stopwords]
        return " ".join(res)

    def apply_stopwords_steem(self,x):
        with_stopwords = self.apply_stopwords(x)
        res = [self.stemmer.stem(x) for x in word_tokenize(with_stopwords) ]
        return " ".join(res)

class TextNormalizationEnglish:

    def __init__(self):
        self.lemmatizer = None
        self.porter = None
        self.stopwords = None
        self.contractions = None


    def lemmatization(self, x):
        """
        Given a sentence x, this function will use the nltk
        WordNetLemmantizer to normalize the words
        """
        if self.lemmatizer is None:
            from nltk.stem import WordNetLemmatizer
            self.lemmatizer = WordNetLemmatizer()
        result = ' '.join([self.lemmatizer.lemmatize(word) for word in word_tokenize(x)])
        return result


    def porter_stemmer(self, x):
        """
        Given a sentence x, this function will use the nltk
        PorterStemmer to normalize the words
        """
        if self.porter is None:
            from nltk.stem import PorterStemmer
            self.porter = PorterStemmer()
        return ' '.join([self.porter.stem(word) for word in word_tokenize(x)])

    def remove_stop_words(self, x):
        """
        Given a sentence x, this function will use wordcloud
        stopwords list to remove the stopwords from the text
        """
        if self.stopwords is None:
            from wordcloud import STOPWORDS
            self.stopwords = STOPWORDS
        return ' '.join([w for w in word_tokenize(x) if not w in self.stopwords])

    def remove_contractions(self, x):
        """
        This function will remove contractions
        :param x:
        :return:
        """
        if self.contractions is None:
            import contractions
            self.contractions = contractions
        return self.contractions.fix(x)


class SpellCheck:
    def __init__(self):
        self.spell = None

    def spell_correct(self, x):
        """
        Given a sentence x, this function will check,
        for each word, weather it was misspelled or not.


        :param x:
        :return:
        """
        if self.spell is None:
            from spellchecker import SpellChecker
            self.spell = SpellChecker()
        word_list = word_tokenize(x)
        misspelled = self.spell.unknown(word_list)
        corrected_words_dict = dict([ (word, self.spell.correction(word)) for word in misspelled])
        word_corrected = [corrected_words_dict.get(x,x) for x in word_list]
        return ' '.join(word_corrected)


    def spell_check(self, x):
        """
        Given a sentence x, this function will return
        the same sentence bu removing all the words that
        were misspelled.

        Notice this function doesn't correct any misspelled words
        but just filter them. If you want to correct those wordspip install pyspellchecker
        you should use spell_check_correct.
        """
        if self.spell is None:
            from spellchecker import SpellChecker
            self.spell = SpellChecker()
        word_list = word_tokenize(x)
        correct_words = self.spell.known(word_list)
        word_list_filtered = [x for x in word_list if x in  correct_words]
        return ' '.join(word_list_filtered)
