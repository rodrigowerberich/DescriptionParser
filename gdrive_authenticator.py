from pydrive.auth import GoogleAuth
from pydrive.drive import  GoogleDrive


class DriveAuthenticators:
    def __init__(self):
        self._handle_map = {}
        self._current_handle = 0

    def generate_handle(self, drive_instance: GoogleDrive):
        self._handle_map[self._current_handle] = drive_instance
        used_handle = self._current_handle
        self._current_handle = self._current_handle + 1
        return used_handle

    def get_instance(self, handle: int):
        print(self._handle_map.keys())
        return self._handle_map[handle]


_drive_authenticators = DriveAuthenticators()


def get_drive_authenticators():
    return _drive_authenticators


def local_authentication_cycle():
    gauth = GoogleAuth()
    # Create local webserver which automatically handles authentication.
    gauth.LocalWebserverAuth()

    # Create GoogleDrive instance with authenticated GoogleAuth instance.
    drive = GoogleDrive(gauth)
    return drive
