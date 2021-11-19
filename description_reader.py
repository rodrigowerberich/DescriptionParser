from excel_file import XlsFile
import re


class OriginalDescription:
    def __init__(self, value, row_index):
        self.value = value
        self.row_index = row_index


class DescriptionParser:
    def __init__(self, xls_file: XlsFile, tab_name, description_column, description_row_offset):
        self._xls_file = xls_file
        self._tab_name = tab_name
        self._description_column = description_column
        self._description_row_offset = description_row_offset

    def get_descriptions(self):
        wb_obj = self._xls_file.get_workbook()
        sheet = wb_obj[self._tab_name]

        is_empty_cell = False
        index = self._description_row_offset
        original_descriptions = []
        while not is_empty_cell:
            cell_coordinate = self._description_column + str(index)
            cell_value = sheet[cell_coordinate].value
            if cell_value:
                cell_value = re.findall(r'.*,"(.*)"', sheet[cell_coordinate].value)[0]
                original_descriptions.append(OriginalDescription(cell_value, index))
            else:
                is_empty_cell = True
            index = index + 1
        return original_descriptions


class ClassificationParser:
    def __init__(self, xls_file: XlsFile, tab_name, regex_column, category_column, description_column, classification_row_offset):
        self._xls_file = xls_file
        self._tab_name = tab_name
        self._regex_column = regex_column
        self._category_column = category_column
        self._description_column = description_column
        self._classification_row_offset = classification_row_offset

    def get_classifications(self):
        aux_wb_obj = self._xls_file.get_workbook()
        classification_sheet = aux_wb_obj[self._tab_name]
        is_empty_cell = False
        index = self._classification_row_offset
        classification_object = []
        while not is_empty_cell:
            regex_cell_coordinate = self._regex_column + str(index)
            category_cell_coordinate = self._category_column + str(index)
            description_cell_coordinate = self._description_column + str(index)
            regex_cell_value = classification_sheet[regex_cell_coordinate].value
            category_cell_value = classification_sheet[category_cell_coordinate].value
            description_cell_value = classification_sheet[description_cell_coordinate].value
            if regex_cell_value:
                classification_object.append([re.compile(regex_cell_value), category_cell_value, description_cell_value])
            else:
                is_empty_cell = True
            index = index + 1
        return classification_object
