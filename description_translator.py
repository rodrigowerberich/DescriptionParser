from typing import Iterable
from description_reader import OriginalDescription


def translate_descriptions(classification_object, original_descriptions: Iterable[OriginalDescription]):
    translated_descriptions = []
    for original_description in original_descriptions:
        translated_descriptions.append({'complete description': original_description.value,
                                        'row index': original_description.row_index,
                                        'possible information': []})
        for description_matcher in classification_object:
            if description_matcher[0].search(original_description.value):
                information = {'description': description_matcher[1],
                               'category': description_matcher[2]}
                translated_descriptions[-1]['possible information'].append(information)
        if not translated_descriptions[-1]['possible information']:
            information = {'description': 'Desconhecida',
                           'category': 'Desconhecida'}
            translated_descriptions[-1]['possible information'].append(information)
    return translated_descriptions
