from typing import AnyStr, Iterable
import manage_gdrive_files


def import_spreadsheet_from_google_drive(path: AnyStr):
    converted_path = manage_gdrive_files.path_converter(path)
    if manage_gdrive_files.import_spreadsheet_file(converted_path):
        return {'message': f"File '{path}' was successfully imported"}, 201
    else:
        return {'message': f"Something went wrong while trying to import file '{path}'"}, 500


def import_spreadsheets_from_google_drive(paths: Iterable[AnyStr]):
    converted_paths = [manage_gdrive_files.path_converter(path) for path in paths]
    if manage_gdrive_files.import_spreadsheets_file(converted_paths):
        return {'message': f"Files were successfully imported"}, 201
    else:
        return {'message': f"Something went wrong while trying to import the files"}, 500