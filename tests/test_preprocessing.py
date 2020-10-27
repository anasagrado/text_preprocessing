import unittest
from unittest.mock import patch
from text_preprocessing.src import text_preprocessing


class TestPreprocessing(unittest.TestCase):

    def test_run_pipeline_each(self):
        # Testing that we can call each method from the pipeline
        eg1 = "I've been to Melisa's house yesterday. I did leave the house earlier because I had some migraines and I wats feeling unwell"
        res1_apply_stopwords = text_preprocessing.run_pipeline(eg1, { "apply_stopwords": {},} )
        self.assertEqual(res1_apply_stopwords, "I 've Melisa 's house yesterday . I leave house earlier I migraines I wats feeling unwell")
        # self.assertEqual(res1_apply_stopwords, "i migraines")

        res1_apply_stopwords_steem = text_preprocessing.run_pipeline(eg1, { "apply_stopwords_steem": {},} )
        self.assertEqual(res1_apply_stopwords_steem, "i ve melisa 's hous yesterday . i leav hous earlier i migrain i wat feel unwel")

        res1_lemmatization = text_preprocessing.run_pipeline(eg1, { "lemmatization": {},} )
        self.assertEqual(res1_lemmatization,"I 've been to Melisa 's house yesterday . I did leave the house earlier because I had some migraine and I wats feeling unwell")

        res1_porter_stemmer = text_preprocessing.run_pipeline(eg1, {"porter_stemmer": {}, })
        self.assertEqual(res1_porter_stemmer, "I 've been to melisa 's hous yesterday . I did leav the hous earlier becaus I had some migrain and I wat feel unwel")

        res1_remove_stop_words = text_preprocessing.run_pipeline(eg1, {"remove_stop_words": {}, })
        self.assertEqual(res1_remove_stop_words, "I 've Melisa 's house yesterday . I leave house earlier I migraines I wats feeling unwell")

        res1_remove_contractions = text_preprocessing.run_pipeline(eg1, {"remove_contractions": {}, })
        self.assertEqual(res1_remove_contractions, "I have been to Melisa's house yesterday. I did leave the house earlier because I had some migraines and I wats feeling unwell")

        res1_apply_re = text_preprocessing.run_pipeline(eg1, {"apply_re": {}, })
        self.assertEqual(res1_apply_re, "I've been to Melisa  house yesterday  I did leave the house earlier because I had some migraines and I wats feeling unwell")

        res1_get_only_words= text_preprocessing.run_pipeline(eg1, {"get_only_words": {}, })
        self.assertEqual(res1_get_only_words, "I ve been to Melisa s house yesterday  I did leave the house earlier because I had some migraines and I wats feeling unwell")

        res1_remove_single_characters = text_preprocessing.run_pipeline(eg1, {"remove_single_characters": {}, })
        self.assertEqual(res1_remove_single_characters, "'ve been to Melisa 's house yesterday did leave the house earlier because had some migraines and wats feeling unwell")

        res1_to_lower_case= text_preprocessing.run_pipeline(eg1, {"to_lower_case": {}, })
        self.assertEqual(res1_to_lower_case, "i've been to melisa's house yesterday. i did leave the house earlier because i had some migraines and i wats feeling unwell")

        res1_ = text_preprocessing.run_pipeline(eg1, {"get_only_words": {}, })
        self.assertEqual(res1_,"I ve been to Melisa s house yesterday  I did leave the house earlier because I had some migraines and I wats feeling unwell")

        res1_filter_tags = text_preprocessing.run_pipeline(eg1, {"filter_tags": {}, })
        self.assertEqual(res1_filter_tags, "'ve been Melisa house yesterday did leave house earlier had migraines wats feeling unwell")


        res1_filter_tags = text_preprocessing.run_pipeline(eg1, {"filter_tags":
                                                                    {'persist_postags': ['NOUN', 'ADJ']} }
                                                            )

        self.assertEqual(res1_filter_tags, "Melisa house yesterday house migraines unwell")

        res1_ner_text = text_preprocessing.run_pipeline(eg1, {"ner_text": {}, })
        self.assertEqual(res1_ner_text, "I 've been to company 's house date . I did leave the house earlier because I had some migraines and I wats feeling unwell")

        res1_spell_correct = text_preprocessing.run_pipeline(eg1, {"spell_correct": {}, })
        self.assertEqual(res1_spell_correct, "I eve been to Melisa is house yesterday . I did leave the house earlier because I had some migraines and I was feeling unwell")

        res1_spell_check = text_preprocessing.run_pipeline(eg1, {"spell_check": {}, })
        self.assertEqual(res1_spell_check, "been to house yesterday did leave the house earlier because had some migraines and feeling unwell")

    def test_run_pipeline(self):
        eg1 = "I have had some migraines"
        res1 = text_preprocessing.run_pipeline(eg1,
                    {
                         "apply_stopwords" : (),
                        "to_lower_case" : (),
                    }
                                    )
        self.assertEqual(res1, "i migraines")

        res2 = text_preprocessing.run_pipeline(eg1,
                    {
                        "to_lower_case": (),
                         "apply_stopwords" : (),

                    }
                                    )
        self.assertEqual(res2, "migraines")

        eg2 = "I have had some migraines but when I went to the doctor he said best remedy is to stay calm and stress free"
        res3 = text_preprocessing.run_pipeline(eg2,
                    {
                        "remove_stop_words": (),
                        "lemmatization" : (),
                        "porter_stemmer" : (),

                    }
                                               )
        self.assertEqual(res3, 'I migrain I went doctor said best remedi stay calm stress free')

        eg3 = "I've been to Melisa's house yesterday"
        res4 = text_preprocessing.run_pipeline(eg3,
                                               {
                                                   "remove_contractions": (),
                                               }
                                               )
        self.assertEqual(res4, "I have been to Melisa's house yesterday")