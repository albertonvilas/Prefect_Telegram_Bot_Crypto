from oauth2client.service_account import ServiceAccountCredentials
import gspread
import utils

def sheet_con():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
    client = gspread.authorize(creds)
    worksheet = client.open('crypto').sheet1
    return worksheet

def load_to_sheet(data):
    now = utils.date_now()
    worksheet = sheet_con()
    for elem in data:
        elem_values = [elem['base'], elem['currency'], elem['amount'], now]
        worksheet.append_row(elem_values)
        