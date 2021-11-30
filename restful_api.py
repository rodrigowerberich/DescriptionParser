from flask import Flask, request
from flask_cors import CORS

import authentication_receiver
import import_request_receiver
import export_request_receiver
import update_descriptions_receiver

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello_world():
    return "Hello leticia!"


@app.route('/request_login_to_google_drive', methods=['GET'])
def request_login_to_google_drive():
    result = authentication_receiver.request_login_to_google_drive()

    return result


@app.route('/login_to_google_drive', methods=['GET'])
def login_to_google_drive():
    result = authentication_receiver.local_authentication()

    return result


@app.route('/import_spreadsheet_from_google_drive_with_auth', methods=['POST'])
def import_spreadsheet_from_google_drive_with_auth():
    path = request.get_json()['path']
    handle = request.get_json()['handle']

    result = import_request_receiver.import_spreadsheet_from_google_drive_with_handle(path, handle)

    return result


@app.route('/export_spreadsheet_to_google_drive_with_auth', methods=['POST'])
def export_spreadsheet_to_google_drive_with_auth():
    month = request.get_json()['month']
    export_path = request.get_json()['export path']
    handle = request.get_json()['handle']

    result = export_request_receiver.export_spreadsheet_to_google_drive_with_auth(month, export_path, handle)

    return result


@app.route('/import_spreadsheet_from_google_drive', methods=['POST'])
def import_spreadsheet_from_google_drive():
    path = request.get_json()['path']

    result = import_request_receiver.import_spreadsheet_from_google_drive(path)

    return result


@app.route('/import_spreadsheets_from_google_drive', methods=['POST'])
def import_spreadsheets_from_google_drive():
    paths = request.get_json()['paths']

    result = import_request_receiver.import_spreadsheets_from_google_drive(paths)

    return result


@app.route('/update_descriptions', methods=['POST'])
def update_descriptions():
    month = request.get_json()['month']
    account_name = request.get_json()['account']

    result = update_descriptions_receiver.update_descriptions(month, account_name)

    return result


@app.route('/export_spreadsheet_to_google_drive', methods=['POST'])
def export_spreadsheet_to_google_drive():
    month = request.get_json()['month']
    export_path = request.get_json()['export path']

    result = export_request_receiver.export_spreadsheet_to_google_drive(month, export_path)

    return result
