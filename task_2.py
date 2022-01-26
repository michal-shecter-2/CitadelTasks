import json


def check_json(file_name):
    try:
     with open(file_name) as f:
        return json.load(f)
    except FileNotFoundError:
         print('FileNotFoundError')
    except ValueError:
         print('json not valid' )

