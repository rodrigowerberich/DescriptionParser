from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from typing import AnyStr, Iterable


def path_converter(path_str: AnyStr):
    path_as_list = path_str.split('/')
    return path_as_list


def authenticate_drive():
    gauth = GoogleAuth()
    # Create local webserver which automatically handles authentication.
    gauth.LocalWebserverAuth()

    # Create GoogleDrive instance with authenticated GoogleAuth instance.
    drive = GoogleDrive(gauth)
    return drive


def get_children(drive, root_folder_id):
    str = "\'" + root_folder_id + "\'" + " in parents and trashed=false"
    file_list = drive.ListFile({'q': str}).GetList()
    return file_list


def find_file_by_name(file_list, file_name):
    for file in file_list:
        if (file['title'] == file_name):
            return file['id']
    return None


def get_file_id(drive, file_location):
    file_id = 'root'
    for name in file_location:
        children = get_children(drive, file_id)
        file_id = find_file_by_name(children, name)
        if not file_id:
            raise FileNotFoundError(str(name) +' was not found in drive in search for '+ str(file_location))
    return file_id


def import_spreadsheet_file_from_drive(drive: GoogleDrive, file_location: Iterable[AnyStr]):
    file_id = get_file_id(drive, file_location)
    file = drive.CreateFile({'id': file_id})
    spreadsheet_name = file_location[-1] + '.xlsx'
    # Aux seems to be a corner case file name in google drive
    if spreadsheet_name == 'Aux.xlsx':
        spreadsheet_name = '_' + spreadsheet_name
    file.GetContentFile(spreadsheet_name,
                        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


def export_spreadsheet_file_to_drive(drive: GoogleDrive, month: AnyStr, file_location: Iterable[AnyStr]):
    try:
        file_id = get_file_id(drive, file_location)
        file = drive.CreateFile({'id': file_id})
    except FileNotFoundError:
        parent_id = get_file_id(drive, file_location[0:-1])
        file = drive.CreateFile({'title': file_location[-1], 'parents': [{'id': parent_id}]})
    spreadsheet_name = month + '.xlsx'
    # Aux seems to be a corner case file name in google drive
    if spreadsheet_name == 'Aux.xlsx':
        spreadsheet_name = '_' + spreadsheet_name
    file.SetContentFile(spreadsheet_name)
    file.Upload({'convert': True})


def import_spreadsheet_file(file_location: Iterable[AnyStr]):
    drive = authenticate_drive()
    import_spreadsheet_file_from_drive(drive, file_location)
    return True


def import_spreadsheets_file(paths: Iterable[Iterable[AnyStr]]):
    drive = authenticate_drive()
    for path in paths:
        import_spreadsheet_file_from_drive(drive, path)
    return True


def export_spreadsheet_file(month, converted_export_path):
    drive = authenticate_drive()
    export_spreadsheet_file_to_drive(drive, month, converted_export_path)
    return True
