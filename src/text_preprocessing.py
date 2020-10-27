from nltk.tokenize import word_tokenize
from src.text_normalization import TextNormalizationLanguage, TextNormalizationEnglish, SpellCheck
from src.text_regular_cleaning import RegularCleaning
from src.text_filter_and_transform import FilterAndTransform
import sys

current_module = sys.modules[__name__]

classes_hierarchy = {
    "TextNormalizationLanguage" : ["apply_stopwords","apply_stopwords_steem"],
    "TextNormalizationEnglish" : ["lemmatization", "porter_stemmer", "remove_stop_words", "remove_contractions"],
    "RegularCleaning" : ["apply_re","get_only_words","remove_single_characters","to_lower_case"],
    "FilterAndTransform" : ["filter_tags", "ner_text"],
    "SpellCheck" : ["spell_correct", "spell_check"],
}


def reverse_dictionary(input_dict):
    new_dic = {}
    for k, v in input_dict.items():
        for x in v:
            new_dic[x] = k
    return new_dic



def run_pipeline(x, pipeline_dictionary):
    function_values = reverse_dictionary(classes_hierarchy)

    for operation, arguments in pipeline_dictionary.items():
        print("Running {} with arguments {}".format(operation, arguments))
        operation_class = function_values.get(operation, None)
        class_inst = getattr(current_module, operation_class)()
        input_arguments = {"x" : x }
        if len(arguments) > 0 :
            input_arguments.update(dict(arguments))
        x = class_inst.__getattribute__(operation)(**input_arguments)
    return x



