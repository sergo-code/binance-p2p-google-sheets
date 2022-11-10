import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheetsAPI:
    def __init__(self, spreadsheet_id, CREDENTIALS_FILE):
        self.CREDENTIALS_FILE = CREDENTIALS_FILE
        self.spreadsheet_id = spreadsheet_id

    def get_service_sacc(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

        return service

    def reader_sheets(self, _range, type):
        values = self.get_service_sacc().spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=_range,
            majorDimension='ROWS'
        ).execute()
        if type == 'int':
            try:
                return int(values['values'][0][0].replace(u'\xa0', '').split(',')[0])
            except ValueError:
                return False
        elif type == 'str':
            try:
                return values['values'][0][0] if values['values'][0][0] in ['RUB', '%'] else False
            except KeyError:
                return False

    def writer_sheets(self, data):
        self.get_service_sacc().spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": data
            }
        ).execute()

    def update_sheets(self, body):
        self.get_service_sacc().spreadsheets().batchUpdate(spreadsheetId=self.spreadsheet_id, body=body).execute()
