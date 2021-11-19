from pathlib import Path
from typing import AnyStr

import configuration_loader
import description_translator
from description_reader import DescriptionParser, ClassificationParser
from description_writer import DescriptionWriter
from excel_file import XlsFile


def update_descriptions(month: AnyStr, account_name: AnyStr):
    configs = configuration_loader.load()
    month_xls_file = XlsFile(Path(month + '.xlsx'))
    aux_xls_file = XlsFile(Path(configs['aux_file']['file_name']))
    description_parser = DescriptionParser(month_xls_file,
                                           tab_name=account_name,
                                           description_column=configs['month_file']['complete_description_column'],
                                           description_row_offset=configs['month_file']['description_row_offset'])
    classification_parser = ClassificationParser(aux_xls_file,
                                                 tab_name=configs['aux_file']['tab_name'],
                                                 regex_column=configs['aux_file']['regex_column'],
                                                 description_column=configs['aux_file']['description_column'],
                                                 category_column=configs['aux_file']['category_column'],
                                                 classification_row_offset=configs['aux_file']['row_offset'])
    description_writer = DescriptionWriter(month_xls_file,
                                           tab_name=configs['month_file']['description_tab_name'],
                                           description_column=configs['month_file']['description_column'],
                                           replacement_query_column=configs['month_file'][
                                               'replacement_query_column'],
                                           category_column=configs['month_file']['category_column'])
    descriptions = description_parser.get_descriptions()
    classifications = classification_parser.get_classifications()
    translated_descriptions = description_translator.translate_descriptions(classifications, descriptions)
    description_writer.write_descriptions(translated_descriptions)
    return {'message': f"Descriptions were updated"}, 200
