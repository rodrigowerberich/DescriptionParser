from typing import AnyStr, Iterable
import gdrive_authenticator


def local_authentication():
    drive_instance = gdrive_authenticator.local_authentication_cycle()
    drive_authenticators = gdrive_authenticator.get_drive_authenticators()
    handle = drive_authenticators.generate_handle(drive_instance)
    return {'handle': handle}, 201