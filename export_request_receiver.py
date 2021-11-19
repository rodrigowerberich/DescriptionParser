from typing import AnyStr, Iterable

import gdrive_authenticator
import manage_gdrive_files


def export_spreadsheet_to_google_drive(month, export_path):
    converted_export_path = manage_gdrive_files.path_converter(export_path)
    if manage_gdrive_files.export_spreadsheet_file(month, converted_export_path):
        return {'message': f"File '{export_path}' was successfully exported"}, 201
    else:
        return {'message': f"Something went wrong while trying to export {month} to file '{export_path}'"}, 500


def export_spreadsheet_to_google_drive_with_auth(month, export_path, handle):
    drive_instance = gdrive_authenticator.get_drive_authenticators().get_instance(handle)
    converted_export_path = manage_gdrive_files.path_converter(export_path)
    manage_gdrive_files.export_spreadsheet_file_to_drive(drive_instance, month, converted_export_path)
    return {'message': f"File '{export_path}' was successfully exported"}, 201