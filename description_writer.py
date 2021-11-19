from excel_file import XlsFile


class DescriptionWriter:
    def __init__(self,
                 xls_file: XlsFile,
                 tab_name,
                 replacement_query_column,
                 description_column,
                 category_column):
        self._xls_file = xls_file
        self._tab_name = tab_name
        self._replacement_query_column = replacement_query_column
        self._description_column = description_column
        self._category_column = category_column

    def write_descriptions(self, translated_descriptions):
        wb_obj = self._xls_file.get_workbook()
        sheet = wb_obj[self._tab_name]
        for translated_description in translated_descriptions:
            index = translated_description['row index']
            if sheet[self._replacement_query_column+str(index)].value != "Nao":
                sheet[self._description_column + str(index)].value = translated_description['possible information'][0]['description']
                sheet[self._category_column + str(index)].value = translated_description['possible information'][0]['category']
        wb_obj.save(self._xls_file.get_path())
