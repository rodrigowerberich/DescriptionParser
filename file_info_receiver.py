from typing import AnyStr, Iterable
import manage_gdrive_files
import gdrive_authenticator


def get_file_link(path: AnyStr, handle):
    drive_instance = gdrive_authenticator.get_drive_authenticators().get_instance(handle)
    converted_path = manage_gdrive_files.path_converter(path)
    link = manage_gdrive_files.get_file_link(drive_instance, converted_path)
    return {'link': f"{link}"}, 201