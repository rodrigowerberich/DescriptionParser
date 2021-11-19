from flask import Flask, request
from flask_cors import CORS

import import_request_receiver
import export_request_receiver
import update_descriptions_receiver

app = Flask(__name__)
CORS(app)


@app.route('/import_spreadsheet_from_google_drive', methods=['POST'])
def import_spreadsheet_from_google_drive():
    print(request.headers)
    print(request.get_data())
    print(request.get_json())
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
