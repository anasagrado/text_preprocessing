import unittest
from unittest.mock import patch
from text_preprocessing.src import text_normalization


class TestPreprocessing(unittest.TestCase):

    def test_TextNormalizationLanguage_spanish(self):
        text_normalization_instance = text_normalization.TextNormalizationLanguage(language ='sp')
        ## --- > apply_stopwords TESTs
        eg1 = 'Esta ha sido una muy buena experiencia'
        expected1 = 'Esta sido buena experiencia'
        result1 = text_normalization_instance.apply_stopwords(eg1)
        self.assertEqual(expected1, result1)

        # All words in the sentence are stopwords
        eg2 = 'la ha '
        expected2 = ''
        result2 = text_normalization_instance.apply_stopwords(eg2)
        self.assertEqual(expected2, result2)

        # All words in the sentence are stopwords but the first one is capital letter
        # so is not being detected as stopword
        eg3 = 'La ha '
        not_expected3 = ''
        expected3 = 'La'
        result3 = text_normalization_instance.apply_stopwords(eg3)
        self.assertEqual(expected3, result3)
        self.assertNotEqual(result3, not_expected3)

        ## --- > apply_stopwords TESTs
        eg1 = 'Esta ha sido una muy buena experiencia'
        expected1 = 'esta sid buen experient'
        result1 = text_normalization_instance.apply_stopwords_steem(eg1)
        self.assertEqual(expected1, result1)

        # All words in the sentence are stopwords
        eg2 = 'la ha '
        expected2 = ''
        result2 = text_normalization_instance.apply_stopwords_steem(eg2)
        self.assertEqual(expected2, result2)

        # All words in the sentence are stopwords but the first one is capital letter
        # so is not being detected as stopword
        eg3 = 'La ha '
        not_expected3 = ''
        expected3 = 'la'
        result3 = text_normalization_instance.apply_stopwords_steem(eg3)
        self.assertEqual(expected3, result3)
        self.assertNotEqual(not_expected3, result3)

        eg4 = 'Vamos a ir haciendo lo que hay que hacer'
        expected4 = 'vam ir hac hac'
        result4 = text_normalization_instance.apply_stopwords_steem(eg4)
        self.assertEqual(expected4, result4)

    def test_TextNormalizationLanguage_english(self):
        text_normalization_instance = text_normalization.TextNormalizationLanguage(language='en')
        ## --- > apply_stopwords TESTs
        eg1 = 'This has been a great experience'
        expected1 = 'This great experience'
        result1 = text_normalization_instance.apply_stopwords(eg1)
        self.assertEqual(expected1, result1)

        # All words in the sentence are stopwords
        eg2 = 'this has been'
        expected2 = ''
        result2 = text_normalization_instance.apply_stopwords(eg2)
        self.assertEqual(expected2, result2)

        # All words in the sentence are stopwords but the first one is capital letter
        # so is not being detected as stopword
        eg3 = 'This has been'
        not_expected3 = ''
        expected3 = 'This'
        result3 = text_normalization_instance.apply_stopwords(eg3)
        self.assertEqual(expected3, result3)
        self.assertNotEqual(result3, not_expected3)

        ## --- > apply_stopwords TESTs
        eg1 = 'This has been a great experience'
        expected1 = 'this great experi'
        result1 = text_normalization_instance.apply_stopwords_steem(eg1)
        self.assertEqual(expected1, result1)

        # All words in the sentence are stopwords
        eg2 = 'this has been'
        expected2 = ''
        result2 = text_normalization_instance.apply_stopwords_steem(eg2)
        self.assertEqual(expected2, result2)

        # All words in the sentence are stopwords but the first one is capital letter
        # so is not being detected as stopword
        eg3 = 'This has been'
        not_expected3 = ''
        expected3 = 'this'
        result3 = text_normalization_instance.apply_stopwords_steem(eg3)
        self.assertEqual(expected3, result3)
        self.assertNotEqual(not_expected3, result3)

        eg4 = "Let's do what needs to be done by doing more "
        expected4 = "let 's need done"
        result4 = text_normalization_instance.apply_stopwords_steem(eg4)
        self.assertEqual(expected4, result4)

    def test_TextNormalizationEnglish(self):
        text_normalization_instance = text_normalization.TextNormalizationEnglish()
        eg1 = "I've been there twice before"
        res1_lemm = text_normalization_instance.lemmatization(eg1)
        res1_porter = text_normalization_instance.porter_stemmer(eg1)
        res1_stopw = text_normalization_instance.remove_stop_words(eg1)
        res1_contrac = text_normalization_instance.remove_contractions(eg1)
        self.assertEqual(res1_lemm, "I 've been there twice before")
        self.assertEqual(res1_porter, "I 've been there twice befor")
        self.assertEqual(res1_stopw,"I 've twice")
        self.assertEqual(res1_contrac, "I have been there twice before")

        res2_contrac = text_normalization_instance.remove_contractions(eg1)
        res2_lemm = text_normalization_instance.lemmatization(res2_contrac)
        res2_porter= text_normalization_instance.porter_stemmer(res2_contrac)
        res2_stopw = text_normalization_instance.remove_stop_words(res2_contrac)
        self.assertEqual(res2_lemm, "I have been there twice before")
        self.assertEqual(res2_porter, "I have been there twice befor")
        self.assertEqual(res2_stopw, "I twice")

    def test_SpellCheck(self):
        text_normalization_instance = text_normalization.SpellCheck()

        eg1 = "I wats able to study"
        res1_check = text_normalization_instance.spell_check(eg1)
        res1_corrected = text_normalization_instance.spell_correct(eg1)
        self.assertEqual(res1_check, "able to study")
        self.assertEqual(res1_corrected, "I was able to study")



