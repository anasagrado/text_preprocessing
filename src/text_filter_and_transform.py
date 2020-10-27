from itertools import groupby
import nltk
from nltk.tokenize import word_tokenize


class FilterAndTransform:
    def __init__(self):
        self.nlp = None

    @staticmethod
    def filter_tags(x, persist_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        """
        This function will filter words in the sentence
        based on it's post_tag value.

        """
        eq = {'NOUN' : "NN",
                'ADJ':"JJ",
                'VERB' : "VB" ,
                'ADV' : "RB" }
        persistPostags_eq = [eq[x] for x in persist_postags]
        def to_tag(tag):
            return any( tag.startswith(tags_eq) for tags_eq in persistPostags_eq)
        return ' '.join([word for (word,tag) in nltk.pos_tag(word_tokenize(x)) if to_tag(tag)] )

    def ner_text(self,x):
        # import spacy
        # nlp = spacy.load('en', disable=['parser', 'ner'])
        if self.nlp is None:
            import en_core_web_sm
            self.nlp = en_core_web_sm.load()

        transformations = {"PERSON": "person",
                           "NORP": "norp",
                           "FAC": "fac",
                           "ORG": "company",
                           "GPE": "place",
                           "LOC": "loc",
                           "PRODUCT": "product",
                           "EVENT": "event",
                           "WORK_OF_ART": "work of art",
                           "LAW": "law",
                           "LANGUAGE": "language",
                           "DATE": "date",
                           "TIME": "time",
                           "PERCENT": "percent",
                           "MONEY": "money",
                           "QUANTITY": "quantity",
                           "ORDINAL": "ordinal",
                           "CARDINAL": "cardinal"

                           }
        doc = self.nlp(x)
        new_doc = [X.text if X.ent_iob_ == 'O' else transformations[X.ent_type_] for X in doc]
        new_doc = [k for k, g in groupby(new_doc)]
        return " ".join(new_doc)
