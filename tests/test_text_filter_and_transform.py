import unittest
from unittest.mock import patch
from text_preprocessing.src import text_filter_and_transform


class TestFilterAndTransform(unittest.TestCase):


    def test_FilterAndTransform(self):
        text_filter_and_transform_instance = text_filter_and_transform.FilterAndTransform()
        eg1 = "I was with my mother yesterday"
        res1_ner = text_filter_and_transform_instance.ner_text(eg1)
        res1_tag_filt_n = text_filter_and_transform_instance.filter_tags(eg1, ['NOUN'])
        res1_tag_filt_v = text_filter_and_transform_instance.filter_tags(eg1, ['VERB'])

        self.assertEqual(res1_ner, "I was with my mother date")
        self.assertEqual(res1_tag_filt_n, "mother yesterday")
        self.assertEqual(res1_tag_filt_v, "was")

        eg2 = "United States is a country primarily located in central North America"
        res2_ner = text_filter_and_transform_instance.ner_text(eg2)
        self.assertEqual(res2_ner, "place is a country primarily located in central loc")