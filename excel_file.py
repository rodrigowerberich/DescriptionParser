import openpyxl
from pathlib import Path


class XlsFile:
    def __init__(self, path: Path):
        self._path = path
        self._wb_obj = openpyxl.load_workbook(self._path)

    def get_workbook(self):
        return self._wb_obj

    def get_path(self):
        return self._path
