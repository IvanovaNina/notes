import json
import os
import copy
from datetime import datetime

FILE_NAME = 'notes.json'
ENCODING = 'UTF-8'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def save(notes):
    to_save = copy.deepcopy(notes)
    for note in to_save:
        note['created_at'] = note['created_at'].strftime(DATE_FORMAT)
        note['updated_at'] = note['updated_at'].strftime(DATE_FORMAT)

    with open(FILE_NAME, 'w', encoding=ENCODING) as outfile:
        outfile.write(json.dumps(to_save, indent=4, sort_keys=True, default=str))


def load() -> list:
    if os.path.exists(FILE_NAME) and os.stat(FILE_NAME).st_size > 0:
        with open(FILE_NAME, 'r', encoding=ENCODING) as json_file:
            notes = json.load(json_file)
            for note in notes:
                note['created_at'] = datetime.strptime(note['created_at'], DATE_FORMAT)
                note['updated_at'] = datetime.strptime(note['updated_at'], DATE_FORMAT)
            return notes
    else:
        return []
