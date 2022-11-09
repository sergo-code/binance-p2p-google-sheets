def startup_table(sheets):
    cell_format = {
        "backgroundColor": {'red': 1, 'green': 1, 'blue': 1},
        "horizontalAlignment": "CENTER",
        "textFormat": {
            "foregroundColor": {'red': 0, 'green': 0, 'blue': 0},
            "fontFamily": "Arial",
            "fontSize": 10,
            "bold": True
        }
    }

    cells_range = {
        "startRowIndex": 0,
        "endRowIndex": 267,
        "startColumnIndex": 0,
        "endColumnIndex": 8
    }

    header_sheet = {
        'coordinates': [
            {
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 0,
                "endColumnIndex": 1
            },
            {
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 2,
                "endColumnIndex": 3
            },
            {
                "startRowIndex": 0,
                "endRowIndex": 1,
                "startColumnIndex": 4,
                "endColumnIndex": 5
            },
            {
                "startRowIndex": 2,
                "endRowIndex": 3,
                "startColumnIndex": 0,
                "endColumnIndex": 8
            },
            {
                "startRowIndex": 15,
                "endRowIndex": 16,
                "startColumnIndex": 0,
                "endColumnIndex": 8
            },
            {
                "startRowIndex": 25,
                "endRowIndex": 26,
                "startColumnIndex": 0,
                "endColumnIndex": 8
            },
            {
                "startRowIndex": 73,
                "endRowIndex": 74,
                "startColumnIndex": 0,
                "endColumnIndex": 7
            },
            {
                "startRowIndex": 101,
                "endRowIndex": 102,
                "startColumnIndex": 0,
                "endColumnIndex": 7
            },
            {
                "startRowIndex": 129,
                "endRowIndex": 130,
                "startColumnIndex": 0,
                "endColumnIndex": 7
            },
            {
                "startRowIndex": 157,
                "endRowIndex": 158,
                "startColumnIndex": 0,
                "endColumnIndex": 7
            },
            {
                "startRowIndex": 185,
                "endRowIndex": 186,
                "startColumnIndex": 0,
                "endColumnIndex": 7
            },
            {
                "startRowIndex": 213,
                "endRowIndex": 214,
                "startColumnIndex": 0,
                "endColumnIndex": 7
            },
            {
                "startRowIndex": 241,
                "endRowIndex": 242,
                "startColumnIndex": 0,
                "endColumnIndex": 7
            }],
        'style': {
            "backgroundColor": {'red': 102, 'green': 0, 'blue': 0},
            "textFormat": {
                "foregroundColor": {'red': 1, 'green': 1, 'blue': 1},
                "fontFamily": "Arial",
                "fontSize": 10,
                "bold": True
            }
        }
    }

    body = {
        'requests': [
            {'repeatCell': {'range': cells_range,
                            'cell': {'userEnteredFormat': cell_format},
                            'fields': 'userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)'}
             }
        ]
    }
    for coord in header_sheet['coordinates']:
        obj = {'repeatCell': {'range': coord,
                              'cell': {'userEnteredFormat': header_sheet['style']},
                              'fields': 'userEnteredFormat(backgroundColor,textFormat)'}
               }
        body['requests'].append(obj)
    sheets.update_sheets(body)
